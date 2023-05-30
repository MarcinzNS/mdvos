from django.urls import path
from main.views import login_system, profile, add_device
from main.views import index, categories, devices, error, favourite, like_devices

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
    path('device/<int:device_id>/like/', like_devices.add_like, name='add_like'),
    path('device/<int:device_id>/dislike/', like_devices.add_dislike, name='add_dislike'),
    path('device/<int:device_id>/like/remove/', like_devices.remove_like, name='remove_like'),
    path('device/<int:device_id>/dislike/remove/', like_devices.remove_dislike, name='remove_dislike'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
