# Generated by Django 5.1.1 on 2024-09-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_faq_alter_category_options_alter_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'Вопрос-ответ', 'verbose_name_plural': 'Вопросы-ответы'},
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=150, verbose_name='Вопрос'),
        ),
    ]
