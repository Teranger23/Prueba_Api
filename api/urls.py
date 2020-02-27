from django.conf.urls import url
from api import views


urlpatterns = [
    url('', views.serie_list),
    url('/<int:pk>', views.serie_detail),
]