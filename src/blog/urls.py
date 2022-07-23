from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from posts.views import blog, index, post, post_create,  post_update, search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('blog/',blog , name= "post_list"),
    path('search/',search , name= "search"),
    path('create/',post_create , name= "post_create"), 
    path('post/<id>/',post , name= "post_detail"), 
    path('post/<id>/update/',post_update, name= "post-update"), 
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('django.contrib.auth.urls') , name='accounts_login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)