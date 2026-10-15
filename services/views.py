from django.shortcuts import redirect, render

from .forms import ServiceForm
from .models import Service

def service_list(request):
    services = Service.objects.all()

    return render(request, "services/service_list.html", {
        "services": services,
    })

def service_create(request):

    if request.method == "POST":
        form = ServiceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('services:service_list')
            
    else:
        form = ServiceForm()
        
    return render(
        request,
        'services/service_form.html',
        {"form": form}
    )