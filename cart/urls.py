from django.contrib import admin
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path("unicorn/", include("django_unicorn.urls")),
]
