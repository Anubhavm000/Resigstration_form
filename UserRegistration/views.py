from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.http import JsonResponse
from UserRegistration.send_mail import mail


# Create your views here.

def index(request):
    #return HttpResponse('<p> Hiiiiiiii </p>')
    return render(request, 'index.html')

def register(request):
     data ={}
     if request.method == "POST":
         print(request.POST)
         firstname = request.POST.get("first_name")
         classname = request.POST.get("classname")
         institution = request.POST.get("institution")
         phone1 = request.POST.get("phone1")
         email = request.POST.get("email")
         interest = request.POST.get("interest")
         workedearlier = request.POST.get("workedearlier")
         attended = request.POST.get("attended")
         training = request.POST.get("training")
         join = request.POST.get("join")
         try:
             user = User(firstname= firstname, classname= classname, institution = institution, phone1= phone1, email = email,interest = interest, workedearlier = workedearlier, attended = attended, training= training, join = join).save()
             data['firstname'] = firstname
             data['classname'] = classname
             data['institution'] = institution
             data['phone1'] = phone1
             data['email'] = email
             data['interest'] = interest
             data['workedearlier'] = workedearlier
             data['attended'] = attended
             data['training'] = training
             data['join'] = join
             data['status'] = 1
             mail(email, firstname)
         except Exception as e:
             print(e)
             data['status'] = 0
            #mail(firstname, email)
            #return HttpResponse(request, '<p> Data Save </p>')
     return JsonResponse(data, safe=False)


def delete(request):
    d={}
    id=request.GET.get("id")
    try:
        User.objects.filter(id=id).delete()
        d['status'] = 1
    except:
        d['status'] = 0
    return JsonResponse(d, safe=False)

def view(request):
    d={}
    user = User.objects.filter().values()
    d['user_data']=list(user)
    return JsonResponse(d, safe=False)




