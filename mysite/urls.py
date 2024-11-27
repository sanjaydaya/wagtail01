from django.conf import settings
from django.urls import include, path
from django.contrib import admin



from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

urlpatterns = [
    # Authentication URLs (Login, Signup, etc.)
    path("accounts/", include("allauth.urls")),  # Allauth URLs for authentication
    
    # Wagtail Admin URLs
    path("django-admin/", admin.site.urls),  # Django admin site
    path("admin/", include(wagtailadmin_urls)),  # Wagtail admin URLs
    
    # Wagtail Documents URLs
    path("documents/", include(wagtaildocs_urls)),  # Wagtail document library URLs
    
    # Search URLs
    path("search/", search_views.search, name="search"),  # Custom search view

    # Wagtail's page serving mechanism for all pages
    path("", include(wagtail_urls)),  # Wagtail URLs for rendering pages

    path('userinfo/', include('userinfo.urls')), 

    path('', include('blog.urls')), 

    path("__reload__/", include("django_browser_reload.urls")),

    path('lessons/', include('lessons.urls')),
 
   
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Static files URLs
    urlpatterns += staticfiles_urlpatterns()

    # Media files URLs
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
