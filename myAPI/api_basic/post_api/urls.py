from django.urls import path
from api_basic.post_api import views
#from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import RedirectView

#app_name='post_api'
urlpatterns = [
    path('',RedirectView.as_view(url='list/')),

    path('list/', views.PostList.as_view(), name='posts'),
    path('list/<slug>/', views.PostDetail.as_view(), name='post-detail'),
    
    path('create/', views.PostCreate.as_view(), name='posts_create'),
    
    path('update/<slug>/', views.PostUpdate.as_view(), name='post_update'),
    path('delete/<slug>/', views.PostDestroy.as_view(), name='post_destroy'),
    
]
#urlpatterns = format_suffix_patterns(urlpatterns)
