from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('', RedirectView.as_view(url='/accounts/login/'), name='redirect_to_login'),  # Redirect to login
#     path('home/', views.home, name='home'),
#     path('profile/', views.profile, name='profile'),
#     path('change-password/', views.change_password, name='change_password'),
#     path('password-changed/', views.password_changed, name='password_changed'),
#     path('aludecor-technical-manual/', views.aludecor_technical_manual, name='aludecor_technical_manual'),
#     path('aludecor-calculator/', views.aludecor_calculator, name='aludecor_calculator'),
#     path('aludecor-design-assist/', views.aludecor_design_assist, name='aludecor_design_assist'),
#     path('fabstar-app/', views.fabstar_app, name='fabstar_app'),
#     path('connect-with-dr_aludecor/', views.connect_with_dr_aludecor, name='connect_with_dr_aludecor'),
#     path('custom-logout/', views.custom_logout, name='custom_logout'),
# ]


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('password-changed/', views.password_changed, name='password_changed'),
    path('aludecor-technical-manual/', views.aludecor_technical_manual, name='aludecor_technical_manual'),
    path('aludecor-calculator/', views.aludecor_calculator, name='aludecor_calculator'),
    path('aludecor-design-assist/', views.aludecor_design_assist, name='aludecor_design_assist'),
    path('fabstar-app/', views.fabstar_app, name='fabstar_app'),
    path('connect-with-dr_aludecor/', views.connect_with_dr_aludecor, name='connect_with_dr_aludecor'),
    path('aludecor_flipbook/', views.aludecor_flipbook, name='aludecor_flipbook'),
    # path('custom-logout/', views.custom_logout, name='custom_logout'),
    path('custom_logout/', auth_views.LogoutView.as_view(), name='custom_logout'),
]
