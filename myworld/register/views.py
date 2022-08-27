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
  user_name = request.POST['user_name']
  ssn = request.POST['ssn']
  email = request.POST['email']
  phone = request.POST['phone']
  check = 0
  for member in Members.objects.all():
      if member.user_name == user_name or member.ssn == ssn or member.email == email or member.phone == phone:
          check=1
  if(check == 0):
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      password = request.POST['password']
      security_question = request.POST['security_question']
      answer = request.POST['answer']
      member = Members(first_name = first_name, last_name = last_name, user_name = user_name, password = password, ssn = ssn, email = email, phone = phone, security_question = security_question, answer = answer)
      member.save()
      return HttpResponseRedirect(reverse('index'))
  else:
      messages.add_message(request, messages.ERROR, 'you have already signed up!')
      return HttpResponseRedirect(reverse('signup'))

def loging(request):
    user_name = request.POST['user_name']
    password = request.POST['password']
    try:
        member = Members.objects.get(user_name=user_name)
        if password == member.password:
            return HttpResponseRedirect(reverse('loged_in',args=[user_name]))
        else:
            messages.add_message(request, messages.ERROR, 'your username and password didnt match')
            return HttpResponseRedirect(reverse('login'))
    except:
        messages.add_message(request, messages.ERROR, 'your username was not found, please sign up')
        return HttpResponseRedirect(reverse('login'))

def loged_in(request,user_name):
    member = Members.objects.get(user_name=user_name)
    security_questions = ("In what city were you born?", "What is the name of your favorite pet?" ,"What is your mother's maiden name?", "What high school did you attend?", "What was the name of your elementary school?", "What was the make of your first car?", "What was your favorite food as a child?")
    security_question  = security_questions[int(member.security_question)-1]
    context = {
      'first_name' : member.first_name , 'last_name' : member.last_name, 'user_name' : member.user_name, 'password' : member.password, 'ssn': member.ssn, 'email' : member.email, 'phone' : member.phone, 'security_question' : security_question, 'answer' : member.answer
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
            return HttpResponseRedirect(reverse('checked',args=[member.user_name]))
        else:
            print(security_question , member.security_question , answer , member.answer)
            messages.add_message(request, messages.ERROR, 'your entries are not matched!')
            return HttpResponseRedirect(reverse('forget'))
    except:
        messages.add_message(request, messages.ERROR, 'your SSN was not found, please sign up')
        return HttpResponseRedirect(reverse('forget'))

def checked(request,user_name):
    context = {
      'user_name' : user_name
    }
    template = loader.get_template('checked.html')
    return HttpResponse(template.render(context,request))

def reset(request,user_name):
    member = Members.objects.get(user_name=user_name)
    password = request.POST['password']
    member.password = password
    member.save()
    return HttpResponseRedirect(reverse('login'))

def delete(request,user_name):
    member = Members.objects.get(user_name=user_name)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def change(request,user_name):
    filed = request.POST['filed']
    req = request.POST[filed]
    if filed == 'phone' or filed == 'email' or filed == 'ssn' or filed == 'user_name':
        check=0
        for member in Members.objects.all():
            attr = getattr(member,filed,None)
            if attr == req:
                check=1
        if(check == 0):
            member = Members.objects.get(user_name=user_name)
            setattr(member,filed,req)
            member.save()
            return HttpResponseRedirect(reverse('loged_in',args=[member.user_name]))
        else:
            messages.add_message(request, messages.ERROR, 'you have already signed up!')
            return HttpResponseRedirect(reverse('loged_in',args=[member.user_name]))
    else:
        member = Members.objects.get(user_name=user_name)
        setattr(member,filed,req)
        member.save()
        return HttpResponseRedirect(reverse('loged_in',args=[member.user_name]))
