from django.urls import path
from . import views
from .views import (HomeListPosts,
                    Content,
                    base,
                    ProgrammingListView,
                    ProgrammingContent,
                    Hi_TechListView,
                    Hi_TechContent)


urlpatterns = [
    path('', HomeListPosts.as_view(), name='home_page'),
    path('base/', base, name='base_page'),
    path('post/<int:pk>/', Content.as_view(), name='post-detail'),
    path('programming/', ProgrammingListView.as_view(), name='programming_page'),
    path('programming_content/<int:pk>/', ProgrammingContent.as_view(), name='pro_content_page'),
    path('Hi-Tech/', Hi_TechListView.as_view(), name='hi_tech_page'),
    path('Hi_content/<int:pk>/', Hi_TechContent.as_view(), name='hi-tech-content-page'),
    path('about/', views.about, name='about_page')
]
