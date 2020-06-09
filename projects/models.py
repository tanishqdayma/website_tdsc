from django.db import models
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
# from wagtailimages.blocks import ImageChooserBlock
from streams import blocks
from projects import projecttype
from django.utils import timezone
# from workshop.models import Event
# Create your models here.
# from wagtail.core.blocks import DateTimeBlock
# from datetime import datetime

class ProjectListingPage(Page):
    """Listing page lists all the Blog Detail Pages."""

    template = "projects/projects_listing_page.html"

    custom_heading = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title',
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("custom_heading"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = ProjectDetailPage.objects.live().public()
        # context["p_posts"] = PastWorkshopDetailPage.objects.live().public()
        return context


class ProjectDetailPage(Page):
    """Project detail page."""

    template = "projects/projects_detail_page.html"

    type_of_project = projecttype.TypesOfProjectsField(blank=False, null=True)
 
    project_description = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link','ol','ul'],null=True,blank=False)

    project_photo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    principal_investigator = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link','ol','ul'],null=True,blank=False)

    team = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link','ol','ul'],null=True,blank=False)

    content = StreamField(
    [
        ("outcomes", blocks.ProjectsIntendedOutcomesBlock()),
        ("documents", blocks.ProjectsDocumentsBlock()),
        ("outputs", blocks.ProjectsOutputsBlock())
    ],
    null=True,
    blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("type_of_project"),
        FieldPanel("project_description"),
        ImageChooserPanel("project_photo"),
        FieldPanel("principal_investigator"),
        FieldPanel("team"),       
        StreamFieldPanel("content"),
        # FieldPanel("address"),
        
        # StreamFieldPanel("contents"),
    ]
