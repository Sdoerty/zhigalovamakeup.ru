from copy import copy

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from broom_django import settings
from .models import MyImage, InstagramImage


def index(request):
    num_img = MyImage.objects.all()
    inst_img = InstagramImage.objects.all()

    if request.method == 'POST' and 'submit1' in request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        info = [name, phone, message]

        send_mail('ФОРМА Обратная связь',
                  str(info).strip('[]'),
                  settings.EMAIL_HOST_USER,
                  ['a.zhyhalova@gmail.com'],
                  fail_silently=False)

    if request.method == 'POST' and 'submit2' in request.POST:
        user = request.POST['user']
        telephone = request.POST['telephone']
        pre2 = 'Контакты для обратного звонка:  '
        info2 = [pre2, user, telephone]

        send_mail('ФОРМА Бесплатная консультация',
                  str(info2).strip('[]'),
                  settings.EMAIL_HOST_USER,
                  ['a.zhyhalova@gmail.com'],
                  fail_silently=False)

    return render(request, 'index.html', context={'num_img': num_img, 'inst_img': inst_img})




