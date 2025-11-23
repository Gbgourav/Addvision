from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import GetInTouch

def index(request):
    return render(request, 'index.html', {'name': 'Gourav'})

@csrf_exempt
def get_in_touch(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        
        # Basic validation
        if not name or not email or not message:
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all required fields.'
            })
        
        # Save the form data
        try:
            contact = GetInTouch.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            return JsonResponse({
                'success': True,
                'message': 'Thank you for contacting us! We will get back to you soon.'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'An error occurred. Please try again.'
            })
    
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method.'
    })
