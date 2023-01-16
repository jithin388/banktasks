from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.contrib import  auth
from django.contrib import messages
from django.http import JsonResponse
from. models import Category
from .models import Gold
from .models import loan
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person, City
from .forms import PersonForm
from django.http import HttpResponseRedirect
# Create your views here.
def goldrate(request):
    gold_rate=Gold.objects.all()
    return render(request,"gold.html",{'gold':gold_rate})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password== password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username alredy exists")
                return redirect('register')
                
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email alredy exists")
                return redirect('register')
                
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                messages.info(request,"user created")
                return redirect(logon)
                
        else:
            messages.info(request,"password doesnot match")
            return redirect(register)
    return render(request,'register.html')
def logon(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"success fully logged in")
            return redirect('/add')
        else:
            messages.error(request,"invalid user")
            return redirect(logon)
    #messages.info(request,"sucessfully logged in")
        
    return render (request,'login.html')

def loandata(request):
    if request.method=='POST':
        loaner_name=request.POST['loanername']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        lgender=request.POST['l_gender']
        aadhar=request.POST['aadhar']
        adharimg=request.POST['aadhar_img']
        pan=request.POST['pan']
        panimg=request.POST['pan_img']
        loan_type=request.POST['loantype']
        amount=request.POST['loanamount']
        loan_data=loan.objects.create(name=loaner_name,email=email,phone=phone,address=address,gender=lgender,aadhar=aadhar,adhar_img=adharimg,pan=pan,pan_img=panimg,loan_type=loan_type,amount=amount)
        loan_data.save();
        if loan_type=="gold":
            messages.info(request,"data stored sucessfully")
            return redirect(goldrate)
        else:
            messages.info(request,"data stored sucessfully")
    return render(request,"loan.html")


def home(request):
    data=Category.objects.all()
    return render(request, "home.html",{'category':data})


def logout(request):
    auth.logout(request)
    return redirect('/')

def data (request) :
    user=request.POST.get("userget")
    results = Person.objects.filter(username=user).all()
    return render (request,"data.html",{'results': results})


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy ('home')
    template_name = "bankapp/person_form.html"
    def post(self,request, *args,**kwargs):
        form= self.get_form()
        if form.is_valid():
            super(PersonCreateView,self).form_valid(form)
            messages.success(request,"sucess fully loggedOut & data had stored !")
            return HttpResponseRedirect(self.get_success_url())
        self.object=None
        return self.form_invalid(form)
 
    


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')


def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'bankapp/city_dropdown_list_options.html', {'cities': cities})




