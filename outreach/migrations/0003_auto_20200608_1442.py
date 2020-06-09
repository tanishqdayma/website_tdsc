# Generated by Django 3.0.5 on 2020-06-08 14:42

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('outreach', '0002_auto_20200606_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outreachpage',
            name='content',
            field=wagtail.core.fields.StreamField([('table', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=True)), ('points', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('SNo', wagtail.core.blocks.IntegerBlock(required=True)), ('title', wagtail.core.blocks.RichTextBlock(icon='text')), ('venue', wagtail.core.blocks.RichTextBlock(icon='text')), ('dates', wagtail.core.blocks.RichTextBlock(icon='text')), ('attendees', wagtail.core.blocks.RichTextBlock(icon='text')), ('host', wagtail.core.blocks.RichTextBlock(icon='text'))])))]))], blank=True, null=True),
        ),
    ]
