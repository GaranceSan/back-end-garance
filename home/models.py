from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField


class HomePage(Page):
    banner_title = models.CharField(max_length=100)
    banner_text = models.TextField(max_length=500)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_text"),
        FieldPanel("banner_image"),
    ]
    api_fields = [
        APIField("banner_title"),
        APIField("banner_text"),
        APIField("banner_image"),
    ]
