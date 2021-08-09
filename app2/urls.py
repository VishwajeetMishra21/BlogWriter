from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import BlogsViewSet
# admin : abhi , pass: abhi

router=routers.DefaultRouter()
router.register(r'blo',BlogsViewSet)


urlpatterns = [
   path('blo',include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('',views.index,name='index'),
   path('register',views.user_register,name='register'),
   path('login',views.user_login,name='login'),
   path('logout',views.logout,name='logout'),
   path('post_blog',views.post_blog,name='post_blog'),
   path('blog_detail/<int:id>',views.blog_detail,name='blog_detail'),
   path('delete/<int:id>',views.delete,name='delete'),
   path('edit/<int:id>',views.edit,name='edit'),
   path('blog_detail/login',views.user_login,name='login'),
   path('blog_detail/logout',views.logout,name='logout'),
   
]

