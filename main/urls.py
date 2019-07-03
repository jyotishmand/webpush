from django.contrib import admin
from django.urls import path, include
from .views import home , send_push
from .import views
from django.views.generic import TemplateView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name ='home'),
                  path('send_push', send_push),
                  path('webpush/', include('webpush.urls')),
                  path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
