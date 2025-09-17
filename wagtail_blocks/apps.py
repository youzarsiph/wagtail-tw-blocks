"""AppConf for wagtail_blocks"""

from django.apps import AppConfig


# Create your config here.
class WagtailBlocksConfig(AppConfig):
    """App configuration for wagtail_blocks"""

    name = "wagtail_blocks"
    label = "wagtail_tw_blocks"
    default_auto_field = "django.db.models.BigAutoField"
