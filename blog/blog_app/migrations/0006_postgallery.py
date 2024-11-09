# Generated by Django 4.2.15 on 2024-10-16 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='gallery/', verbose_name='Фото')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='blog_app.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Фото поста',
                'verbose_name_plural': 'Фото поста',
            },
        ),
    ]