# Generated by Django 3.0.5 on 2020-04-29 07:18

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='gallery',
            field=wagtail.core.fields.StreamField([('gallery', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(icon='image'))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='important_links',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='news',
            field=wagtail.core.fields.StreamField([('news', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Add news main line', required=True)), ('date_of_event', wagtail.core.blocks.DateBlock(blank=False, null=True))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='what_is_tdsc',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='HomePageCarouselImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('carousel_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_images', to='home.HomePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
