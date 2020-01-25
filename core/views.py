from django.shortcuts import render, redirect
from datetime import datetime
import random
from core.forms import ContactUsForm
from core.models import Feedback, Subject, Author


# Create your views here.

def landing_page_view(request):
    # massage = request.GET.get('message')

    return render(request, 'landing_page.html', context={'name': 'andrii', 'now': datetime.now()})

def info_about_me(request):
    return render(request, 'about_me.html', context={'name': 'andrii', 'date_born': '08.01.1991', 'language': 'uk', 'city': 'rivne'})


def contact_us_view(request):
    LAST_MESSAGE = 'no message'
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print('okey')
            LAST_MESSAGE = request.POST.get('message')
            
            feedback = Feedback.objects.create(
                name=request.POST['name'], 
                text=LAST_MESSAGE
                )
            response = redirect('feedbacks')
            response['location'] += '?from=contact_us'
            return response
    else:
        form = ContactUsForm()

    return render(request, 'contact_us.html', context={'form': form, 'message': LAST_MESSAGE})


def feedbacks(request):
    has_contacted = bool(request.GET.get('from'))
    feedbacks = Feedback.objects.filter(is_active=True)
    return render(request, 'feedbacks.html', context={'feedbacks': feedbacks, 'has_contacted': has_contacted})


def subjects_page(request):
    author_name = request.GET.get('author')
    if author_name:
        author_obj = Author.objects.filter(name=author_name).first()
        subjects = Subject.objects.filter(is_active=True, author=author_obj)
    else:
        subjects = Subject.objects.filter(is_active=True)
    return render(request, 'subjects.html', context={'subjects': subjects})    


def subject_item_view(request, subject_name):
    subject_item = Subject.objects.filter(bot_name=subject_name, is_active=True).first()
    return render(request, 'bot.html', context={'bot': subject_item})
