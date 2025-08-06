# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create new Django project and configure the settings
RUN django-admin startproject core
RUN cp -r wagtail_blocks core

# Configure settings
RUN echo "AUTH_USER_MODEL = 'users.User'" >> core/settings.py
RUN echo "INSTALLED_APPS += [" >> core/settings.py
RUN echo "    # Wagtail Blocks" >> core/settings.py
RUN echo "    'wagtail_blocks'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.answers'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.assignments'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.blog'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.categories'," >> core/settings.py
RUN echo "    'wagtail_blocks.cms'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.courses'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.enrollments'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.items'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.lessons'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.modules'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.notifications'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.paths'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.posts'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.questions'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.reviews'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.submissions'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.tags'," >> core/settings.py
RUN echo "    'wagtail_blocks'," >> core/settings.py
RUN echo "    'wagtail_blocks.apps.users'," >> core/settings.py
RUN echo "    # Deps" >> core/settings.py
RUN echo "    'rest_wind'," >> core/settings.py
RUN echo "    'rest_framework'," >> core/settings.py
RUN echo "    'wagtail.contrib.forms'," >> core/settings.py
RUN echo "    'wagtail.contrib.redirects'," >> core/settings.py
RUN echo "    'wagtail.embeds'," >> core/settings.py
RUN echo "    'wagtail.sites'," >> core/settings.py
RUN echo "    'wagtail.users'," >> core/settings.py
RUN echo "    'wagtail.snippets'," >> core/settings.py
RUN echo "    'wagtail.documents'," >> core/settings.py
RUN echo "    'wagtail.images'," >> core/settings.py
RUN echo "    'wagtail.search'," >> core/settings.py
RUN echo "    'wagtail.admin'," >> core/settings.py
RUN echo "    'wagtail'," >> core/settings.py
RUN echo "    'modelcluster'," >> core/settings.py
RUN echo "    'taggit'," >> core/settings.py
RUN echo "]" >> core/settings.py

# Setup URLConf
RUN echo "from django.urls import include" >> core/urls.py
RUN echo "urlpatterns += [path('', include('wagtail_blocks.urls'))]" >> core/urls.py

# Run migrations
RUN cd core && python manage.py migrate


WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && cwagtail_blocksn -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi"]
