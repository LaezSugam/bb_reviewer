from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from forms import UserForm
from models import User

# Create your views here.
def index(request):

	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			User.objects.add_user(form)
		else:
			print "Bad form, no valido!", form.errors
	else:
		form = UserForm()

	context = {
		"form": form,
		"users": User.objects.all(),
	}

	return render(request, "log_reg/index.html", context)

def register(request):



	return redirect("log_reg:index")
