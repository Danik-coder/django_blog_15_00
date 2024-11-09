from django import template

from blog_app.models import Category, FAQ

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_answer_question():
    all = FAQ.objects.all()
    question = all[0]
    answer = all[1]
    return [(q.question, q.answer) for q in all]

