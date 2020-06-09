from django.db import models
from django.db.models import CharField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
# from wagtail.core.fields import RichTextField

from wagtail.core.fields import StreamField
from streams import blocks
# from wagtail.admin.edit_handlers import TabbedInterface, ObjectList


class ServicesPage(Page):
    """Services page class""" 

    template = "services/services_page.html"

    services_offered = StreamField(
		[
			("services",blocks.ServicesInfoBlock())
		],
		null=True,
		blank=True
	)

    ircc = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link','ol','ul'],null=True,blank=False)

    team = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link','ol','ul'],null=True,blank=False)
	
    areas_and_projects = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link','ol','ul'],null=True,blank=False)


    content_panels = Page.content_panels + [
         StreamFieldPanel("services_offered"),
         FieldPanel("ircc"),
         FieldPanel("team"),
         FieldPanel("areas_and_projects"),
        #  StreamFieldPanel("participate_points"),
        
      ]

    class Meta:
         verbose_name = "Services Page"




    

