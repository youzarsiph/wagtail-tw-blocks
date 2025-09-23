"""Custom Wagtail CMS blocks"""

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageBlock as WImageBlock

from wagtail_blocks import (
    ACCORDION_STYLES,
    ALERT_LEVELS,
    ALERT_STYLES,
    COLOR_CHOICES,
    PROGRAMMING_LANGUAGES,
    TAB_STYLES,
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

SHOW_WINDOW_CONTROLS = getattr(
    settings,
    "WAGTAIL_BLOCKS_SHOW_WINDOW_CONTROLS",
    True,
)


class ImageBlock(blocks.StructBlock):
    """Image block with caption"""

    image = WImageBlock(
        required=True,
        help_text=_("Image"),
    )
    caption = blocks.CharBlock(
        max_length=128,
        required=False,
        help_text=_("Image caption"),
    )
    attribution = blocks.CharBlock(
        max_length=128,
        required=False,
        help_text=_("Image attribution"),
    )

    class Meta:
        """Meta data"""

        icon = "image"
        template = "wagtail_blocks/blocks/image.html"


class ButtonBlock(blocks.StructBlock):
    """Action block (link)"""

    icon = blocks.CharBlock(
        max_length=32,
        required=False,
        default="check-circle2",
        help_text=_("Icon name (lucide icons)"),
    )
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
    color = blocks.ChoiceBlock(
        choices=COLOR_CHOICES,
        required=False,
        help_text=_("Action button color"),
    )


class AccordionItem(blocks.StructBlock):
    """Accordion Item"""

    icon = blocks.CharBlock(
        max_length=32,
        required=False,
        default="check-circle2",
        help_text=_("Icon name (lucide icons)"),
    )
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
    """
    Accordion is used for showing and hiding content
    but only one item can stay open at a time.
    """

    name = blocks.CharBlock(
        max_length=64,
        required=True,
        help_text=_("Accordion name"),
    )
    style = blocks.ChoiceBlock(
        choices=ACCORDION_STYLES,
        required=False,
        help_text=_("Accordion style"),
    )
    items = blocks.ListBlock(
        AccordionItem(),
        required=True,
        help_text=_("Accordion items"),
    )

    class Meta:
        """Meta data"""

        icon = "collapse-down"
        template = "wagtail_blocks/blocks/accordion.html"


class AlertBlock(blocks.StructBlock):
    """Alert informs users about important events."""

    icon = blocks.CharBlock(
        max_length=32,
        required=False,
        default="alert-triangle",
        help_text=_("Icon name (lucide icons)"),
    )
    is_vertical = blocks.BooleanBlock(
        default=False,
        required=False,
        help_text=_("Designates if alert is vertical or horizontal (default)"),
    )
    style = blocks.ChoiceBlock(
        choices=ALERT_STYLES,
        required=False,
        help_text=_("Alert style"),
    )
    level = blocks.ChoiceBlock(
        choices=ALERT_LEVELS,
        required=True,
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
        ButtonBlock(),
        required=False,
        help_text=_("Alert actions"),
    )

    class Meta:
        """Meta data"""

        icon = "warning"
        template = "wagtail_blocks/blocks/alert.html"


class CarouselItem(blocks.StructBlock):
    """Carousel Items"""

    image = ImageBlock(
        required=False,
        help_text=_("Image"),
    )
    video = EmbedBlock(
        required=False,
        help_text=_("Video"),
    )
    caption = blocks.CharBlock(
        max_length=128,
        required=False,
        help_text=_("Caption"),
    )


class CarouselBlock(blocks.StructBlock):
    """Carousel show images or content in a scrollable area."""

    is_vertical = blocks.BooleanBlock(
        default=False,
        required=False,
        help_text=_("Designates if carousel is vertical or horizontal (default)"),
    )
    items = blocks.ListBlock(
        CarouselItem(),
        required=True,
        help_text=_("Carousel items"),
    )

    class Meta:
        """Meta data"""

        icon = "media"
        template = "wagtail_blocks/blocks/carousel.html"


class CodeBlock(blocks.StructBlock):
    """Code block is used to show a block of code in a box that looks like a code editor."""

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
    show_window_btns = blocks.BooleanBlock(
        default=SHOW_WINDOW_CONTROLS,
        required=False,
        help_text=_("Wether to show or hide window buttons"),
    )
    file_name = blocks.CharBlock(
        max_length=64,
        default="Untitled",
        required=True,
        help_text=_("File name"),
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
    """Diff component shows a side-by-side comparison of two items."""

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

        icon = "image"
        template = "wagtail_blocks/blocks/diff.html"


class FABBlock(blocks.StructBlock):
    """
    FAB (Floating Action Button) stays in the bottom corner of screen. It includes a
    focusable and accessible element with button role. Clicking or focusing it shows
    additional buttons (known as Speed Dial buttons) in a vertical arrangement or a
    flower shape (quarter circle).
    """

    is_flower = blocks.BooleanBlock(
        default=False,
        required=False,
        help_text=_("Designates if FAB is vertical or flower shaped (quarter circle)"),
    )
    toggle = ButtonBlock(
        required=True,
        help_text=_("FAB toggle btn"),
    )
    main = ButtonBlock(
        required=False,
        help_text=_("FAB main action"),
    )
    items = blocks.ListBlock(
        ButtonBlock(),
        required=True,
        help_text=_("FAB items"),
    )

    class Meta:
        """Meta data"""

        icon = "grip"
        template = "wagtail_blocks/blocks/fab.html"


class HoverGalleryItem(blocks.StructBlock):
    """Hover gallery items"""

    image = ImageBlock(
        required=True,
        help_text=_("Image"),
    )
    caption = blocks.CharBlock(
        max_length=128,
        required=False,
        help_text=_("Caption"),
    )


class HoverGalleryBlock(blocks.StructBlock):
    """
    Hover Gallery is container of images.
    The first image is visible be default and when we hover it horizontally,
    other images show up. Hover Gallery is useful for product cards in ecommerce sites,
    portfoilios or in image galleries. Hover Gallery can include up to 10 images.
    """

    items = blocks.ListBlock(
        HoverGalleryItem(),
        required=True,
        help_text=_("Gallery items"),
    )

    class Meta:
        """Meta data"""

        icon = "image"
        template = "wagtail_blocks/blocks/hover_gallery.html"


class TimelineItem(blocks.StructBlock):
    """Timeline item"""

    date = blocks.DateBlock(
        required=True,
        help_text=_("Item date"),
    )
    icon = blocks.CharBlock(
        max_length=32,
        required=False,
        default="check-circle2",
        help_text=_("Icon name (lucide icons)"),
    )
    content = blocks.CharBlock(
        max_length=128,
        required=True,
        help_text=_("Item content"),
    )


class TimelineBlock(blocks.StructBlock):
    """Timeline component shows a list of events in chronological order."""

    is_compact = blocks.BooleanBlock(
        default=False,
        required=False,
        help_text=_("Designates if timeline is compact"),
    )
    is_vertical = blocks.BooleanBlock(
        default=False,
        required=False,
        help_text=_("Designates if timeline is vertical or horizontal (default)"),
    )
    snap_to_icon = blocks.BooleanBlock(
        default=False,
        required=False,
        help_text=_("Designates if dates should snap to icons"),
    )
    items = blocks.ListBlock(
        TimelineItem(),
        required=True,
        help_text=_("Timeline items"),
    )

    class Meta:
        """Meta data"""

        icon = "calendar-alt"
        template = "wagtail_blocks/blocks/timeline.html"


class StepItem(blocks.StructBlock):
    """Step item"""

    name = blocks.CharBlock(
        max_length=64,
        required=True,
        help_text=_("Item name"),
    )
    icon = blocks.CharBlock(
        max_length=32,
        required=False,
        default="check-circle2",
        help_text=_("Icon name (lucide icons)"),
    )
    color = blocks.ChoiceBlock(
        choices=COLOR_CHOICES,
        required=False,
        help_text=_("Item color"),
    )


class StepsBlock(blocks.StructBlock):
    """Steps can be used to show a list of steps in a process."""

    is_vertical = blocks.BooleanBlock(
        default=False,
        required=False,
        help_text=_("Designates if Steps is vertical or horizontal (default)"),
    )
    items = blocks.ListBlock(
        StepItem(),
        required=True,
        help_text=_("Steps items"),
    )

    class Meta:
        """Meta data"""

        icon = "breadcrumb-expand"
        template = "wagtail_blocks/blocks/steps.html"


class TabItem(blocks.StructBlock):
    """Tab items"""

    title = blocks.CharBlock(
        max_length=64,
        required=True,
        help_text=_("Item title"),
    )
    is_selected = blocks.BooleanBlock(
        default=False,
        required=False,
        help_text=_("Designates if tab is selected"),
    )
    content = blocks.StreamBlock(
        [
            ("alert", AlertBlock(required=True, help_text=_("Alert"))),
            ("code", CodeBlock(required=True, help_text=_("Code"))),
            ("image", ImageBlock(required=True, help_text=_("Image"))),
            ("video", EmbedBlock(required=True, help_text=_("Video"))),
            ("text", blocks.RichTextBlock(required=True, help_text=_("Rich text"))),
        ],
        required=True,
        help_text=_("Tab Content"),
    )


class TabsBlock(blocks.StructBlock):
    """Tabs can be used to show a list of links in a tabbed format."""

    name = blocks.CharBlock(
        max_length=64,
        required=True,
        help_text=_("Tab name"),
    )
    is_reversed = blocks.BooleanBlock(
        default=False,
        required=False,
        help_text=_("Designates if tab buttons position is reversed"),
    )
    style = blocks.ChoiceBlock(
        choices=TAB_STYLES,
        default="border",
        required=True,
        help_text=_("Tab style"),
    )
    items = blocks.ListBlock(
        TabItem(),
        required=True,
        help_text=_("Tab items"),
    )

    class Meta:
        """Meta data"""

        icon = "dots-horizontal"
        template = "wagtail_blocks/blocks/tabs.html"


class ToastBlock(blocks.StructBlock):
    """Toast is a wrapper to stack elements, positioned on the corner of page."""

    items = blocks.ListBlock(
        AlertBlock(),
        required=True,
        help_text=_("Toast items"),
    )

    class Meta:
        """Meta data"""

        icon = "mail"
        template = "wagtail_blocks/blocks/toast.html"


class ListItem(blocks.StructBlock):
    """List item"""

    image = ImageBlock(
        required=False,
        help_text=_("Item image"),
    )
    title = blocks.CharBlock(
        max_length=64,
        required=True,
        help_text=_("Item title"),
    )
    description = blocks.CharBlock(
        max_length=128,
        required=False,
        help_text=_("Item description"),
    )
    page = blocks.PageChooserBlock(
        required=False,
        help_text=_("Item internal link"),
    )
    url = blocks.URLBlock(
        required=False,
        help_text=_("Item external link"),
    )
    actions = blocks.ListBlock(
        ButtonBlock(),
        required=False,
        help_text=_("Actions"),
    )


class ListBlock(blocks.StructBlock):
    """List is a vertical layout to display information in rows."""

    title = blocks.CharBlock(
        max_length=64,
        required=True,
        help_text=_("List title"),
    )
    items = blocks.ListBlock(
        ListItem(),
        required=True,
        help_text=_("List items"),
    )

    class Meta:
        """Meta data"""

        icon = "list-ol"
        template = "wagtail_blocks/blocks/list.html"


class PhoneMockupBlock(blocks.StructBlock):
    """Phone mockup shows a mockup of an iPhone."""

    show_camera = blocks.BooleanBlock(
        default=True,
        required=False,
        help_text=_("Wether to show or hide camera"),
    )
    wallpaper = ImageBlock(
        required=True,
        help_text=_("Phone wallpaper"),
    )

    class Meta:
        """Meta data"""

        icon = "mobile-alt"
        template = "wagtail_blocks/blocks/phone.html"


class BrowserMockupBlock(blocks.StructBlock):
    """Browser mockup shows a box that looks like a browser window."""

    show_url = blocks.BooleanBlock(
        default=True,
        required=False,
        help_text=_("Wether to show or hide toolbar"),
    )
    url = blocks.URLBlock(
        required=True,
        help_text=_("Browser URL"),
    )
    wallpaper = ImageBlock(
        required=True,
        help_text=_("Browser wallpaper"),
    )

    class Meta:
        """Meta data"""

        icon = "desktop"
        template = "wagtail_blocks/blocks/browser.html"


class WindowMockupBlock(blocks.StructBlock):
    """Window mockup shows a box that looks like an operating system window."""

    wallpaper = ImageBlock(
        required=True,
        help_text=_("Window wallpaper"),
    )

    class Meta:
        """Meta data"""

        icon = "desktop"
        template = "wagtail_blocks/blocks/window.html"


class CodeMockupBlock(blocks.StructBlock):
    """Code mockup is used to show a block of code in a box that looks like a code editor."""

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
        template = "wagtail_blocks/blocks/code_mockup.html"
