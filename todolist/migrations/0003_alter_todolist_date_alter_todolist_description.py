# Generated by Django 4.1 on 2022-09-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_todolist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
