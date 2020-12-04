from json import load
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import News
from .forms import NewsForm, InstanceForm, FilterForm
from contrib.decorators.decorators import group_required


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''
    return {
        'order': order,
        'text': text,
    }

def news_list_view(request):
    # import ipdb; ipdb.set_trace()
    params = extract_filter_values(request.GET)
    order_by = 'title' if params['order'] == FilterForm.ORDER_ASC else '-title'
    news = News.objects.filter(title__icontains=params['text']).order_by(order_by)
    # news = News.objects.all()
    for n in news:
        n.user_created = n.created_by_id == request.user.id
        # import ipdb; ipdb.set_trace()
        
    context = {
        'news': news,
        'filter_form': FilterForm(initial=params),
    }
    return render(request, 'news_list.html', context)

def news_view(request, id):
    news = get_object_or_404(News, id=id)

    context = {
        'news': news,
    }
    return render(request, 'news.html', context)

def news_delete_view(request, id):
    news = get_object_or_404(News, id=id)
    if request.method == 'POST':
        news.delete()
        return redirect('../../')

    context = {
        'news': news,
    }
    return render(request, 'delete_form.html', context)

# @login_required(login_url='login_user')
@login_required
def news_create_view(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = NewsForm()

    context = {
        'form': form,
    }
    return render(request, 'create_news.html', context)

@group_required(groups=['Regular User'])
def new_update_view(request, id):
    news = News.objects.get(pk=id)

    form = NewsForm(request.POST, request.FILES, instance=news)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = InstanceForm(instance=news)

    context = {
        'form': form,
    }
    return render(request, 'update_news.html', context)

def news_detail_view(request, id):
    news = get_object_or_404(News, id=id)
    context = {
        'news': news,
    }
    return render(request, 'detail_news.html', context)