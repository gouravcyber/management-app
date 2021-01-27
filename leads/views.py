from django.shortcuts import render, HttpResponse,redirect
from .models import Lead
from .forms import LeadForm

def lead_list(request):
    leads = Lead.objects.all()
    context={
        'leads': leads
    }
    return render(request, 'leads/lead_list.html', context)   

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead
    }
    return render(request, 'leads/lead_detail.html', context)  

def lead_create(request):
    if request.method=='POST':
        print(request.POST)
        return redirect('leads:lead_create')
    else:
        context = {
            'form': LeadForm()
        }
        return render(request, "leads/lead_create.html", context)