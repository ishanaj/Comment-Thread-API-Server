# Generated by Django 3.1.1 on 2021-03-31 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuesAns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
