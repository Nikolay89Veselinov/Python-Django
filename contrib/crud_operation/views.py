from django.shortcuts import render, get_object_or_404, redirect

from .models import News
from .forms import NewsForm, InstanceForm

def news_list_view(request):
    news = News.objects.all()

    context = {
        'news': news,
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