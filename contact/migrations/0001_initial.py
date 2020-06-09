# Generated by Django 3.0.5 on 2020-06-08 14:45

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('supervisors', wagtail.core.fields.StreamField([('supervisors', wagtail.core.blocks.StructBlock([('info', wagtail.core.blocks.RichTextBlock(icon='text')), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('Dept', wagtail.core.blocks.RichTextBlock(icon='text')), ('contact', wagtail.core.blocks.RichTextBlock(icon='text')), ('website', wagtail.core.blocks.URLBlock(required=True))])))]))], blank=True, null=True)),
                ('project_manager', wagtail.core.fields.RichTextField(null=True)),
                ('project_engg', wagtail.core.fields.StreamField([('project_engg', wagtail.core.blocks.StructBlock([('info', wagtail.core.blocks.RichTextBlock(icon='text')), ('points', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('members', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.RichTextBlock(icon='text')), ('designation', wagtail.core.blocks.RichTextBlock(icon='text')), ('email', wagtail.core.blocks.EmailBlock()), ('contact_no', wagtail.core.blocks.RichTextBlock(icon='number'))])))])))]))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Contact Page',
            },
            bases=('wagtailcore.page',),
        ),
    ]