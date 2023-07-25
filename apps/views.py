from django.shortcuts import render, redirect
from django.urls import reverse
from apps.forms import (UserModelForm, ServisModelForm,
                        UserUpdateForm, BlogModelForm,
                        AddSkillForm, CommentsForm,
                        PortfolioModelForm, ContactForm)
from apps.models import User, Service, Blog, Skill, Comment, Portfolio
from config.settings import TELEGRAM_BOT_TOKEN
from httpx import post, get


def send_message(chat_id, message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = get(url, params=params)
    print(response.text, response.status_code)


def index(request, pk):
    data = User.objects.filter(id=pk).first()
    servis = Service.objects.filter(user_id=pk).all()
    blog = Blog.objects.filter(user_id_id=pk).all()
    skill = Skill.objects.filter(user_id=pk).all()
    port = Portfolio.objects.filter(user_id_id=pk).all()
    return render(request, 'index.html', {'user': data, 'servis': servis, 'blog': blog, 'skill': skill, 'port': port})


def portfolio(request, pk):
    p = Portfolio.objects.filter(id=pk).first()
    data = User.objects.filter(id=p.user_id_id).first()
    return render(request, 'portfolio.html', {'user':data, 'port': p})


def blog(request, pk):
    bloga = Blog.objects.filter(id=pk).first()
    data = User.objects.filter(id=bloga.user_id_id).first()
    c_view = Comment.objects.filter(post_id__id=pk).all()
    if request.POST:
        comment = CommentsForm(request.POST)
        if comment.is_valid():
            comment.save()
        return redirect(reverse('blog', args=(bloga.pk, )))
    return render(request, 'blog.html', {'user':data, 'blog': bloga, 'c_view': c_view})


def sign_up(request):
    if request.POST:
        data = UserModelForm(request.POST, files=request.FILES)
        if data.is_valid():
            data.save()
        return redirect(reverse('login'))
    return render(request, 'signup.html')


def login(request):
    data = request.POST
    if request.POST:
        username = data.get('username')
        password = data.get('password')
        a = User.objects.filter(username=username, password=password).first()
        if a:
            return redirect(reverse('index', args=(a.pk, )))
    return render(request, 'login.html')


def updete_servis(request, pk):
    data = request.POST
    a = User.objects.filter(id=pk).first()
    if data:
        user_id = data.get('user_id')
        s = ServisModelForm(data)
        if s.is_valid():
            s.save()
        return redirect(reverse('index', args=(a.pk,)))
    return render(request, 'update_servis.html', {'user':a})


def updete_anketa(request, pk):
    a = User.objects.filter(id=pk).first()
    if request.POST:
        data = UserUpdateForm(request.POST, instance=a)
        if data.is_valid():
            data.save()
        return redirect(reverse('index', args=(a.pk,)))
    return render(request, 'update_anketa.html', {'user': a})


def updete_blog(request, pk):
    a = User.objects.filter(id=pk).first()
    if request.POST:
        data = BlogModelForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
        return redirect(reverse('index', args=(a.pk,)))
    return render(request, 'update_blog.html', {'user': a})


# @login_required
def updete_skill(request, pk):
    a = User.objects.filter(id=pk).first()
    if request.POST:
        data = AddSkillForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect(reverse('index', args=(a.pk, )))
    return render(request, 'update_skill.html', {'user': a})


def updete_portfolio(request, pk):
    a = User.objects.filter(id=pk).first()
    if request.POST:
        data = PortfolioModelForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            return redirect(reverse('index', args=(a.pk, )))
    return render(request, 'update_portfolio.html', {'user': a})


def contact_form(request, pk):
    data = request.POST
    a = User.objects.filter(id=pk).first()
    if data:
        form = ContactForm(data)
        if form.is_valid():
            data = form.cleaned_data
            m = f'''📥 New mail\n📩 From: {data['email']}\n👱 Name: {data['name']}\n📄 Message: {data['message']}'''
            send_message(1038185913, m)
        # return redirect(reverse(''))
    return render(request, 'index.html', {'user': a})
