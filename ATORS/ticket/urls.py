from .import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('bookTicket/', views.bookTicket, name="bookTicket"),
    path('myTicket/', views.myTicket, name="myTicket"),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('delete/<int:id>', views.deletefun, name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
