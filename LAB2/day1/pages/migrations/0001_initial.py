# Generated by Django 5.0.4 on 2024-04-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('publishDate', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='photos/%Y/%m/%d')),
                ('version', models.IntegerField(default=1)),
                ('latestVersion', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
