from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import ServiceRequest
from .forms import ServiceRequestForm  # Assuming you'll create a form for service requests
from django.utils import timezone

# View for submitting a new service request
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save()
            return redirect('service_request_detail', pk=service_request.pk)
    else:
        form = ServiceRequestForm()
    return render(request, 'user_req/create.html', {'form': form})

# View for tracking a specific service request by ID
def service_request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    return render(request, 'user_req/service_request_detail.html', {'service_request': service_request})

# API view for tracking service requests (optional JSON response for status tracking)
def track_service_request_status(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    response_data = {
        'customer_name': service_request.customer_name,
        'service_type': service_request.get_service_type_display(),
        'status': service_request.get_status_display(),
        'created_at': service_request.created_at,
        'updated_at': service_request.updated_at,
        'resolved_at': service_request.resolved_at,
    }
    return JsonResponse(response_data)

# View for customer support to see all service requests (optional, no login required)
def list_service_requests(request):
    service_requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'user_req/list_service_requests.html', {'service_requests': service_requests})

# View to update the status of a service request (for customer support use)
def update_service_request_status(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(ServiceRequest.STATUS_CHOICES):
            service_request.status = new_status
            if new_status == 'resolved':
                service_request.resolved_at = timezone.now()
            service_request.save()
            return redirect('service_request_detail', pk=service_request.pk)

    return render(request, 'update_service_request_status.html', {'service_request': service_request})
