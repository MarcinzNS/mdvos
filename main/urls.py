from django.urls import path
from main.views import login_system, profile, add_device
from main.views import index, categories, devices, error, favourite

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index.home, name="home"),
    path('sign-in', login_system.loginUser, name="login"),
    path('sign-out', login_system.logoutUser, name="logout"),
    path('sign-up', login_system.registration, name="registration"),
    path('categories', categories.categories, name="categories"),
    path('add-device', add_device.add_device, name="add_device"),
    path('devices', devices.devices, name="devices"),
    path('devices/<int:page>', devices.devices, name="devices"),
    path('devices/<int:how_many_item_on_page>/<int:page>', devices.devices, name="devices"),
    path('devices/<str:category>', devices.devices, name="devices"),
    path('devices/<str:category>/<int:page>', devices.devices, name="devices"),
    path('devices/<str:category>/<int:how_many_item_on_page>/<int:page>', devices.devices, name="devices"),
    path('one-device/<int:id>', devices.one_device, name="one_device"),
    path('profile', profile.profile, name="profile"),
    path('error', error.error, name="error"),
    path('fav/<int:id>/', favourite.favourite_add, name="fav"),
    path('profile/favourites/', favourite.favourites_list, name='favourites_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
