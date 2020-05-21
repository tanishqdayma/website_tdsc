# Generated by Django 3.0.5 on 2020-05-17 12:16

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectdetailpage',
            name='intended_outcomes',
        ),
        migrations.RemoveField(
            model_name='projectdetailpage',
            name='project_documents',
        ),
        migrations.RemoveField(
            model_name='projectdetailpage',
            name='project_outputs',
        ),
        migrations.AddField(
            model_name='projectdetailpage',
            name='content',
            field=wagtail.core.fields.StreamField([('outcomes', wagtail.core.blocks.StructBlock([('intended_outcomes', wagtail.core.blocks.RichTextBlock(icon='text'))])), ('documents', wagtail.core.blocks.StructBlock([('project_documents', wagtail.core.blocks.RichTextBlock(icon='text'))])), ('outputs', wagtail.core.blocks.StructBlock([('project_outputs', wagtail.core.blocks.RichTextBlock(icon='text'))]))], blank=True, null=True),
        ),
    ]