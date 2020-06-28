from django.conf.urls import url
from your_diary_app import views

app_name='app'
urlpatterns=[
    url(r'^register/$',views.register,name="register"),
    url(r'^login/$',views.user_login,name="user_login"),
    url(r'^write/$',views.write,name="write"),
    url(r'^view/$',views.view,name="view"),
    url(r'^diary/$',views.diary,name='diary')
]
