from django.db import models
from django.db.models import CharField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
# from wagtail.core.fields import RichTextField

from wagtail.core.fields import StreamField
from streams import blocks
# from wagtail.admin.edit_handlers import TabbedInterface, ObjectList


class OutreachPage(Page):
    """Outreach Page Class"""

    template = "outreach/outreach_page.html"

    content = StreamField(
        [
            ("table", blocks.TableRowHeadingBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
        
    ]

    class Meta: #noqa
        verbose_name = "Outreach Page"
        verbose_name_plural = "Outreach Pages"




    

