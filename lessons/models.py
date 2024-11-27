from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.blocks import CharBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel
from django.utils import timezone

class LessonsPage(Page):
    """The lessons page model."""
    body = StreamField([
        ('heading', CharBlock()),
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)  # Ensure to include `use_json_field=True` for recent Wagtail versions

    # Add default value for date field
    date = models.DateField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('date'),
    ]
