from django.urls import path, include

from articles.views import ArticleDetailView, ArticleListView, TagListView, TagDetailView

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('articles/<str:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/', ArticleListView.as_view(), name='home'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<str:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('tinymce/',include('tinymce.urls')),
]
