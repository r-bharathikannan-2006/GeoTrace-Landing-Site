from django.shortcuts import render

from core.models import Partnership

# Create your views here.
def index(request):
    return render(request, 'Home.html')

def partnership(request):
    if request.method == 'POST':
        # Handle form submission logic here
        org_name = request.POST.get('organizationName')
        org_type = request.POST.get('orgType')
        name = request.POST.get('contactName')
        email = request.POST.get('contactEmail')
        phone = request.POST.get('contactPhone')
        goal = request.POST.get('partnershipGoal')
        message = request.POST.get('description')
        record = Partnership.objects.filter(email=email).first()
        if record:
            # Update existing record
            record.org_name = org_name
            record.org_type = org_type
            record.name = name
            record.phone = phone
            record.message = message
            record.primary_goal = goal
            record.save()
        else:
            record = Partnership(
                org_name=org_name,
                org_type=org_type,
                name=name,
                email=email,
                phone=phone,
                primary_goal=goal,
                message=message
        )
        record.save()   
        return render(request, 'success.html')
    else:
        return render(request, 'partnership.html')

def demo(request):
    return render(request, 'demo.html')