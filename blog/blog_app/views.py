from django.shortcuts import render, HttpResponse, redirect
from .models import Category, FAQ, Slider, Post, PostGallery, Comment, PostViews, Like, Dislike
from .forms import LoginForm, RegisterForm, CommentForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView


# Create your views here.
def home_page(request):
    faqs = FAQ.objects.all()
    slides = Slider.objects.all()
    posters = Post.objects.all()

    context = {
        'faqs': faqs,
        'slides': slides,
        'posters': posters,
    }
    return render(request, 'blog_app/index.html', context)


def contacts_page(request):
    return render(request, 'blog_app/contacts.html')


def faq_page(request):
    return render(request, 'blog_app/faq.html')


def about_page(request):
    return render(request, 'blog_app/about.html')


def category_page(request, pk):
    category = Category.objects.get(pk=pk)
    posts = Post.objects.filter(category=category)
    sort_query = request.GET.get('sort')
    if sort_query:
        posts = posts.order_by(sort_query)
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog_app/category.html', context)


def post_page(request, pk):
    if pk == 'all':
        posts = Post.objects.all()
        comment = Comment.objects.all()
        return render(request, 'blog_app/posts.html', {posts: 'posts'})
    post = Post.objects.get(pk=pk)
    gallery = PostGallery.objects.filter(post=post)
    comments = Comment.objects.filter(post=post)

    if not request.session.session_key:
        print('No session')
        request.session.save()

    session_key = request.session.session_key

    post_viewer = PostViews.objects.filter(post=post, session_id=session_key).count()
    if post_viewer == 0 and session_key != 'None':
        obj = PostViews(post=post, session_id=session_key)
        obj.save()

        post.views += 1
        post.save()

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.post = post
            form.save()
            return redirect('post', pk=post.pk)
    else:
        form = CommentForm()

    try:
        post.likes
    except Exception as e:
        Like.objects.create(post=post)

    try:
        post.dislikes
    except Exception as e:
        Dislike.objects.create(post=post)
    total_likes = post.likes.user.all().count()
    total_dislikes = post.dislikes.user.all().count()

    context = {
        'post': post,
        'gallery': gallery,
        'form': form,
        'comments': comments,
        'total_likes': total_likes,
        'total_dislikes': total_dislikes,
    }
    return render(request, 'blog_app/post.html', context)


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Неправильный логин или пароль')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'blog_app/login.html', context)


def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'blog_app/register.html', context)


def logout_page(request):
    logout(request)
    return redirect('home')


def create_post_page(request):
    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            for item in request.FILES.getlist('photos'):
                new_obj = PostGallery(
                    post=form,
                    photo=item
                )
                new_obj.save()
            return redirect('post', pk=form.pk)
    else:
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'blog_app/create_post.html', context)


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('home')


class PostUpdateView(UpdateView):
    model = Post
    success_url = "/"
    form_class = PostForm
    template_name = 'blog_app/create_post.html'


def search_page(request):
    query = request.GET.get('q')
    posts = []
    if query:
        posts = Post.objects.filter(title__iregex=query, short_description__iregex=query,
                                    full_description__iregex=query)
    context = {
        'posts': posts,
        'query': query
    }
    return render(request, 'blog_app/search_page.html', context)


def add_vote(request, post_id, action):
    post = Post.objects.get(pk=post_id)
    if action == 'add_like':
        if request.user in post.likes.user.all():
            post.likes.user.remove(request.user.pk)
        else:
            post.likes.user.add(request.user.pk)
            post.dislikes.user.remove(request.user.pk)
    if action == 'add_dislike':
        if request.user in post.dislikes.user.all():
            post.dislikes.user.remove(request.user.pk)
        else:
            post.dislikes.user.add(request.user.pk)
            post.likes.user.remove(request.user.pk)

    return redirect('post', pk=post_id)
