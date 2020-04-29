from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock



class NewsBlock(blocks.StructBlock):
    """Text and date and nothing else."""

    text = blocks.CharBlock(required=True, help_text="Add news main line")
    date_of_event = blocks.DateBlock(blank=False, null=True)

    class Meta:  # noqa
        template = "streams/news_and_date_block.html"
        icon = "edit"
        label = "Text & Date"


class GalleryBlock(blocks.StructBlock):
    """Gallery Images block"""
    
    image = ImageChooserBlock(icon="image")
       
    class Meta:  #noqa
        template = "streams/gallery.html"
        icon="edit"
        label="Image"
