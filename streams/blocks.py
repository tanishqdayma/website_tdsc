from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


# Home Page Blocks
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

# About Page Blocks


class RichtextBackgroundBlock(blocks.StructBlock):
    """Richtext with all the features."""

    text1 = blocks.RichTextBlock(icon="text")
    text2 = blocks.RichTextBlock(icon="text")

    class Meta:  # noqa
        template = "streams/richtext_bg_block.html"
        icon = "doc-full"
        label = "Full RichText"

class RichtextProposalBlock(blocks.StructBlock):
    """Richtext with all the features."""

    text = blocks.RichTextBlock(icon='text')

    class Meta:  # noqa
        template = "streams/richtext_proposal_block.html"
        icon = "doc-full"
        label = "Full RichText"

