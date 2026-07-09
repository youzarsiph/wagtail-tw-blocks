"""Block definitions"""

from django.core.validators import MaxValueValidator, MinValueValidator
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


class IDEBlock(blocks.StructBlock):
    """Embed online code editor like StackBlitz using a url"""

    title = blocks.CharBlock(
        required=False,
        help_text=_("Title of the iframe."),
    )
    url = blocks.CharBlock(
        required=False,
        help_text=_("IDE embed URL."),
    )


class CodePenBlock(IDEBlock):
    """Embed CodePen pens in your wagtail-powered sites"""

    slug_hash = blocks.CharBlock(
        required=True,
        help_text=_(
            "The slug hash of the Pen being embedded. Required or the embed will fail."
        ),
    )
    user = blocks.CharBlock(
        required=False,
        help_text=_("The CodePen username associated with the Pen."),
    )
    theme_id = blocks.CharBlock(
        required=False,
        help_text=_(
            "Theme ID for the embed. "
            "Use -1 for Light, -3 for Dark, or a custom theme ID."
        ),
    )
    height = blocks.IntegerBlock(
        required=False,
        help_text=_("Height of the embed iframe in pixels."),
    )
    default_tab = blocks.CharBlock(
        required=False,
        help_text=_(
            "Deprecated: default tab to show (e.g. 'css,result'). "
            "Prefer using `file` and `preview` instead."
        ),
    )
    file = blocks.CharBlock(
        required=False,
        help_text=_(
            "Default file to show in the embed (e.g. '/.codepen/pen.config.json'). "
            "Leave empty to show the first file alphabetically."
        ),
    )
    preview = blocks.BooleanBlock(
        required=False,
        help_text=_(
            "Whether to show preview mode. "
            "True = click-to-play preview, False = hide preview, None = normal iframe preview."
        ),
    )
    zoom = blocks.FloatBlock(
        required=False,
        help_text=_(
            "Zoom level for the preview. "
            "1 = normal, 0.5 = half-size, 0.25 = quarter-size."
        ),
    )
    editable = blocks.BooleanBlock(
        required=False,
        help_text=_(
            "Enable live editing inside the embed. "
            "Only one file can be edited at a time."
        ),
    )
    css_class = blocks.CharBlock(
        required=False,
        help_text=_(
            "Optional CSS class to apply to the embed wrapper for custom styling."
        ),
    )
    prefill = blocks.TextBlock(
        required=False,
        help_text=_(
            "JSON-like data for Prefill Embeds. "
            "Used when embedding code directly instead of referencing a saved Pen."
        ),
    )

    class Meta:
        """Meta data"""

        icon = "code"
        label = _("CodePen embeds")
        value_class = values.CodePenValue
        template = "wagtail/blocks/code/pen.html"


class CodeSandboxBlock(IDEBlock):
    """Embed CodeSandbox in your wagtail-powered sites"""

    class Meta:
        """Meta data"""

        icon = "code"
        label = _("CodeSandbox embeds")
        template = "wagtail/blocks/code/sandbox.html"


class StackBlitzBlock(IDEBlock):
    """Embed StackBlitz in your wagtail-powered sites"""

    ctl = blocks.BooleanBlock(
        required=False,
        help_text=_("Prompts users to “click to load” the embed."),
    )
    devtoolsheight = blocks.IntegerBlock(
        required=False,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text=_("Sets the height of the console in the editor preview."),
    )
    embed = blocks.BooleanBlock(
        required=False,
        help_text=_("Forces embed view regardless of screen size."),
    )
    file = blocks.CharBlock(
        required=False,
        help_text=_("Specifies the default file to have open in the editor."),
    )
    hidedevtools = blocks.BooleanBlock(
        required=False,
        help_text=_("Hides the console in the editor preview."),
    )
    hideExplorer = blocks.BooleanBlock(
        required=False,
        help_text=_("Hides the file explorer pane in embed view."),
    )
    hideNavigation = blocks.BooleanBlock(
        required=False,
        help_text=_("Hides the preview's URL bar."),
    )
    hideNavigation = blocks.BooleanBlock(
        required=False,
        help_text=_("Hides the preview's URL bar."),
    )
    initialpath = blocks.URLBlock(
        required=False,
        help_text=_(
            "Specifies the initial URL path (URI encoded) the preview should open."
        ),
    )
    showSidebar = blocks.BooleanBlock(
        required=False,
        help_text=_("Shows the sidebar in embed view (large viewports only)"),
    )
    startScript = blocks.CharBlock(
        required=False,
        help_text=_(
            "Specifies the npm script to run on project load (WebContainers-based projects only)."
        ),
    )
    terminalHeight = blocks.IntegerBlock(
        required=False,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text=_("Sets the height of the terminal."),
    )
    theme = blocks.ChoiceBlock(
        required=False,
        choices=[("light", _("Light")), ("dark", _("Dark"))],
        help_text=_("Sets the color theme of the editor UI."),
    )
    view = blocks.ChoiceBlock(
        required=False,
        choices=[("editor", _("Editor")), ("preview", _("Preview"))],
        help_text=_("Specifies which view to open by default."),
    )

    class Meta:
        """Meta data"""

        icon = "code"
        label = _("StackBlitz embeds")
        value_class = values.StackBlitzValue
        template = "wagtail/blocks/code/stack_blitz.html"


class ExpoSnackBlock(blocks.StructBlock):
    """Embed Expo snacks in your wagtail-powered sites"""

    id = blocks.CharBlock(
        required=False,
        help_text=_(
            "Id of the saved Snack. "
            "When specified, `code` and `dependencies` are ignored."
        ),
    )
    name = blocks.CharBlock(
        required=False,
        help_text=_("Name of the Snack."),
    )
    description = blocks.CharBlock(
        required=False,
        help_text=_("Description of the Snack."),
    )
    code = blocks.TextBlock(
        required=False,
        help_text=_("JavaScript code to use for the Snack."),
    )
    dependencies = blocks.CharBlock(
        required=False,
        help_text=_(
            "Comma separated list of dependencies to include in the Snack. "
            "The dependency version is optional. When omitted the version "
            "that is compatible with the selected SDK version is used."
        ),
    )
    loading = blocks.ChoiceBlock(
        default="auto",
        required=False,
        choices=[
            ("auto", _("Auto")),
            ("lazy", _("Lazy")),
            ("eager", _("Eager")),
        ],
        help_text=_("iFrame loading attribute."),
    )
    platform = blocks.ChoiceBlock(
        default="web",
        required=False,
        choices=[
            ("web", _("Web")),
            ("ios", _("IOS")),
            ("android", _("Android")),
            ("mydevice", _("My Device")),
        ],
        help_text=_("The default platform to preview the Snack on."),
    )
    preview = blocks.BooleanBlock(
        default=True,
        required=False,
        help_text=_("Shows or hides the preview pane."),
    )
    sdkversion = blocks.CharBlock(
        required=False,
        help_text=_(
            "The Expo SDK version to use (eg. 38.0.0). "
            "Defaults to the latest released Expo SDK version."
        ),
    )
    supportedplatforms = blocks.CharBlock(
        required=False,
        help_text=_(
            "The platforms available for previewing the Snack."
            "Defaults to `mydevice,ios,android,web` when not specified."
        ),
    )
    theme = blocks.ChoiceBlock(
        default="light",
        choices=[("light", _("Light")), ("dark", _("Dark"))],
        help_text=_(
            "The theme to use, light or dark. "
            "When omitted uses the theme that was configured by the user (defaults to light)."
        ),
    )
    deviceappearance = blocks.ChoiceBlock(
        required=False,
        choices=[("light", _("Light")), ("dark", _("Dark"))],
        help_text=_(
            "The device appearance to use, `light` or `dark`. "
            "When omitted, uses fallback to Snack theme (defaults to `undefined`)."
        ),
    )

    class Meta:
        """Meta data"""

        icon = "code"
        label = _("Expo snack embeds")
        value_class = values.ExpoSnackValue
        template = "wagtail/blocks/code/expo_snack.html"
