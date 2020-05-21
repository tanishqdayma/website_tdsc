from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField

from streams import blocks


class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
   
    panels = [
        ImageChooserPanel("carousel_image"),
        ]

class HomePage(Page):
    "Home Page Model"
    
    templates = "home/home_page.html"


    what_is_tdsc = models.TextField(max_length=1000, null=True,blank=True)

    important_links = RichTextField(features=['link'],null=True,blank=True)

    news = StreamField(
        [
            ("news", blocks.NewsBlock()),
        ],
        null=True,
        blank=True,
    )

    gallery = StreamField(
        [
            ("gallery", blocks.GalleryBlock()),
        ],
        null=True,
        blank=True,
    )

    

    content_panels = Page.content_panels + [

        MultiFieldPanel([
                InlinePanel("carousel_images", max_num=3, min_num=1, label="Image"),
            ],
            heading="Carousel Panel",
        ),
        FieldPanel("what_is_tdsc"),

        FieldPanel("important_links"),

        StreamFieldPanel("news"),           
        StreamFieldPanel("gallery"),           
     
    ]

