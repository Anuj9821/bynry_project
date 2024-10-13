from django.db import models
from django.contrib.auth.models import User  # Assuming support reps are users

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('gas_leakage', 'Gas Leakage'),
        ('meter_malfunction', 'Meter Malfunction'),
        ('billing_issue', 'Billing Issue'),
        ('new_connection', 'New Connection'),
        ('disconnection', 'Disconnection'),
        ('maintenance', 'Maintenance'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('cancelled', 'Cancelled'),
    ]
    
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15, blank=True, null=True) 
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    
    # For request tracking and assignment to support staff
    support_rep = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='assigned_requests')

    def __str__(self):
        return f'{self.customer_name} - {self.service_type} - {self.status}'
