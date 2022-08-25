from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from django.contrib import messages

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

def loging(request):
    user_name = request.POST['user_name']
    password = request.POST['password']
    try:
        global member
        member = Members.objects.get(user_name=user_name)
        if password == member.password:
            return HttpResponseRedirect(reverse('loged_in'))
        else:
            messages.add_message(request, messages.ERROR, 'your username and password didnt match')
            return HttpResponseRedirect(reverse('login'))
    except:
        messages.add_message(request, messages.ERROR, 'please enter your username and password correctly')
        return HttpResponseRedirect(reverse('login'))

def loged_in(request):
    global member
    context = {
      'first_name' : member.first_name , 'last_name' : member.last_name, 'user_name' : member.user_name, 'password' : member.password, 'ssn': member.ssn, 'email' : member.email, 'phone' : member.phone, 'security_question' : member.security_question, 'answer' : member.answer
    }
    template = loader.get_template('loged_in.html')
    return HttpResponse(template.render(context,request))
