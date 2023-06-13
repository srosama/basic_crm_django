from django.shortcuts import render, redirect
from django.http import *
from django.views.generic import *
from .forms import SignUpForm , AddRecordForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Record
# Create your views here.

class Home(TemplateView):
    def get(self, request):
        return render(request, 'home.html')

class Singup(TemplateView):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'singup.html', {'form':form})   
     
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have Successfully Registerd!')
            return redirect('dashborad')
        else:
            messages.success(request, 'Invaild Input ReCheck',  extra_tags='danger')
            form = SignUpForm()
            return redirect('singup')

class Login(TemplateView):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST['username']
        psw = request.POST['password']
        #Autho
        user = authenticate(request, username=username, password=psw)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Sccuffule')
            return redirect('dashborad')
        else:
            messages.success(request, 'Invaild Email Or Password',  extra_tags='danger')
            return redirect('login')

class Logout(TemplateView):
    def get(self, request):
        logout(request)
        messages.success(request, "You Have Been Logged Out")
        return redirect('home')

class Dashborad(ListView):
    def get(self, request):
        if request.user.is_authenticated:
            records = Record.objects.all()
            return render(request, 'dashborad.html', {'record':records})
        else:
            messages.error(request, 'You Should To singup First, Or Login'.title(),  extra_tags='danger')
            return redirect('singup')

class DashboradR(TemplateView):
    def get(self, request, pk):
        if request.user.is_authenticated:
            cust_r = Record.objects.get(id=pk)
            return render(request, 'dashboardR.html', {'cust_r':cust_r})
        else:
            messages.error(request, 'You Should To singup First, Or Login'.title(),  extra_tags='danger')
            return redirect('singup')
        

class DeleteDashboradR(TemplateView):
    def get(self, request, pk):
        if request.user.is_authenticated:
            idFor = Record.objects.get(id=pk)
            delete_recored = Record.objects.get(id=pk)
            delete_recored.delete()
            messages.success(request, f'You have sccuffuley delete the customer info with name of {idFor.client_first_name}')
            return redirect('dashborad')
        else:
            messages.error(request, 'You Should To singup First, Or Login'.title(),  extra_tags='danger')
            return redirect('singup')
        
class AddDashboradR(TemplateView):
    def get(self, request):
        form = AddRecordForm(request.POST or None)
        return render(request, 'add.html', {'form':form})        
    def post(self, request) :
        form = AddRecordForm(request.POST or None)
        context = {
            'form':form
        }
        if request.user.is_authenticated:
            if form.is_valid():
                add_record = form.save()
                messages.success(request, f'You have sccuffuley Add New customer info'.title())
                return redirect('dashborad')
            return render(request, template_name='add.html',context=context)
        else:
            messages.error(request, 'You Should To singup First, Or Login'.title(),  extra_tags='danger')
            return redirect('singup')
        
class Update_dashboradR(TemplateView):

    def get(self, request, pk):
            current_record = Record.objects.get(id=pk)
            form = AddRecordForm(request.POST or None ,instance=current_record)
            context = {
                'form':form
            }
            return render(request, template_name='update.html',context=context )

    def post(self, request, pk):
        if request.user.is_authenticated:
            current_record = Record.objects.get(id=pk)
            form = AddRecordForm(request.POST or None ,instance=current_record)
            context = {
                'form':form
            }
            if form.is_valid():
                form.save()
                messages.success(request, f'Your Customer Info Have Been Updated'.title())
                return redirect('dashborad')


        else:
            messages.error(request, 'You Should To singup First, Or Login'.title(),  extra_tags='danger')
            return redirect('singup')