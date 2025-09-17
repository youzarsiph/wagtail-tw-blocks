# wagtail-tw-blocks

[![CI](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/ci.yml)
[![CD](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/cd.yml)
[![Code Style: Black](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/black.yml)
[![Code Linting: Ruff](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/ruff.yml)
[![Docker Image](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/docker-image.yml/badge.svg)](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/docker-image.yml)
[![Docker Publish](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/docker-publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/wagtail-tw-blocks?logo=pypi&logoColor=white)](https://pypi.org/project/wagtail-tw-blocks/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wagtail-tw-blocks?logo=python&logoColor=white)](https://pypi.org/project/wagtail-tw-blocks/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/wagtail-tw-blocks?logo=pypi&logoColor=white)](https://pypi.org/project/wagtail-tw-blocks/)
[![PyPI - License](https://img.shields.io/pypi/l/wagtail-tw-blocks?logo=pypi&logoColor=white)](https://pypi.org/project/wagtail-tw-blocks/)

## Overview

**wagtail-tw-blocks** is a collection of reusable, production-ready content blocks for Wagtail CMS, styled with Tailwind CSS and daisyUI. It provides a set of common UI components—ready to drop into your `StreamField`—so you can build rich, modern page layouts without reinventing the wheel.

---

## Available blocks

- **Accordion (Collapse):** Expandable/collapsible sections for FAQs or structured content.
- **Alert:** Highlight important messages or status updates.
- **Carousel:** Image or content slider with responsive design.
- **Code:** Syntax-highlighted code snippets for technical content (Requires `highlight.js` and `clipboard.js` to be included in your page).
- **Diff:** Side-by-side or inline difference highlighting for image comparisons.

---

## Installation

```bash
pip install wagtail-tw-blocks
```

---

## Configuration

Add `wagtail_blocks` to your `INSTALLED_APPS` **after** configuring your Wagtail settings:

```python
# project/settings.py

INSTALLED_APPS = [
    "wagtail_blocks",
    # ...
]
```

### Available settings

You can customize the behavior of `wagtail-tw-blocks` by adding the following settings to your Django settings file:

```python
# project/settings.py

# Extend or override the default programming languages for the CodeBlock
WAGTAIL_BLOCKS_PROGRAMMING_LANGUAGES = [
    ('python', 'Python'),
    ('javascript', 'JavaScript'),
    ('html', 'HTML'),
    ('css', 'CSS'),
    ('java', 'Java'),
    ('csharp', 'C#'),
    ('cpp', 'C++'),
    ('ruby', 'Ruby'),
    ('go', 'Go'),
    ('php', 'PHP'),
    # ...
]

# Show or hide the programming language label in the CodeBlock
WAGTAIL_BLOCKS_SHOW_PROGRAMMING_LANGUAGE = True  # Default is True

# Show or hide the copy button in the CodeBlock
WAGTAIL_BLOCKS_SHOW_COPY_BUTTON = True  # Default is True
---

## Usage example

```python
# blog/models.py

from wagtail_blocks import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from django.utils.translation import gettext_lazy as _


class Article(Page):
    content = StreamField(
        [
            ("accordion", blocks.AccordionBlock()),
            ("alert", blocks.AlertBlock()),
            ("carousel", blocks.CarouselBlock()),
            ("code", blocks.CodeBlock()),
            ("diff", blocks.DiffBlock()),
        ],
        help_text=_("Article content"),
    )

    content_panels = Page.content_panels + [
        FieldPanel("content"),
        # ...
    ]
```

```html
<!-- blog/base.html -->

{% load static %}

<!doctype html>

<html data-theme="luxury">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Wagtail Blocks Usage Example</title>
    <!-- You also may want to include TailwindCSS and daisyUI -->
    <link href="{% static 'wagtail_blocks/css/styles.css' %}" rel="stylesheet" type="text/css" />
  </head>

  <body>
    <!-- ... -->
     <main>
       {{ article.content }}
     </main>
  </body>
</html>
```

---

## Key features

- **Modern design:** Tailwind CSS + daisyUI styling for clean, responsive layouts.  
- **Multiple themes:** All daisyUI themes included, with easy customization.  
- **CI/CD:** GitHub Actions pipelines for automated testing and deployment.  
- **Dependency management:** Poetry for reproducible, maintainable installs.  
- **Code formatting:** Black for consistent, automatic formatting.  
- **Linting:** Ruff for fast, comprehensive linting.  
- **Testing:** Django test runner for unit and integration tests.  
- **Starter configs:** `.gitignore`, `pyproject.toml`, and other essentials included.

---

## Contributing

We welcome community contributions. See the [CONTRIBUTING](CONTRIBUTING.md) guide for setup instructions, coding standards, and workflow. Opening an issue before major changes helps align on scope and direction.

---

## Support

For questions, bug reports, or feature requests, open an issue or join the conversation in [GitHub Discussions](https://github.com/youzarsiph/wagtail-tw-blocks/discussions).

---

## License

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
