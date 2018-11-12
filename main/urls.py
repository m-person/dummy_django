from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from main import views

urlpatterns = [
                  url(r'^$', views.HomeView.as_view(), name='home'),
                  url(r'^article/$', views.ArticleList.as_view(), name='article_list'),
                  url(r'^article/(?P<slug>[-\w]+)/$', views.ArticleDetails.as_view(), name='article_details'),
                  url(r'^article/(?P<slug>[-\w]+)/delete$', views.ArticleDelete.as_view(), name='article_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
