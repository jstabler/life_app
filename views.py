import time
from calendar import month_name
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.context_processors import csrf
from life.models import Event, EventForm, Categories, CategoriesForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

def login(request):
	if request.method != 'POST':
		raise HTTP404('Only POSTs are allowed')
	try:
		m = Member.objects.get(username=request.POST['username'])
		if m.password == request.POST['password']:
			request.session['member_id'] = m.id
			return HttpResponseRedirect('/life/?logged_in=yes')
	except Member.DoesNotExist:
		return HttpResponse('Your username and password did not match.')

def logout(request):
	logout(request)
	return HttpResponseRedirect('/life/')

def lifeEvent(request):
	title = Event.objects.order_by('-timestamp')

	return render_to_response('event.html', dict(title=title), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def add_event(request):
	if request.method == "POST":
			form = EventForm(request.POST, request.FILES)
			if form.is_valid():
				event = Event.objects.create(
					title=form.cleaned_data['title'],
					category=form.cleaned_data['category'],
					length=form.cleaned_data['length'],
					counter=form.cleaned_data['counter'],
					counterUnit=form.cleaned_data['counterUnit'],
					url=form.cleaned_data['url'],
					description=form.cleaned_data['description'],
					image=form.cleaned_data['image'],
					timestamp=form.cleaned_data['timestamp'],
					)
				return HttpResponseRedirect('/life/')
	else:
		form = EventForm()

	d = dict(form=form)
	d.update(csrf(request))
	return render_to_response('add_event.html', d, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def add_category(request):
	if request.method == "POST":
			form = CategoriesForm(request.POST)
			if form.is_valid():
				category = Categories.objects.create(
					title=form.cleaned_data['category'],
					)
				return HttpResponseRedirect('/add/')
	else:
		form = CategoriesForm()

	d = dict(form=form)
	d.update(csrf(request))
	return render_to_response('add_category.html', d, context_instance=RequestContext(request))