from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from fabstar_app import views  # Import the views here
from django.views.generic.base import RedirectView


# urlpatterns = [
#     path('', include('django.contrib.auth.urls')),

#     path('admin/', admin.site.urls),
#     # path('', RedirectView.as_view(url='/accounts/login/'), name='redirect_to_login'),  # Redirect root URL
#     path('login/', views.login_view, name='login'),

#     path('accounts/password_change/', views.change_password, name='password_change'),  # Add this line to override the default
#     path('accounts/', include('django.contrib.auth.urls')), 
# ]


urlpatterns = [
#    path('', RedirectView.as_view(url='/accounts/login/?next=/'), name='redirect_to_login'),

    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('fabstar_app.urls')),
    path('accounts/password_change/', views.change_password, name='password_change'),  # Add this line to override the default
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

