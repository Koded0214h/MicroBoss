from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('toolkits/', views.toolkit, name='toolkits'),
    path('toolkits/<int:id>/', views.toolkit_detail, name='toolkit'),
    path('waitlist/', views.waitlist, name='waitlist'),
    path('waitlist-finish/', views.waitlist_finish, name='waitlist-finish')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
