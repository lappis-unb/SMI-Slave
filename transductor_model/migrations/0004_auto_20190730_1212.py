# Generated by Django 2.1.5 on 2019-07-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transductor_model', '0003_auto_20190624_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transductormodel',
            name='model_code',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, unique=True),
        ),
    ]
