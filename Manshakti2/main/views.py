from django.shortcuts import render
from .models import *
from django.utils import timezone

# Create your views here.
def index(request):
	allstorys=Story.objects.filter(admin_approved=True).order_by('pub_date')
	return render(request, 'main/index.html', {'allstorys':allstorys,})

def share(request):
	if request.method=='POST':
		if request.POST['inbox'] and request.POST['city']:
			story1 = Story()
			story1.name=request.POST['name']
			story1.city=request.POST['city']
			story1.inbox=request.POST['inbox']
			story1.pub_date=datetime.timezone.now()
			story1.save()
			allstorys=Story.objects.filter(admin_approved=True).order_by('pub_date')
			return render(request, 'main/index.html', {'allstorys':allstorys, 'lookup':'Your story has been submitted successfully. You can see it in Shared Stories Section once it gets approved',})

		else:
			allstorys=Story.objects.filter(admin_approved=True).order_by('pub_date')
			return render(request, 'main/index.html', {'allstorys':allstorys, 'lookup':'It seems like you missed out one field'})

	else:
		allstorys=Story.objects.filter(admin_approved=True).order_by('pub_date')
		return render(request, 'main/index.html', {'allstorys':allstorys,})

def viewall(request):
	all_storys=Story.objects.filter(admin_approved=True).order_by('-pub_date')
	return render(request, 'main/index.html', {'allstorys':allstorys,})