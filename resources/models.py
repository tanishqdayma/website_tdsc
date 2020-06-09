from django.db import models
from django.db.models import CharField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
# from wagtail.core.fields import RichTextField

from wagtail.core.fields import StreamField
from streams import blocks
# from wagtail.admin.edit_handlers import TabbedInterface, ObjectList


class ResourcesPage(Page):
    """Resource Page Class"""

    template = "resources/resources_page.html"

    content = StreamField(
        [
            ("docs", blocks.PointAndPdfBlock()),
            ("talks", blocks.PointAndPdfsBlock()),
            ("tools", blocks.PointAndURLBlock()),
        ],
        null=True,
        blank=True,
    )

    # talks = StreamField(
    #     [
    #         ("talks", blocks.PointAndPdfBlock()),
    #     ],
    #     null=True,
    #     blank=True,
    # )

    # tools_and_resources = StreamField(
    #     [
    #         ("tools", blocks.PointAndURLBlock()),
    #     ],
    #     null=True,
    #     blank=True,
    # )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
        
    ]

    class Meta: #noqa
        verbose_name = "Resource Page"
        verbose_name_plural = "Resources Pages"




    

