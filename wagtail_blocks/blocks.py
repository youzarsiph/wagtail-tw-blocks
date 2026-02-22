"""Block definitions"""

import math
from typing import Any, Dict, Literal, Optional

from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageBlock

from wagtail_blocks import constants


class AccordionItem(blocks.StructBlock):
    """Accordion Item"""

    title = blocks.CharBlock(max_length=64, help_text=_("Item title"))
    content = blocks.RichTextBlock(help_text=_("Item content"))


class AccordionBlock(blocks.StructBlock):
    """
    Accordion is used for showing and hiding content
    but only one item can stay open at a time.
    """

    style = blocks.ChoiceBlock(
        choices=constants.ACCORDION_STYLES,
        required=False,
        help_text=_("Accordion style"),
    )
    items = blocks.ListBlock(AccordionItem(), help_text=_("Accordion items"))

    class Meta:
        """Meta data"""

        label = _("Accordion")
        icon = "collapse-down"
        template = "wagtail/blocks/accordion.html"

    def get_context(
        self,
        value: Dict[str, Any],
        parent_context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return {
            **super().get_context(value, parent_context),
            "name": get_random_string(5),
        }


class AlertBlock(blocks.StructBlock):
    """Alert informs users about important events."""

    level = blocks.ChoiceBlock(
        choices=constants.ALERT_LEVELS, help_text=_("Alert level")
    )
    style = blocks.ChoiceBlock(
        choices=constants.ALERT_STYLES, required=False, help_text=_("Alert style")
    )
    message = blocks.RichTextBlock(help_text=_("Alert message"))

    class Meta:
        """Meta data"""

        label = _("Alert")
        icon = "warning"
        template = "wagtail/blocks/alert.html"

    def get_icon(
        self,
        level: Optional[Literal["info", "success", "warning", "error"]],
    ) -> Literal[
        "info",
        "circle-check",
        "alert-triangle",
        "x-circle",
        "question-mark-circle",
    ]:
        """
        Get alert icon based on alert level.

        Args:
            level (str): Alert level

        Returns:
            str: Alert icon
        """

        match level:
            case "info":
                return level

            case "success":
                return "circle-check"

            case "warning":
                return "alert-triangle"

            case "error":
                return "x-circle"

            case None:
                return "question-mark-circle"

    def get_context(
        self,
        value: Dict[str, Any],
        parent_context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return {
            **super().get_context(value, parent_context),
            "icon": self.get_icon(value.get("level")),
        }


class CarouselBlock(blocks.StructBlock):
    """Carousel show images or content in a scrollable area."""

    items = blocks.ListBlock(ImageBlock(), help_text=_("Carousel items"))

    class Meta:
        """Meta data"""

        label = _("Carousel")
        icon = "media"
        template = "wagtail/blocks/carousel.html"

    def get_context(
        self,
        value: Dict[str, Any],
        parent_context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return {
            **super().get_context(value, parent_context),
            "item_count": len(value.get("items", 0)),
        }


class CodeBlock(blocks.StructBlock):
    """Code block is used to show a block of code in a box that looks like a code editor."""

    language = blocks.ChoiceBlock(
        choices=constants.PROGRAMMING_LANGUAGES, help_text=_("Programming language")
    )
    code = blocks.TextBlock(help_text=_("Code content"))

    class Meta:
        """Meta data"""

        label = _("Code")
        icon = "code"
        template = "wagtail/blocks/code.html"


class DiffBlock(blocks.StructBlock):
    """Diff block shows a side-by-side comparison of two items."""

    item_1 = ImageBlock(help_text=_("Diff Item 1"))
    item_2 = ImageBlock(help_text=_("Diff Item 2"))

    class Meta:
        """Meta data"""

        label = _("Diff")
        icon = "image"
        template = "wagtail/blocks/diff.html"


class DocumentBlock(blocks.StructBlock):
    """Document block shows a document card with a download button"""

    document = DocumentChooserBlock()

    class Meta:
        """Meta data"""

        label = _("Document")
        icon = "doc-full"
        template = "wagtail/blocks/document.html"

    def get_doc_size(self, size_bytes: int) -> str:
        """
        Converts a file size in bytes into a human-readable string (e.g., "1.43 MB").

        This method uses the binary prefix system (base 1024) and scales the
        unit dynamically based on the magnitude of the file size.

        Args:
            size_bytes (int): The total size of the document in bytes.

        Returns:
            str: A formatted string containing the scaled size and its unit.
        """

        if size_bytes <= 0:
            return "0 B"

        # Define the sequence of data units supported
        DATA_UNITS = ("B", "KB", "MB", "GB", "TB", "PB", "EB")

        # Determine the power of 1024 to which the size corresponds
        # log(size, 1024) returns the index of the unit in our DATA_UNITS tuple
        unit_index = int(math.floor(math.log(size_bytes, 1024)))

        # Safety check: ensure the index does not exceed our defined units
        unit_index = min(unit_index, len(DATA_UNITS) - 1)

        # Calculate the divisor: 1024 raised to the power of the unit index
        divisor = math.pow(1024, unit_index)

        # Scale the size and round to two decimal places for UI clarity
        scaled_size = round(size_bytes / divisor, 2)
        unit_label = DATA_UNITS[unit_index]

        return f"{scaled_size} {unit_label}"

    def get_context(
        self,
        value: Dict[str, Any],
        parent_context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return {
            **super().get_context(value, parent_context),
            "size": self.get_doc_size(value.get("document").file_size),
        }


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

        label = _("Gallery")
        icon = "image"
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


class TabsBlock(blocks.StructBlock):
    """Tabs can be used to show a list of links in a tabbed format."""

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

    def get_context(
        self,
        value: Dict[str, Any],
        parent_context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return {
            **super().get_context(value, parent_context),
            "name": get_random_string(5),
        }
