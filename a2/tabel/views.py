from django.http import HttpResponseRedirect, HttpResponse
from .models import daftartabel, Pekerjaan
from .forms import form1, form2, UserForm, UserProfileInfoForm
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    if request.method == 'POST':
        #print(request.POST['name'])
        current_name=request.POST['name']
        all_datas = daftartabel.objects.filter(pekerjaan_id=request.POST['name'])
    else:
        all_datas = daftartabel.objects.all()

    all_pekerjaan = Pekerjaan.objects.all()
    template = loader.get_template('tabel/index.html')
    if request.method == 'POST':
        context = {
            'all_datas' : all_datas,
            'all_pekerjaan' : all_pekerjaan,
            'current_name' : int(request.POST['name']),
            }
    else:
                context = {
                    'all_datas' : all_datas,
                    'all_pekerjaan' : all_pekerjaan,
                    }
    return HttpResponse(template.render(context, request))

@login_required
def special(request):
    return HttpResponse("You're logged in, Nice !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method =="POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'tabel/registration.html',
                            {'user_form':user_form,
                             'profile_form':profile_form,
                             'registered':registered})



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(user)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Login details supplied")
    else:
        return render(request,'tabel/login.html',{})


def formview(request):
    form = forms.form1()

    if request.method == 'POST':
        form= forms.form1(request.POST)
        if form.is_valid():
            print("Validation Complete")
            print("Name : "+form.cleaned_data['name'])
            print("E-mail : "+form.cleaned_data['email'])
            print("Text : "+form.cleaned_data['text'])



    return render(request,'tabel/formpage.html',{'form':form})
