# Generated by Django 3.0.5 on 2020-05-28 14:36

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20200528_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcespage',
            name='content',
            field=wagtail.core.fields.StreamField([('docs', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=True)), ('points', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('info', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('point', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('pdf', wagtail.documents.blocks.DocumentChooserBlock(required=False))])))])))])), ('talks', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=True)), ('points', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('info', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('point', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('pdf', wagtail.documents.blocks.DocumentChooserBlock(required=False))])))])))])), ('tools', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=True)), ('points', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('point', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('url', wagtail.core.blocks.URLBlock(required=True))])))]))], blank=True, null=True),
        ),
    ]
