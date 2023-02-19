from django.urls import path, re_path
from django.utils import archive

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('login/', login, name='login'),
    path('registeer/', register, name='register'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('cats/<str:category>', categories),
    re_path(r'archive/(?P<year>[0-9]{4})/', archive),
]