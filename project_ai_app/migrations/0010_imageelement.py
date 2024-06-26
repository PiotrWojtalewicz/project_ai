# Generated by Django 4.0 on 2024-05-27 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_ai_app', '0009_textelement'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='mediaphoto')),
            ],
        ),
    ]
