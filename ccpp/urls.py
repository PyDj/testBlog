#from django.conf.urls import url
#from . import views
#
#urlpatterns = [
#    url(r'', views.show)
#]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name="list_news"),
    path('single/<int:pk>', views.new_single, name="new_single"),
]
