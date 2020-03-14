# Generated by Django 2.2.2 on 2019-07-31 00:50

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('meyer', '0003_auto_20190721_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subtopic',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='topic',
            name='content',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
