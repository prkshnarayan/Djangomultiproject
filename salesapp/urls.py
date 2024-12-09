from django.urls import path

from salesapp import views

from django.contrib.auth import views as auth_views

from django.urls import reverse_lazy


urlpatterns = [
    # path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('', views.home_fun, name='home'),
    path('add/', views.add_fun, name='add student'),
    path('display/', views.display_fun, name='display'),
    path('update/<int:id>', views.update_fun, name='update'),
    path('delete/<int:id>', views.delete_fun, name='delete'),
    path('logout/', views.logout_fun, name='logout'),
    path('display employee/', views.employee_fun, name='employee')
]


urlpatterns += [
    path('accounts/login/', auth_views.LoginView.as_view(next_page=reverse_lazy('login')), name="login"),
]
