# wagtail-tw-blocks

[![CI](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/ci.yml)
[![CD](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/cd.yml)
[![Code Style: Black](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/black.yml)
[![Code Linting: Ruff](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/wagtail-tw-blocks/actions/workflows/ruff.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/wagtail-tw-blocks?logo=pypi&logoColor=white)](https://pypi.org/project/wagtail-tw-blocks/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wagtail-tw-blocks?logo=python&logoColor=white)](https://pypi.org/project/wagtail-tw-blocks/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/wagtail-tw-blocks?logo=pypi&logoColor=white)](https://pypi.org/project/wagtail-tw-blocks/)
[![PyPI - License](https://img.shields.io/pypi/l/wagtail-tw-blocks?logo=pypi&logoColor=white)](https://pypi.org/project/wagtail-tw-blocks/)

## Overview

**wagtail-tw-blocks** is a collection of reusable, production-ready content blocks for Wagtail CMS, styled with Tailwind CSS and daisyUI. It provides a set of common UI components—ready to drop into your `StreamField`—so you can build rich, modern page layouts without reinventing the wheel.

---

## Key features

- **Modern design:** Tailwind CSS + daisyUI styling for clean, responsive layouts.
- **Multiple themes:** All daisyUI themes included, with easy customization.
- **CI/CD:** GitHub Actions pipelines for automated testing and deployment.

---

## Demo

[![Demo](https://img.youtube.com/vi/0b0dZByyPok/maxresdefault.jpg)](https://youtu.be/0b0dZByyPok)

---

## Available blocks

- **Accordion (Collapse):** Expandable/collapsible sections for FAQs or structured content.
- **Alert:** Highlight important messages or status updates.
- **Carousel:** Image or content slider with responsive design.
- **Code:** Syntax-highlighted code snippets for technical content (Requires `highlight.js` and `clipboard.js` to be included in your page).
- **Diff:** Side-by-side or inline difference highlighting for image comparisons.
- **FAB:** Floating Action Button with multiple action items.
- **Hover Gallery:** Image gallery with hover effects.
- **List:** Ordered lists with custom styling.
- **Steps:** Step-by-step process indicators.
- **Tabs:** Tabbed content sections.
- **Timeline:** Chronological event listings.
- **Toast:** Temporary notification messages.
- **Image:** Responsive images with optional captions.
- **Browser Mockup:** Browser window frame for screenshots or web content.
- **Phone Mockup:** Mobile phone frame for app screenshots or mobile content.
- **Window Mockup:** Desktop window frame for application screenshots or desktop content.

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
WB_CODE_BLOCK_PROGRAMMING_LANGUAGES = [
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

# Show or hide the header the CodeBlock
WB_CODE_BLOCK_SHOW_HEADER = True  # Default is True

# Show or hide the programming language label in the CodeBlock
WB_CODE_BLOCK_SHOW_PROGRAMMING_LANGUAGE = True  # Default is True

# Show or hide the copy button in the CodeBlock
WB_CODE_BLOCK_SHOW_COPY_BUTTON = True  # Default is True

# Show or hide window control buttons in the CodeBlock
WB_CODE_BLOCK_SHOW_WINDOW_CONTROLS = True  # Default is True
```

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
            # ...
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
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Wagtail Blocks Usage Example</title>

    <!-- Code highlighting for CodeBlock -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/github-dark.min.css"
    />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>

    <!-- Include stylesheet -->
    {% load static %}
    <link href="{% static 'wagtail_blocks/css/styles.css' %}" rel="stylesheet" type="text/css" />
  </head>

  <body>
    <main>
      <h1>{{ article.title }}</h1>
      
      <div>{{ article.content }}</div>
    </main>

    <!-- Lucide icons: https://lucide.dev/icons/ -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <script>lucide.createIcons();</script>

    <!-- For copy buttons in CodeBlock -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.11/clipboard.min.js"></script>
    <script>const btns = new ClipboardJS(".btn-copy");</script>
  </body>
</html>
```

---

## Extending

You can easily extend or customize the provided blocks by sub-classing them. For example, to create a custom alert block with additional styles:

```python
from wagtail_blocks import blocks

class CustomAlertBlock(blocks.AlertBlock):

    class Meta:
        template = "path/to/your/custom_alert_template.html"
        icon = "warning"
        label = "Custom Alert"
```

---

## Contributing

We welcome community contributions. See the [CONTRIBUTING](CONTRIBUTING.md) guide for setup instructions, coding standards, and workflow. Opening an issue before major changes helps align on scope and direction.

---

## Support

For questions, bug reports, or feature requests, open an issue or join the conversation in [GitHub Discussions](https://github.com/youzarsiph/wagtail-tw-blocks/discussions).

---

## License

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
