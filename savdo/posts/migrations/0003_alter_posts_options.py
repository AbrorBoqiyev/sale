# Generated by Django 5.0.6 on 2024-07-01 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_posts_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ('date_posted',)},
        ),
    ]
