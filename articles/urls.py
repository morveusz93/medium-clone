from django.urls import path

from articles.views import ArticleDetailView, ArticlesListView

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('articles/<str:pk>/', ArticleDetailView.as_view(), name='article-details'),
    path('articles/', ArticlesListView.as_view(), name='home'),
]
