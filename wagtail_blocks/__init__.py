"""Wagtail Blocks"""

from django.utils.translation import gettext_lazy as _

# Constants
ACCORDION_STYLE_VARIANTS = [
    ("plus", _("Plus")),
    ("arrow", _("Arrow")),
]

ALERT_STYLE_VARIANTS = [
    ("soft", _("Soft")),
    ("outlined", _("Outlined")),
    ("dashed", _("Dashed")),
]

ALERT_LEVELS = [
    ("info", _("Info")),
    ("success", _("Success")),
    ("warning", _("Warning")),
    ("error", _("Error")),
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
