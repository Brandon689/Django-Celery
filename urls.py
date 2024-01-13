from django.urls import include, path

urlpatterns = [
    path('celeryDJ/', include('celeryDJ.urls')),
]