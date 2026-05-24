# wagtail-tw-blocks

[![CI](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/ci.yml)
[![CD](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/cd.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/wagtail-tw-blocks?logo=pypi&logoColor=white)](https://pypi.org/project/wagtail-tw-blocks/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wagtail-tw-blocks?logo=python&logoColor=white)](https://pypi.org/project/wagtail-tw-blocks/)
[![PyPI - License](https://img.shields.io/pypi/l/wagtail-tw-blocks?logo=pypi&logoColor=white)](https://pypi.org/project/wagtail-tw-blocks/)

## Overview

**wagtail-tw-blocks** is a comprehensive library of production-ready `StreamField` components and UI elements designed for Wagtail CMS. Built on the foundation of **Tailwind CSS** and **daisyUI**, this package enables developers to rapidly deploy modern, accessible, and highly customizable layouts without the overhead of building foundational UI components from scratch.

---

## Core Features

- **Design-First Architecture:** Leverages Tailwind CSS and daisyUI for clean, responsive, and professional aesthetics.
- **Thematic Flexibility:** Full support for all daisyUI themes, allowing for effortless brand alignment.
- **Extensibility:** Architected for easy subclassing and template overriding to meet specific project requirements.

---

## Installation

### 1. Install via Pip

```bash
pip install wagtail-tw-blocks

```

### 2. Configure Django Settings

Add `wagtail_blocks` to your `INSTALLED_APPS`. Ensure it is placed after your core Wagtail configuration to ensure proper template loading.

```python
# settings.py

INSTALLED_APPS = [
    # ...
    "wagtail_blocks",
    # ...
]

```

---

## Available blocks & components

### Blocks

- **Accordion (Collapse):** Interactive, collapsible sections ideal for FAQs and structured data.

  ![Accordion Demo](https://github.com/user-attachments/assets/237cd36c-fa38-47c3-834f-a52df7052c32)

- **Alert:** Visual indicators for status updates, warnings, or informational highlights.

  ![Alert Demo](https://github.com/user-attachments/assets/cd51fdc7-1578-4bc6-9bf8-931a00012757)

- **Carousel:** A responsive content and image slider with intuitive navigation.

  ![Carousel Demo](https://github.com/user-attachments/assets/24fa83ef-8ae3-485d-9284-b88d112cc089)

- **Code:** Syntax-highlighted code blocks with integrated "copy-to-clipboard" functionality.
  (**Note:** Requires `highlight.js` and `clipboard.js`).

  ![Code Demo](https://github.com/user-attachments/assets/b7c076db-8a01-4295-8507-add12ad1ad7c)

- **Document:** Displays document info inside a card with download button.

  ![Document Demo](https://github.com/user-attachments/assets/5131c90c-bfee-4318-85db-5b8b92bd31ce)

- **Diff:** Side-by-side visual comparison tools for images.

  ![Diff Demo](https://github.com/user-attachments/assets/0ec9e29c-7999-4671-acfc-d675cae74da3)

- **Hover Gallery:** An immersive image gallery featuring sophisticated hover interactions.

  ![Gallery Demo](https://github.com/user-attachments/assets/3c05fc0e-9e1d-4840-9e65-92b541a16d75)

- **Tabs:** Efficient organization of content into navigable tabbed interfaces.

  ![Tabs Demo](https://github.com/user-attachments/assets/9e461e9c-c3d9-4fe0-9c51-874fa442f7ca)

#### Implementation Example

To integrate these blocks into your page models, import the block library into your `models.py`:

```python
from wagtail_blocks import blocks
from wagtail.fields import StreamField
from wagtail.models import Page

class Article(Page):
    content = StreamField([
        ("accordion", blocks.AccordionBlock()),
        ("alert", blocks.AlertBlock()),
        ("carousel", blocks.CarouselBlock()),
        ("code", blocks.CodeBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]

```

To ensure full functionality (specifically for the **Code Block**), include the following assets in your base template:

```html
<link rel="stylesheet" href="{% static 'wagtail_blocks/css/styles.css' %}" />
<link
  rel="stylesheet"
  href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/github.min.css"
/>

<script src="https://unpkg.com/lucide@latest"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.11/clipboard.min.js"></script>

<script>
  // Initialization
  lucide.createIcons();
  hljs.highlightAll();
  new ClipboardJS(".btn-copy");
</script>
```

#### Extending

You can easily extend or customize the provided blocks by sub-classing them.
For example, to create a custom alert block with additional styles:

```python
from wagtail_blocks.blocks import AlertBlock

class CustomAlertBlock(AlertBlock):
    class Meta:
        icon = "warning"
        label = "Custom Alert"
        template = "path/to/your/custom_alert_template.html"
```

---

### Components

Beyond `StreamField` blocks, this package includes reusable template components to enhance global site functionality.

#### Breadcrumbs

Automatic breadcrumb generation following the Wagtail page hierarchy.

- **Context:** a Wagtail `page`.
- **Usage:**

  ```html
  {% extends 'app/base.html' %}

  <!---->
  {% block content %}
  <section class="container-prose">
    {% include 'wagtail/components/breadcrumbs.html' %}

    <h1>{{ page.title }}</h1>
  </section>
  {% endblock %}
  ```

- **Demo:**

  ![Breadcrumbs demo](https://github.com/user-attachments/assets/58a99988-b942-4b21-bedd-738a5fdc3b81)

#### Forms

Accessible, daisyUI-styled wrappers for standard Django forms.

- **Context:** A Django `form`.
- **Options:**
  - `method`: Form `method` attribute (Defaults to `post`).
  - `action`: Form `action` attribute (Defaults to `''`).
  - `csrf`: A boolean that indicates whether to include Django `{% csrf_token %}` in the form (Defaults to `True`).
- **Usage:**

  ```html
  {% extends 'app/base.html' %}

  <!---->
  {% block content %}
  <section class="container-prose">
    <h1>New User</h1>

    {% include 'wagtail/components/form.html' %}

    <!-- Pass the options using `with` keyword: -->
    {% include 'wagtail/components/form.html' with method="get" csrf=False %}
  </section>
  {% endblock %}
  ```

- **Demo:**

  ![Forms demo](https://github.com/user-attachments/assets/6740b422-1b0b-4f23-b979-64815e6796be)

#### Language switch

Seamless integration with Django/Wagtail `i18n` for multi-lingual sites.

- **Context:** `LANGUAGES` from `django.template.context_processors.i18n` or a Wagtail `page`.
- **Usage:**

  ```html
  {% extends 'app/base.html' %}{% load static %}

  <!---->
  {% block content %}
  <header class="absolute inset-x-0 top-0 z-10 backdrop-blur-3xl">
    <nav class="navbar p-4">
      <ul class="navbar-start gap-4">
        <li
          class="tooltip tooltip-bottom tooltip-primary"
          data-tip="Your Brand"
        >
          <h1>
            <a href="https://your.domain.com">
              <img
                alt="Your Brand"
                class="lg:size-8 2xl:size-10"
                src="{% static 'path/to/logo.png' %}"
              />
            </a>
          </h1>
        </li>
      </ul>

      <ul class="navbar-end gap-4">
        {% include 'wagtail/components/languages.html' %}
      </ul>
    </nav>
  </header>
  {% endblock %}
  ```

- **Demo:**

  ![Languages demo](https://github.com/user-attachments/assets/03774cb3-2518-4cc8-a162-98ced48eb833)

#### Theme switch

Switch between daisyUI themes with a single click.

- **Usage:**

  ```html
  {% extends 'app/base.html' %}{% load static %}

  <!---->
  {% block content %}
  <header class="absolute inset-x-0 top-0 z-10 backdrop-blur-3xl">
    <nav class="navbar p-4">
      <ul class="navbar-start gap-4">
        <li
          class="tooltip tooltip-bottom tooltip-primary"
          data-tip="Your Brand"
        >
          <h1>
            <a href="https://your.domain.com">
              <img
                alt="Your Brand"
                class="lg:size-8 2xl:size-10"
                src="{% static 'path/to/logo.png' %}"
              />
            </a>
          </h1>
        </li>
      </ul>

      <ul class="navbar-end gap-4">
        {% include 'wagtail/components/themes.html' %}
      </ul>
    </nav>
  </header>
  {% endblock %}
  ```

- **Demo:**

  ![Themes demo](https://github.com/user-attachments/assets/ef13b4fb-655f-476e-a532-df92a3bdda92)

#### Messages

Integrated support for the Django messages framework.

- **Context:** `messages` from `django.contrib.messages.context_processors.messages`.
- **Usage:**

  ```html
  {% extends 'app/base.html' %}

  <!---->
  {% block content %}
  <section class="container-prose">
    {% include 'wagtail/components/messages.html' %}

    <h1>Messages</h1>

    ...
  </section>
  {% endblock %}
  ```

- **Demo:**

  ![Messages demo](https://github.com/user-attachments/assets/9c20ca0b-c504-4cc5-9108-cd4af96b7b42)

#### Pagination

Professional pagination controls for `ListView` and QuerySets.

- **Context:**
  - `paginator`: Django paginator instance.
  - `page_obj`: Page instance.
  - `is_paginated`: Boolean that indicates whether the content is paginated or not.
  - `object_list`: Paginated QuerySet.
- **Usage:**

  ```html
  {% extends 'app/base.html' %}

  <!---->
  {% block content %}
  <section class="container-prose">
    <h1>Items</h1>

    <ol>
      {% for item in object_list %}
      <li>{{ item }}</li>
      {% endfor %}
    </ol>

    {% include 'wagtail/components/pagination.html' %}
  </section>
  {% endblock %}
  ```

- **Demo:**

  ![Pagination demo](https://github.com/user-attachments/assets/1d9a9e9e-8c82-40a5-b266-5508eadd5ebf)

#### Prev/Next

Smart pagination between sibling pages, with recursive fallback to parent pages.

- **Context:** A Wagtail `page`.
- **Usage:**

  ```html
  {% extends 'app/base.html' %}

  <!---->
  {% block content %}
  <section class="container-prose">
    <h1>{{ page.title }}</h1>

    {% include 'wagtail/components/prev_next.html' %}
  </section>
  {% endblock %}
  ```

- **Demo:**

  ![Prev/Next demo](https://github.com/user-attachments/assets/4b2352f6-cacb-47b8-a5b6-4109b0dac08b)

#### Tree

Recursive, tree-like navigation structures for documentation or complex sitemaps.

- **Context:** A Wagtail `page`.
- **Usage:**

  ```html
  {% extends 'app/base.html' %}

  <!---->
  {% block content %}
  <div class="drawer lg:drawer-open">
    <input id="drawer" type="checkbox" class="drawer-toggle" />

    <section class="drawer-content">
      <main class="container-prose">
        <h1>{{ page.title }}</h1>

        <label
          for="drawer"
          aria-label="open drawer"
          class="btn btn-sm btn-primary lg:btn-md 2xl:btn-lg"
        >
          <i data-lucide="menu" class="size-4 lg:size-6"></i>
          Menu
        </label>

        ...
      </main>
    </section>

    <section class="drawer-side z-50">
      <label
        for="drawer"
        aria-label="close drawer"
        class="drawer-overlay"
      ></label>

      <div
        class="relative flex size-full flex-col overflow-hidden lg:min-w-sm lg:max-w-sm 2xl:min-w-md 2xl:max-w-md"
      >
        <header
          class="absolute inset-x-0 top-0 z-10 p-4 backdrop-blur-3xl lg:p-6"
        >
          <div class="flex items-center justify-between gap-4">
            <h1>Docs</h1>

            <div
              class="tooltip tooltip-left rtl:tooltip-right lg:hidden"
              data-tip="Close"
            >
              <label
                for="sidebar"
                aria-label="close sidebar"
                class="btn btn-sm btn-square btn-ghost lg:btn-md 2xl:btn-lg"
              >
                <i data-lucide="x" class="size-4 lg:size-6"></i>
                <span class="sr-only">Close</span>
              </label>
            </div>
          </div>
        </header>

        <div class="max-h-dvh overflow-y-auto py-16 lg:py-20">
          <ul class="menu menu-sm w-full grow lg:menu-md 2xl:menu-lg">
            {% include 'wagtail/components/tree.html' %}
          </ul>
        </div>
      </div>
    </section>
  </div>
  {% endblock %}
  ```

- **Demo:**

  ![Tree demo](https://github.com/user-attachments/assets/8ed71d86-1799-4cf7-b320-a485030cd2fc)

---

## Contributing

We value community involvement. If you wish to contribute,
please review our [CONTRIBUTING.md](CONTRIBUTING.md) for coding standards and setup procedures.
For significant architectural changes, please open an issue first to discuss your proposed implementation.

## Technical Support

- **Bug Reports & Feature Requests:** Please utilize the [GitHub Issues](https://github.com/youzarsiph/wagtail-tw-blocks/issues) tracker.
- **General Inquiry:** Join the community in [GitHub Discussions](https://github.com/youzarsiph/wagtail-tw-blocks/discussions).

## License

This project is open-source software licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for further details.
