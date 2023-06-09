# Generated by Django 4.2.1 on 2023-07-02 12:45

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_description_long'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='фотография')),
                ('image_number', models.IntegerField(default=0, verbose_name='Номер картинки')),
            ],
            options={
                'verbose_name': 'картинка',
                'verbose_name_plural': 'картинки',
                'ordering': ['place'],
            },
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, default='', verbose_name='Краткое описание'),
        ),
        migrations.DeleteModel(
            name='PlaceImage',
        ),
        migrations.AddField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place'),
        ),
    ]
