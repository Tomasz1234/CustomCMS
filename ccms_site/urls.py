from django.urls import path
from . import views

app_name = 'ccms_site'

urlpatterns=[
    path('',views.framecontent,name="framecontent"),
    path('<slug:post>/',views.post_detail,name="post_detail"),
]