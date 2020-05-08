from django.db import models
from django.db.models import CharField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
# from wagtail.core.fields import RichTextField

from wagtail.core.fields import StreamField
from streams import blocks
# from wagtail.admin.edit_handlers import TabbedInterface, ObjectList


class AboutPage(Page):
    """About page class""" 

    template = "about/about_page.html"

    background = StreamField(
		[
			("background",blocks.RichtextBackgroundBlock())
		],
		null=True,
		blank=True
	)

    CTARA_response = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link','ol','ul'],null=True,blank=False)
    proposal = StreamField(
		[
			("proposal",blocks.RichtextProposalBlock())
		],
		null=True,
		blank=True
	)

    business_model = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link','ol','ul'],null=True,blank=False)
	
    content_panels = Page.content_panels + [
         StreamFieldPanel("background"),
         FieldPanel("CTARA_response"),
         StreamFieldPanel("proposal"),
         FieldPanel("business_model"),
        #  StreamFieldPanel("participate_points"),
        
      ]

    class Meta:
         verbose_name = "About Us Page"




    

