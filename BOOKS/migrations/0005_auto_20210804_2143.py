# Generated by Django 2.2.6 on 2021-08-04 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKS', '0004_auto_20210804_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_genre',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='BOOKS.Genres'),
        ),
    ]
