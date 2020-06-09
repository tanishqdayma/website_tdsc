from django.db import models
from django.db.models import CharField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
# from wagtail.core.fields import RichTextField

from wagtail.core.fields import StreamField
from streams import blocks
# from wagtail.admin.edit_handlers import TabbedInterface, ObjectList


class ContactPage(Page):
    """Contact page class""" 

    template = "contact/contact_page.html"

    supervisors = StreamField(
		[
			("supervisors",blocks.SupervisorBlock())
		],
		null=True,
		blank=True
	)

    project_manager = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link','ol','ul'],null=True,blank=False)

    project_engg = StreamField(
        [
            ("project_engg",blocks.ProjectEngineersBlock())
        ],
        null=True,
        blank=True
    )


    content_panels = Page.content_panels + [
         StreamFieldPanel("supervisors"),
         FieldPanel("project_manager"),
         StreamFieldPanel("project_engg"),
        
      ]

    class Meta: #noqa
         verbose_name = "Contact Page"




    

