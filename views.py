from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render



def aboutUs(request):
    return HttpResponse("<b>Welcome to sujan</b>")



def Form(request):
    name = request.POST.get("name")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")
    gender = request.POST.get("gender", "")
    dob = request.POST.get("dob", "")
    course = request.POST.get("course", "")
    address = request.POST.get("address", "")
    
    url="/aboutUs/?address1={}".format(address)

    
    return HttpResponseRedirect(url)

    return render(request, "form.html", {
        'name': name,
        'email': email,
        'phone': phone,
        'gender': gender,
        'dob': dob,
        'course': course,
        'address1': address
    })
