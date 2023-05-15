from django.urls import path
from main.views import login_system, profile
from main.views import index, categories, devices

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index.home, name="home"),
    path('sign-in', login_system.loginUser, name="login"),
    path('sign-out', login_system.logoutUser, name="logout"),
    path('sign-up', login_system.registration, name="registration"),
    path('categories', categories.categories, name="categories"),
    path('devices', devices.devices, name="devices"),
    path('devices/<int:page>', devices.devices, name="devices"),
    path('one-device/<int:id>', devices.one_device, name="one_device"),
    path('profile', profile.profile, name="profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
