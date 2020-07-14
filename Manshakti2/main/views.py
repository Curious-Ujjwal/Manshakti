from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request):
	storyform = storyForm()
	allstorys=Story.objects.filter(admin_approved=True).order_by('-pub_date')
	return render(request, 'main/index.html', {'allstorys':allstorys, 'storyform' : storyform })

def share(request):
	if request.method=='POST':
		storyform = storyForm(request.POST)
		if storyform.is_valid():
			storyform.save()
			storyform = storyForm()
			allstorys=Story.objects.filter(admin_approved=True).order_by('-pub_date')
			return render(request, 'main/index.html', {'allstorys':allstorys, 'lookup':'Your story has been submitted successfully. You can see it in Shared Stories Section once it gets approved', 'storyform' : storyform})

		else:
			storyform = storyForm()
			allstorys=Story.objects.filter(admin_approved=True).order_by('-pub_date')
			return render(request, 'main/index.html', {'allstorys':allstorys, 'storyform' : storyform})

	else:
		storyform = storyForm()
		allstorys=Story.objects.filter(admin_approved=True).order_by('-pub_date')
		return render(request, 'main/index.html', {'allstorys':allstorys, 'storyform' : storyform})

def viewall(request):
	storyform = storyForm()
	all_storys=Story.objects.filter(admin_approved=True).order_by('-pub_date')
	return render(request, 'main/index.html', {'allstorys':allstorys, 'storyform' : storyform})