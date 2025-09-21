"""Wagtail Blocks"""

from django.utils.translation import gettext_lazy as _

# Constants
ACCORDION_STYLES = [
    ("plus", _("Plus")),
    ("arrow", _("Arrow")),
]

ALERT_STYLES = [
    ("soft", _("Soft")),
    ("outline", _("Outline")),
    ("dash", _("Dash")),
]

ALERT_LEVELS = [
    ("info", _("Info")),
    ("success", _("Success")),
    ("warning", _("Warning")),
    ("error", _("Error")),
]

COLOR_CHOICES = [
    ("primary", _("Primary")),
    ("secondary", _("Secondary")),
    ("accent", _("Accent")),
    ("success", _("Success")),
    ("info", _("Info")),
    ("warning", _("Warning")),
    ("error", _("Error")),
]

TAB_STYLES = [
    ("border", _("Border")),
    ("box", _("Box")),
    ("lift", _("Lift")),
]

# The popular programming languages
PROGRAMMING_LANGUAGES = [
    ("auto", _("Auto")),
    ("bash", "Bash"),
    ("c", "C"),
    ("cpp", "C++"),
    ("csharp", "C#"),
    ("css", "CSS"),
    ("dart", "Dart"),
    ("dockerfile", "Dockerfile"),
    ("go", "Go"),
    ("html", "HTML"),
    ("java", "Java"),
    ("javascript", "JavaScript"),
    ("json", "JSON"),
    ("kotlin", "Kotlin"),
    ("lua", "Lua"),
    ("markdown", "Markdown"),
    ("php", "PHP"),
    ("python", "Python"),
    ("ruby", "Ruby"),
    ("rust", "Rust"),
    ("scss", "SCSS"),
    ("shell", "Shell"),
    ("sql", "SQL"),
    ("swift", "Swift"),
    ("typescript", "TypeScript"),
    ("xml", "XML"),
    ("yaml", "YAML"),
    ("plaintext", _("Plain text")),
]
