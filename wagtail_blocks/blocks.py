"""Block definitions"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageBlock

from wagtail_blocks import constants, values


class AccordionItem(blocks.StructBlock):
    """Accordion Item"""

    title = blocks.CharBlock(max_length=64, help_text=_("Item title"))
    content = blocks.RichTextBlock(help_text=_("Item content"))


class AccordionBlock(values.NameMixin, blocks.StructBlock):
    """
    Accordion is used for showing and hiding content
    but only one item can stay open at a time.
    """

    prefix = "accordion"

    style = blocks.ChoiceBlock(
        choices=constants.ACCORDION_STYLES,
        required=False,
        help_text=_("Accordion style"),
    )
    items = blocks.ListBlock(AccordionItem(), help_text=_("Accordion items"))

    class Meta:
        """Meta data"""

        icon = "collapse-down"
        label = _("Accordion")
        template = "wagtail/blocks/accordion.html"


class AlertBlock(blocks.StructBlock):
    """Alert informs users about important events."""

    level = blocks.ChoiceBlock(
        choices=constants.ALERT_LEVELS,
        help_text=_("Alert level"),
    )
    style = blocks.ChoiceBlock(
        choices=constants.ALERT_STYLES,
        required=False,
        help_text=_("Alert style"),
    )
    message = blocks.RichTextBlock(help_text=_("Alert message"))

    class Meta:
        """Meta data"""

        icon = "warning"
        label = _("Alert")
        value_class = values.AlertValue
        template = "wagtail/blocks/alert.html"


class CarouselBlock(blocks.StructBlock):
    """Carousel show images or content in a scrollable area."""

    items = blocks.ListBlock(ImageBlock(), help_text=_("Carousel items"))

    class Meta:
        """Meta data"""

        icon = "media"
        label = _("Carousel")
        value_class = values.CarouselValue
        template = "wagtail/blocks/carousel.html"


class CodeBlock(blocks.StructBlock):
    """Code block is used to show a block of code in a box that looks like a code editor."""

    language = blocks.ChoiceBlock(
        choices=constants.PROGRAMMING_LANGUAGES,
        help_text=_("Programming language"),
    )
    code = blocks.TextBlock(help_text=_("Code content"))

    class Meta:
        """Meta data"""

        icon = "code"
        label = _("Code")
        template = "wagtail/blocks/code.html"


class DiffBlock(blocks.StructBlock):
    """Diff block shows a side-by-side comparison of two items."""

    item_1 = ImageBlock(help_text=_("Diff Item 1"))
    item_2 = ImageBlock(help_text=_("Diff Item 2"))

    class Meta:
        """Meta data"""

        icon = "image"
        label = _("Diff")
        template = "wagtail/blocks/diff.html"


class DocumentBlock(blocks.StructBlock):
    """Document block shows a document card with a download button"""

    document = DocumentChooserBlock()

    class Meta:
        """Meta data"""

        icon = "doc-full"
        label = _("Document")
        value_class = values.DocumentValue
        template = "wagtail/blocks/document.html"


class HoverGalleryBlock(blocks.StructBlock):
    """
    Hover Gallery is container of images.
    The first image is visible be default and when we hover it horizontally,
    other images show up. Hover Gallery is useful for product cards in e-commerce sites,
    portfolios or in image galleries. Hover Gallery can include up to 10 images.
    """

    items = blocks.ListBlock(
        ImageBlock(),
        max_num=10,
        min_num=2,
        help_text=_("Gallery items"),
    )

    class Meta:
        """Meta data"""

        icon = "image"
        label = _("Gallery")
        template = "wagtail/blocks/hover_gallery.html"


class TabItem(blocks.StructBlock):
    """Tab items"""

    title = blocks.CharBlock(
        max_length=64,
        help_text=_("Tab title"),
    )
    content = blocks.StreamBlock(
        [
            ("alert", AlertBlock(help_text=_("Alert"))),
            ("code", CodeBlock(help_text=_("Code"))),
            ("image", ImageBlock(help_text=_("Image"))),
            ("video", EmbedBlock(help_text=_("Video"))),
            ("text", blocks.RichTextBlock(help_text=_("Text"))),
        ],
        help_text=_("Tab Content"),
    )


class TabsBlock(values.NameMixin, blocks.StructBlock):
    """Tabs can be used to show a list of links in a tabbed format."""

    prefix = "tabs"

    style = blocks.ChoiceBlock(
        choices=constants.TAB_STYLES,
        help_text=_("Tab style"),
    )
    items = blocks.ListBlock(
        TabItem(),
        help_text=_("Tab items"),
    )

    class Meta:
        """Meta data"""

        label = _("Tabs")
        icon = "dots-horizontal"
        template = "wagtail/blocks/tabs.html"
