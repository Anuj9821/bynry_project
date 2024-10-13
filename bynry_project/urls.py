from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('gas/', include('user_req.urls')),  # Include URLs from the app (replace 'app_name' with your actual app name)
]
