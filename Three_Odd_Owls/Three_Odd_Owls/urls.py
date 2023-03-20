"""URL patterns for the entire project.

This variable maps URL paths to views. Each path is associated with a
corresponding view function that generates an HTTP response. The views
can be defined in any app included in the project's INSTALLED_APPS
setting.

The urlpatterns variable is automatically used by Django's URL routing
mechanism to resolve incoming HTTP requests to the appropriate view.

Includes patterns for the following apps:

- band: Contains views for the band's website.
- ourblog: Contains views for the blog section of the website.
- django.contrib.auth: Contains built-in authentication views.
- accounts: Contains views for user account management.

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('band.urls')),
    path('ourblog/', include('ourblog.urls')),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
