from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  template = loader.get_template('choose.html')
  return HttpResponse(template.render({},request))

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({},request))

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  user_name = request.POST['user_name']
  password = request.POST['password']
  ssn = request.POST['ssn']
  email = request.POST['email']
  phone = request.POST['phone']
  security_question = request.POST['security_question']
  answer = request.POST['answer']
  member = Members(first_name = first_name, last_name = last_name, user_name = user_name, password = password, ssn = ssn, email = email, phone = phone, security_question = security_question, answer = answer)
  member.save()
  return HttpResponseRedirect(reverse('index'))
