# Generated by Django 4.2.1 on 2023-06-09 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_state_alter_articles_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='State',
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]