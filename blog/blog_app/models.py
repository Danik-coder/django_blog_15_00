from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class FAQ(models.Model):
    question = models.CharField(max_length=150, verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return f"{self.question} - {self.answer[:50]}..."

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'


class Slider(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=75)
    subtitle = models.CharField(verbose_name='Подзаголовок', max_length=150)
    image = models.ImageField(upload_to='slider/', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cлайдер'
        verbose_name_plural = 'Cлайдер'

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', unique=True)
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')
    views = models.PositiveIntegerField(verbose_name='Просмотры', default=0)
    published_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    preview = models.ImageField(verbose_name='Превью', upload_to='posts/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    def get_preview(self):
        if self.preview:
            return self.preview.url
        return 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwTLmUQce5oCqaLebzXc4Lrxrh5qR9GSlBxQ&s'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-published_at']


class PostGallery(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='gallery', verbose_name='Пост', blank=True,
                             null=True)
    photo = models.ImageField(upload_to='gallery/', verbose_name='Фото', blank=True, null=True)

    class Meta:
        verbose_name = 'Фото поста'
        verbose_name_plural = 'Фото поста'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.post} - {self.author} - {self.created_at} - {self.text[:50]}..."

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']


class PostViews(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    session_id = models.TextField()


class Like(models.Model):
    user = models.ManyToManyField(User, related_name='likes')
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='likes')


class Dislike(models.Model):
    user = models.ManyToManyField(User, related_name='dislikes')
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='dislikes')




