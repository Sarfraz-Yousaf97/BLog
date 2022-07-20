from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from posts.views import blog, index, post , search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('blog/',blog , name= "post_list"),
    path('search/',search , name= "search"),
    path('post/<id>/',post , name= "post_detail"), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)