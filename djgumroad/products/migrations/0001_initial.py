# Generated by Django 3.0.11 on 2021-01-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='product_covers/')),
                ('slug', models.SlugField()),
                ('content_url', models.URLField(blank=True, null=True)),
                ('content_file', models.FileField(blank=True, null=True, upload_to='')),
                ('price', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]