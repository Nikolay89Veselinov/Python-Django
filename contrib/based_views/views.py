from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Article
from .forms import ArticleForm

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.filter(active=True)

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    form_class = ArticleForm
    # queryset = Article.objects.filter(active=True)


    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_, active=True)

    def get_success_url(self):
        return reverse('articles:article-list')


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.filter(active=True)


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    # queryset = Article.objects.filter(active=True)

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)