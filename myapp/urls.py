from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from myapp.middlewares.auth import auth_middleware

urlpatterns = [
    path('autoadmin/',admin.site.urls),
    path('', views.home, name='home.html'),
    
    path('home', views.home, name='home'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logout, name='logout'),
    path('aboutus', views.aboutus, name='aboutus'),
    
    path('mycart', views.mycart, name='mycart'),
    path('user_profile', auth_middleware(views.user_profile), name='user_profile'),
    #path('services', views.services, name='services'),
    #path('contect', views.contact, name='contect'),

    
    path('paymentsummary', auth_middleware(views.paymentsummary), name='paymentsummary'),
    path('check_out', auth_middleware(views.check_out), name='check_out'),
    path('regist', views.regist, name='regist'),
    path('searchpage', views.searchpage, name='searchpage')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


