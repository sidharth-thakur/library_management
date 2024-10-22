
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),              
    path('books/', include('bookmanagement.urls')),  
    path('borrowings/', include('borrowingmanagement.urls')), 
    path('reviews/', include('reviewsmanagement.urls',namespace='reviews')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)