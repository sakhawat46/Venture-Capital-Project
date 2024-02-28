# Generated by Django 4.2.4 on 2024-02-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venture_app', '0002_alter_member_additional_documents_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('organigation', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]
