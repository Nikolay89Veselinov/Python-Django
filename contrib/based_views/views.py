from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .models import Article
from .forms import ArticleForm

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    # form_class = ArticleForm
    # queryset = Article.objects.filter(active=True)
    model = Article
    fields = '__all__'
    success_url = reverse_lazy('articles:article-list')

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
    # model = Article
    # context_object_name = 'article'
    queryset = Article.objects.filter(active=True)
    paginate_by = 3

    # Here can get and filter queryset. This method execute after call class, before all methods
    def dispatch(self, request, *args, **kwargs):

        # Link for test: http://127.0.0.1:8000/en/based_views/?page=3&page_size=4
        if 'page_size' in request.GET:
            self.paginate_by = request.GET['page_size']
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_text'] = 'List Artiles'
        return context


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    # Overide context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = context['article']
        context['article_name'] = article.title
        return context

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    # queryset = Article.objects.filter(active=True)

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)
