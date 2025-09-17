"""Custom Wagtail CMS blocks"""

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageBlock

from wagtail_blocks import (
    ACCORDION_STYLE_VARIANTS,
    ALERT_LEVELS,
    ALERT_STYLE_VARIANTS,
    PROGRAMMING_LANGUAGES,
)


# Settings
PROGRAMMING_LANGUAGES = getattr(
    settings,
    "WAGTAIL_BLOCKS_PROGRAMMING_LANGUAGES",
    PROGRAMMING_LANGUAGES,
)

SHOW_PROGRAMMING_LANGUAGE = getattr(
    settings,
    "WAGTAIL_BLOCKS_SHOW_PROGRAMMING_LANGUAGE",
    True,
)

SHOW_COPY_BUTTON = getattr(
    settings,
    "WAGTAIL_BLOCKS_SHOW_COPY_BUTTON",
    True,
)


class ButtonBlock(blocks.StructBlock):
    """Action block (link)"""

    label = blocks.CharBlock(
        max_length=32,
        required=False,
        help_text=_("Action label"),
    )
    page = blocks.PageChooserBlock(
        required=False,
        help_text=_("Action internal link"),
    )
    url = blocks.URLBlock(
        required=False,
        help_text=_("Action external link"),
    )


class AccordionItemBlock(blocks.StructBlock):
    """Accordion Item"""

    is_expanded = blocks.BooleanBlock(
        default=False,
        required=False,
        help_text=_("Wether to show or hide item content"),
    )
    title = blocks.CharBlock(
        max_length=64,
        required=True,
        help_text=_("Item title"),
    )
    content = blocks.RichTextBlock(
        required=True,
        help_text=_("Item content"),
    )


class AccordionBlock(blocks.StructBlock):
    """Accordions block"""

    name = blocks.CharBlock(
        max_length=64,
        required=True,
        help_text=_("Accordion name"),
    )
    variant = blocks.ChoiceBlock(
        choices=ACCORDION_STYLE_VARIANTS,
        required=False,
        help_text=_("Style variant"),
    )
    items = blocks.ListBlock(
        AccordionItemBlock(),
        required=True,
        help_text=_("Accordion items"),
    )

    class Meta:
        """Meta data"""

        icon = "folder-open-inverse"
        template = "wagtail_blocks/blocks/accordion.html"


class AlertBlock(blocks.StructBlock):
    """Alert block"""

    variant = blocks.ChoiceBlock(
        choices=ALERT_STYLE_VARIANTS,
        required=False,
        help_text=_("Style variant"),
    )
    level = blocks.ChoiceBlock(
        choices=ALERT_LEVELS,
        required=False,
        help_text=_("Alert level"),
    )
    message = blocks.RichTextBlock(
        required=True,
        help_text=_("Alert message"),
        features=[
            "bold",
            "italic",
            "link",
            "document-link",
            "code",
            "superscript",
            "subscript",
            "strikethrough",
        ],
    )
    actions = blocks.ListBlock(
        ButtonBlock(
            required=False,
            help_text=_("Alert action"),
        ),
        required=False,
        help_text=_("Alert actions"),
    )

    class Meta:
        """Meta data"""

        icon = "warning"
        template = "wagtail_blocks/blocks/alert.html"


class CarouselItemBlock(blocks.StructBlock):
    """Carousel Item block"""

    image = ImageBlock(
        required=False,
        help_text=_("Image"),
    )
    video = EmbedBlock(
        required=False,
        help_text=_("Video"),
    )


class CarouselBlock(blocks.StructBlock):
    """Carousel block"""

    is_vertical = blocks.BooleanBlock(
        default=False,
        required=False,
        help_text=_("Designates if carousel is vertical or horizontal (default)"),
    )
    items = blocks.ListBlock(
        CarouselItemBlock(),
        required=True,
        help_text=_("Carousel items"),
    )

    class Meta:
        """Meta data"""

        icon = "image"
        template = "wagtail_blocks/blocks/carousel.html"


class CodeBlock(blocks.StructBlock):
    """Code block"""

    show_language = blocks.BooleanBlock(
        default=SHOW_PROGRAMMING_LANGUAGE,
        required=False,
        help_text=_("Wether to show or hide which programming language is used"),
    )
    show_copy_btn = blocks.BooleanBlock(
        default=SHOW_COPY_BUTTON,
        required=False,
        help_text=_("Wether to show or hide copy buttons"),
    )
    language = blocks.ChoiceBlock(
        choices=PROGRAMMING_LANGUAGES,
        default="auto",
        required=True,
        help_text=_("Programming language"),
    )
    code = blocks.TextBlock(
        required=True,
        help_text=_("Code content"),
    )

    class Meta:
        """Meta data"""

        icon = "code"
        template = "wagtail_blocks/blocks/code.html"


class DiffBlock(blocks.StructBlock):
    """Diff block"""

    item_1 = ImageBlock(
        required=True,
        help_text=_("Diff Item 1"),
    )
    item_2 = ImageBlock(
        required=True,
        help_text=_("Diff Item 2"),
    )

    class Meta:
        """Meta data"""

        icon = "code"
        template = "wagtail_blocks/blocks/diff.html"
