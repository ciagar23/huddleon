from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^message/', include('message.urls', namespace="message")),
    url(r'^admin/', admin.site.urls),
]
