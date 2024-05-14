# Generated by Django 5.0.4 on 2024-05-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0008_delete_reserve'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('reserve_id', models.AutoField(primary_key=True, serialize=False)),
                ('reserve_name', models.CharField(blank=True, max_length=50, null=True)),
                ('reserve_surname', models.CharField(blank=True, max_length=150, null=True)),
                ('reserve_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('reserve_number', models.CharField(max_length=20)),
                ('reserve_comment', models.TextField(blank=True, max_length=700, null=True)),
            ],
        ),
    ]
