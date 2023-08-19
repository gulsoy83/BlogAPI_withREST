from django.urls import path
from api_basic.comment_api import views
#from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import RedirectView

#app_name='comment_api'
urlpatterns = [
    path('',RedirectView.as_view(url='list/')),

    path('list/', views.CommentList.as_view()),
    path('list/<int:pk>/', views.CommentDetail.as_view(), name = 'comment-detail'),

    path('create/', views.CommentCreate.as_view(), name='comments_create'),
    
    path('update/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update'),
    path('delete/<int:pk>/', views.CommentDestroy.as_view(), name='comment_destroy'),
]
#urlpatterns = format_suffix_patterns(urlpatterns)