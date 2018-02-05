from django.conf.urls import include, url
from django.contrib import admin
from tabel import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^formpage/', views.formview, name='form1'),
    url(r'^tabel/', include('tabel.urls')),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^special/$',views.special,name='special'),
]
