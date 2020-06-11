from django.shortcuts import render
from .models import User
from .forms import RegForm, LoginForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from home.models import Book, Person
from django.db.models.signals import post_save, class_prepared
from django.dispatch import receiver
from requests.exceptions import HTTPError
from django.contrib.auth import logout, authenticate, login

def add_friend(request, friend_id):
	if friend_id == request.user.id:# Ограничение чтобы пользователь не добавлял сам себя в друзья
		return redirect("/")
	to_me = get_object_or_404(User, id=friend_id)
	i_to = get_object_or_404(User, id=request.user.id).person
	print(1)
	i_to.friends.add(to_me)
	print(i_to.friends.all())
	i_to.save()
	return redirect(f'/cabinet/{friend_id}')

def unsubscribe(request, friend_id):
	pass

def reg(request):
	print(dir(request.user))
	message = ''
	form = RegForm(request.POST or None)
	if form.is_valid():
		form.save()
		cd = form.cleaned_data
		user = authenticate(username=cd['username'], password=cd['password1'])
		login(request, user)
		return redirect('/')
	else:
		try:
			errors = form.errors.as_data()
			messages = [i for i in errors]
			message = str(errors[messages[-1]])
			first = message.find("'") + 1
			second = message.rfind("'") - 1
			message = message[first:second]
		except:
			pass
	return render(request, 'cabinet/registration.html', {'user': request.user, 'message': message})

def log(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		cd = form.cleaned_data
		user = authenticate(username=cd['username'], password=cd['password'])
		if user is not None:
			login(request, user)
			request.user = 'renat'
			print(request.user, 22)
			return redirect('/')
	return render(request, 'cabinet/login.html', {'user': request.user, })#

def user_logout(request):
	logout(request)
	return redirect('/')
	
def cabinet(request, user_id):
	d = {}
	d['edit'] = False
	if user_id == request.user.id:
		d['edit'] = True
	d['human'] = get_object_or_404(User, id=user_id)
	d['written'] = Book.objects.filter(author_name_id=user_id)
	d['read'] = get_object_or_404(Person, user_id=user_id).read.all
	d["user"] = request.user
	a = d["human"].users.all()
	d['readers'] = a if len(a) < 7 else a[0:6]
	a = d["human"].person.friends.all()
	d['subscriptions'] = a if len(a) < 7 else a[0:6]
	d["in_friends"] = request.user in d["subscriptions"]
	return render(request, "cabinet/cabinet.html", d)

def bookcreate(request):
	human = get_object_or_404(Person, user_id=request.user.id)
	form = LoginForm(request.POST or None)
	if form.is_valid():
		cd = form.cleaned_data
	return render(request, "cabinet/book_create.html", {"form": LoginForm()})


@receiver(post_save, sender = User)
def add_person(instance, **kwargs):
	try:
		person = get_object_or_404(Person, user_id=instance.id) # Если не найдено намерено вызывается ошибка 404
	except:
		person = Person()
		person.user_id = instance.id
		person.save()


@receiver(post_save, sender=Book)
def add_book_1(instance, **kwargs):
	try:
		book = get_object_or_404(Book, id=instance.id)
		user = get_object_or_404(Person, user_id=1) #Защита от незареганных 
		user.read.add(book)
	except:
		pass