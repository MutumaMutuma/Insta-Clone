from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.signup, name='signup'),
    url(r'^home/$',views.index,name='index'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^comment/', views.comment, name='comment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)