# Generated by Django 4.0 on 2022-01-27 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccms_site', '0006_menupage_delete_home_alter_book_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
