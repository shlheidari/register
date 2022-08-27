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
        member = Members.objects.get(user_name=user_name)
        if password == member.password:
            global member_logedin
            member_logedin = member
            return HttpResponseRedirect(reverse('loged_in'))
        else:
            messages.add_message(request, messages.ERROR, 'your username and password didnt match')
            return HttpResponseRedirect(reverse('login'))
    except:
        messages.add_message(request, messages.ERROR, 'your username was not found, please sign up')
        return HttpResponseRedirect(reverse('login'))

def loged_in(request):
    global member_logedin
    context = {
      'first_name' : member_logedin.first_name , 'last_name' : member_logedin.last_name, 'user_name' : member_logedin.user_name, 'password' : member_logedin.password, 'ssn': member_logedin.ssn, 'email' : member_logedin.email, 'phone' : member_logedin.phone, 'security_question' : member_logedin.security_question, 'answer' : member_logedin.answer
    }
    template = loader.get_template('loged_in.html')
    return HttpResponse(template.render(context,request))

def forget(request):
    template = loader.get_template('forget.html')
    return HttpResponse(template.render({},request))

def check(request):
    ssn = request.POST['ssn']
    security_question = request.POST['security_question']
    answer = request.POST['answer']
    try:
        member = Members.objects.get(ssn=ssn)
        if security_question == member.security_question and answer == member.answer:
            global member_checked
            member_checked = member
            return HttpResponseRedirect(reverse('checked'))
        else:
            messages.add_message(request, messages.ERROR, 'your entries are not matched!')
            return HttpResponseRedirect(reverse('forget'))
    except:
        messages.add_message(request, messages.ERROR, 'your SSN was not found, please sign up')
        return HttpResponseRedirect(reverse('forget'))

def checked(request):
    global member_checked
    context = {
      'user_name' : member_checked.user_name
    }
    template = loader.get_template('checked.html')
    return HttpResponse(template.render(context,request))

def reset(request):
    global member_checked
    member_checked = member_checked
    password = request.POST['password']
    member_checked.password = password
    member_checked.save()
    return HttpResponseRedirect(reverse('login'))

def delete(request):
    global member_logedin
    member_logedin.delete()
    return HttpResponseRedirect(reverse('index'))

def change(request):
    filed = request.POST['filed']
    req = request.POST[filed]
    global member_logedin
    setattr(member_logedin,filed,req)
    return HttpResponseRedirect(reverse('loged_in'))
