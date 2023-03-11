from django.urls import path, include



from app.views import IshchiView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', IshchiView.as_view(), name= 'Ishchi')
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)