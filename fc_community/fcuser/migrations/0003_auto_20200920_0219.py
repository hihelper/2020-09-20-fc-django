# Generated by Django 3.1.1 on 2020-09-20 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_auto_20200919_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(max_length=128, verbose_name='사용자이메일'),
        ),
    ]