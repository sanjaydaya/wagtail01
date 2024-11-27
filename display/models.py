from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.blocks import CharBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.models import Image
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from django.utils import timezone
from datetime import date


# Sponsor Model to be used in DisplayPage
@register_snippet
class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='sponsors_images'
    )
    code_snippet = models.CharField(max_length=255, blank=True, null=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('image'),
        FieldPanel('code_snippet'),
    ]

    def __str__(self):
        return self.name


# DisplayPage Model
class DisplayPage(Page):
    # Header Section with logo and navigation
    logo = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    banner_title = models.CharField(max_length=255)
    banner_button_text = models.CharField(max_length=50, default="Click")
    banner_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    banner_text = models.TextField(blank=True, null=True)

    # Features Section
    welcome_message = models.CharField(max_length=255, blank=True, null=True)
    feature_1 = models.CharField(max_length=255, blank=True, null=True)
    feature_2 = models.CharField(max_length=255, blank=True, null=True)
    feature_3 = models.CharField(max_length=255, blank=True, null=True)

    # StreamField for dynamic body content
    body = StreamField([
        ('heading', CharBlock(classname="full title", template="blocks/heading_block.html")),
        ('paragraph', RichTextBlock(classname="full richtext", template="blocks/paragraph_block.html")),
        ('image', ImageChooserBlock(classname="full image", template="blocks/image_block.html")),
    ], use_json_field=True, blank=True, null=True)

    # Marquee text and Footer
    marquee_text = models.CharField(max_length=255, blank=True, null=True)
    footer_text = models.TextField(blank=True, null=True)

    # Date field
    date = models.DateField(default=date.today)

    # Sponsors (Many-to-many relationship)
    sponsors = models.ManyToManyField(Sponsor, through='DisplayPageSponsor', related_name='display_pages')

    # Content panels for the admin interface
    content_panels = Page.content_panels + [
        FieldPanel('logo'),
        FieldPanel('banner_title'),
        FieldPanel('banner_button_text'),
        FieldPanel('banner_image'),
        FieldPanel('banner_text'),
        FieldPanel('welcome_message'),
        FieldPanel('feature_1'),
        FieldPanel('feature_2'),
        FieldPanel('feature_3'),
        MultiFieldPanel([
            InlinePanel('display_page_sponsors', label="Sponsor", min_num=1),
        ], heading="Sponsors"),
        FieldPanel('body'),
        FieldPanel('marquee_text'),
        FieldPanel('footer_text'),
        FieldPanel('date'),
    ]

    class Meta:
        verbose_name = "Display Page"


# DisplayPageSponsor Model for Linking Sponsors to DisplayPage
class DisplayPageSponsor(models.Model):
    page = ParentalKey(DisplayPage, on_delete=models.CASCADE, related_name='display_page_sponsors')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='+')

    panels = [
        FieldPanel('sponsor'),
    ]
