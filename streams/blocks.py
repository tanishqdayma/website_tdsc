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

# Services Page
class ServicesInfoBlock(blocks.StructBlock):

    point = blocks.CharBlock(required=True, help_text="Add a new service point")
    info = blocks.RichTextBlock(icon='text')

    class Meta: #noqa
        template = 'streams/services_info_block.html'
        icon='doc-full'
        label = "Text and Information"

# Projects page
class ProjectsIntendedOutcomesBlock(blocks.StructBlock):

    intended_outcomes = blocks.RichTextBlock(icon='text')
    
    class Meta: #noqa
        template = 'streams/projects_intended_outcomes_block.html'
        icon='doc-full'
        label = "Intended Outcomes"

class ProjectsDocumentsBlock(blocks.StructBlock):

    project_documents = blocks.RichTextBlock(icon='text') 

    class Meta: #noqa
        template = 'streams/projects_documents_block.html'
        icon='doc-full'
        label = "Project Documents"

class ProjectsOutputsBlock(blocks.StructBlock):

    project_outputs = blocks.RichTextBlock(icon='text')

    class Meta: #noqa
        template = 'streams/projects_outputs_block.html'
        icon='doc-full'
        label = "Project Outputs"

# Resources Page Blocks

class PointAndPdfBlock(blocks.StructBlock):
    """List and buttons of main"""

    heading = blocks.CharBlock(required=True)

    points = blocks.ListBlock(
            blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock(required=True, max_length=200)),
                        ("info", blocks.ListBlock(
                            blocks.StructBlock(
                            [
                                ("point", blocks.CharBlock(required=True, max_length=200)),
                                ("pdf", DocumentChooserBlock(required=False)),
                                    
                                
                            ]
                        )
                    )
                )
            ]        
        )
    )

    class Meta:  #noqa
        template = "streams/point_and_pdf_page.html"
        icon="edit"
        label="TDSC Documents"

class PointAndPdfsBlock(blocks.StructBlock):
    """List and buttons of main"""

    heading = blocks.CharBlock(required=True)

    points = blocks.ListBlock(
            blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock(required=True, max_length=200)),
                        ("info", blocks.ListBlock(
                            blocks.StructBlock(
                            [
                                ("point", blocks.CharBlock(required=True, max_length=200)),
                                ("pdf", DocumentChooserBlock(required=False)),
                                    
                                
                            ]
                        )
                    )
                )
            ]        
        )
    )

    class Meta:  #noqa
        template = "streams/point_and_pdf_page.html"
        icon="edit"
        label="TDSC Talks"


class PointAndURLBlock(blocks.StructBlock):
    """List and buttons of main"""
    heading = blocks.CharBlock(required=True)
    tools_and_resources = blocks.RichTextBlock(icon='text')

    class Meta:  #noqa
        template = "streams/point_and_url_page.html"
        icon="edit"
        label="TDSC Tools & Resources"

# Outreach Page Blocks
class TableRowHeadingBlock(blocks.StructBlock):

    heading = blocks.CharBlock(required=True)

    points = blocks.ListBlock(
            blocks.StructBlock(
                    [
                        ("SNo", blocks.IntegerBlock(required=True)),
                        ("title", blocks.RichTextBlock(icon='text')),
                        ("venue", blocks.RichTextBlock(icon='text')),
                        ("dates", blocks.RichTextBlock(icon='text')),
                        ("attendees", blocks.RichTextBlock(icon='text')),
                        ("host", blocks.RichTextBlock(icon='text')),
                    ]        
            )
    )

    class Meta:  #noqa
        template = "streams/table_row_page.html"
        icon="edit"
        label="Outreach Table"

# Contact Page Blocks
class SupervisorBlock(blocks.StructBlock):

    info = blocks.RichTextBlock(icon="text")

    cards = blocks.ListBlock(
            blocks.StructBlock(
                    [
                        ("photo", ImageChooserBlock(required=False)),
                        ("name", blocks.RichTextBlock(icon='text')),
                        ("Dept", blocks.RichTextBlock(icon='text')),
                        ("contact", blocks.RichTextBlock(icon='text')),
                        ("website", blocks.URLBlock(required=True)),
                    ]        
            )
    )

    class Meta:  #noqa
        template = "streams/supervisor_block.html"
        icon="edit"
        label="Supervisor Cards"

class ProjectEngineersBlock(blocks.StructBlock):
    """List and buttons of main"""

    info = blocks.RichTextBlock(icon="text")

    points = blocks.ListBlock(
            blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock(required=True, max_length=200)),
                        ("members", blocks.ListBlock(
                            blocks.StructBlock(
                            [
                                ("name", blocks.RichTextBlock(icon='text')),
                                ("designation", blocks.RichTextBlock(icon='text')),
                                ("email", blocks.EmailBlock()),
                                ("contact_no", blocks.RichTextBlock(icon='number')),
                            ]
                        )
                    )
                )
            ]        
        )
    )

    class Meta:  #noqa
        template = "streams/project_engineers_block.html"
        icon="edit"
        label="Project Engineer and Members"
