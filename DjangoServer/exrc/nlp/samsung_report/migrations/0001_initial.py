# Generated by Django 4.1.4 on 2022-12-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SamsungReport',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('rank', models.TextField()),
                ('word', models.TextField()),
                ('count', models.TextField()),
            ],
            options={
                'db_table': 'samsung_report',
            },
        ),
    ]
