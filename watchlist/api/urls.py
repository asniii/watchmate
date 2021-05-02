from django.urls import path, include

from watchlist.api.views import WatchListAV, WatchListDetailAV, StreamPlatformListAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movies-detail'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream'),
]
