from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField


class BlogIndexPage(Page):
    display_title = models.CharField(max_length=100)
    intro = models.TextField(max_length=500)

    content_panels = Page.content_panels + [
        FieldPanel("display_title"),
        FieldPanel("intro"),
    ]
    max_count = 1

    api_fields = [
        APIField("display_title"),
        APIField("intro"),
    ]

    def __str__(self):
        return self.title


class BlogDetailPage(Page):
    pass
