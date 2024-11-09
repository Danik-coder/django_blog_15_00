# Generated by Django 5.1.1 on 2024-09-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_faq_options_alter_faq_answer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=150, verbose_name='Подзаголовок')),
                ('image', models.ImageField(upload_to='slider/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Cлайдер',
                'verbose_name_plural': 'Cлайдер',
            },
        ),
    ]
