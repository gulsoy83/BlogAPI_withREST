from django.urls import path
from api_basic.user_api import views
#from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import RedirectView

#app_name='user_api'
urlpatterns = [
    path('',RedirectView.as_view(url='list/')),

    path('list/', views.UserList.as_view(), name='users'),
    path('list/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    
]
#urlpatterns = format_suffix_patterns(urlpatterns)