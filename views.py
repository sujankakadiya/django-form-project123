from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def Home(request):
#     data = {
#         'title': 'Sujan',
#         'msg': 'SUJAN BHAI MAJAMA AAVDI GYU BADHU KE NAY ',
#         'color': 'red',
#         'btn_color': 'green',
#     'padding': '10px 20px',
#     'border': '5px',
#     'text_color': 'white',
#     'btn_text': 'Click me',
#     ###loop mate 
    
#     'clist': [ 'php','java','Django','rust','go'],
#     'student_details': [
#         {'number':'1','name':'sujan','mo_number':'1234567888'},
#         {'number':'2','name':'kri','mo_number':'1234567888'},  
        
        
#  ],
    
     
#          'numbers':[1,2,3,4,5,6,7],
#         'num': 6,
#         'dat' : {'user': 'sujan'},
   
# }
    
    
    
    
    
    return render (request,"index.html")

def aboutUs(request):
 
    
    return HttpResponse("<b>Welcome to sujan</b>")

def course(request):
    return HttpResponse("Welcome to company ")

def courseDetails(request,courseId):   ### daynamic mate nu chhe
    return HttpResponse(courseId)


def courseDeeps(request,coursename):    ### daynamic mate nu chhe koi bhi string 
    return HttpResponse(coursename)


def slugs(request,myslugs):              ### daynamic mate nu chhe  --- aave 
    return HttpResponse(myslugs)

# def userFrom(request):
#     total=0
#     try:
#         n1=int(request.POST['num1'])
#         n2=int(request.POST['num2'])
#         total=n1+n2
#     except:
#         pass

#     return render(request,"from.html",{'output':total})








# from django.shortcuts import render

# def From(request):
#     name = ""
#     age = ""

#     # POST method થી data લેશું
#     if request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")

#     data = {
#         'name': name,
#         'age': age
#     }

#     return render(request, "from.html", data)



# from django.shortcuts import render

# def Form(request):
    # # 1️⃣ initial values (empty)
    # name = ""
    # email = ""
    # phone = ""
    # gender = ""
    # dob = ""
    # course = ""
    # address = ""

    # 2️⃣ GET method થી data લઈએ
    # if request.method == "GET":
    #     name = request.GET.get("name","")
    #     email = request.GET.get("email","")
    #     phone = request.GET.get("phone","")
    #     gender = request.GET.get("gender","")
    #     dob = request.GET.get("dob","")
    #     course = request.GET.get("course","")
    #     address = request.GET.get("address","")

    # 3️⃣ dictionary બનાવી
    # data = {
    #     # 'name': name,
    #     # 'email': email,
    #     # 'phone': phone,
    #     # 'gender': gender,
    #     # 'dob': dob,
    #     # 'course': course,
    #     # 'address': address
    # }

    # return render(request, "form.html", {
    #     'name': name,
    #     'email': email,
    #     'phone': phone,
    #     'gender': gender,
    #     'dob': dob,
    #     'course': course,
    #     'address': address
        
        
        
        
        
        
        
        
        
        
        
        
        

# def Form(request):
#     # GET data with default empty values
#     name = request.GET.get("name", "")
#     email = request.GET.get("email", "")
#     phone = request.GET.get("phone", "")
#     gender = request.GET.get("gender", "")
#     dob = request.GET.get("dob", "")
#     course = request.GET.get("course", "")
#     address = request.GET.get("address", "")

#     data = {
#         'name': name,
#         'email': email,
#         'phone': phone,
#         'gender': gender,
#         'dob': dob,
#         'course': course,
#         'address': address
#     }

#     return render(request, "form.html", data)









# from django.shortcuts import render

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
