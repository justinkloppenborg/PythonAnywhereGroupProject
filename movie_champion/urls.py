from django.urls import path
# from django.contrib.auth.views import password_change as pwd_change, password_change_done as pwd_change_done,
# password_reset as reset, password_reset_done as reset_done, password_reset_confirm as reset_confirm,
# password_reset_complete as reset_complete
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url

app_name = 'movie_champion'
urlpatterns = [
    path('', views.home, name='home'),
    path('', views.movie_list, name='movie_list'),
    path('', views.cart, name='cart'),
    path('movie_list', views.movie_list, name='movie_list'),
    path('', views.customer_list, name='customer_list'),
    path('customer_list', views.customer_list, name='customer_list'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^register/$', views.register, name='register'),
    # change password urls
    path('password_change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('crm:password_change_done')),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('crm:password_reset_done')),
         {'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('crm:password_reset_complete')),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
