# Generated by Django 4.1 on 2022-09-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_todolist_date_alter_todolist_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.TextField(),
        ),
    ]
