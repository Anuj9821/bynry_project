from django.urls import path
from . import views

urlpatterns = [
    # URL for submitting a new service request
    path('submit/', views.submit_service_request, name='submit_service_request'),
    
    # URL for viewing details of a specific service request (by ID)
    path('request/<int:pk>/', views.service_request_detail, name='service_request_detail'),
    
    # URL for tracking service request status (optional API for JSON response)
    path('request/<int:pk>/status/', views.track_service_request_status, name='track_service_request_status'),
    
    # URL for customer support to view all service requests
    path('requests/', views.list_service_requests, name='list_service_requests'),
    
    # URL for updating the status of a specific service request (by ID)
    path('request/<int:pk>/update/', views.update_service_request_status, name='update_service_request_status'),
]
