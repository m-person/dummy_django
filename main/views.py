from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import DeleteView, TemplateView, UpdateView
from django.views.generic.edit import FormView

from .forms import ArticleForm
from .models import Article


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['settings'] = [(i, getattr(settings, i)) for i in dir(settings) if not i.startswith('_')]
        return ctx


class ArticleList(FormView):
    template_name = 'article_list.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    success_url = reverse_lazy('article_list')
    fields = ['title', 'body', 'image']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form invalid', form.errors.as_json())
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['articles'] = Article.objects.all().order_by('-updated')
        return ctx


class ArticleDetails(UpdateView):
    template_name = 'article_details.html'
    model = Article
    fields = ['title', 'body', 'image']
    success_url = reverse_lazy('article_list')


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
