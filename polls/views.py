from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm,InsertForm,UpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from polls.models import RegistrationTable , TeamMatches
import datetime
import random
from datetime import date, timedelta
from django.contrib import messages
from django.core.paginator import Paginator








def Front_page(request):
    return render(request, "front.html")


def login_1(request):
    if request.user.is_authenticated:
        return HttpResponse('You Are already logged in')
    else:

        if request.method == 'POST':
            form = LoginForm(request.POST)

            if form.is_valid():



                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=username, password=password)
                                
                if user is not None:
                    
                    if user.is_active:
                        login(request, user)    
                        return redirect('/polls/schedule_listad')
                    else:
                        return HttpResponse('Your account is not active')
                        
                else:
                    return HttpResponse('The Account does not exist')
            else:
                form = LoginForm()
                return render(request, "logindr.html",{"form":form})
        else:
            form = LoginForm()
            return render(request, "logindr.html",{"form":form})

def logout_view(request):
    logout(request)
    return redirect('/polls/welcome')
    



def insert_Team(request):
    if request.method == 'POST':

        blog_form = InsertForm(request.POST)
        if blog_form.is_valid():

            teamname = blog_form.cleaned_data['TeamNameform'] 
            playername = blog_form.cleaned_data['PlayerNameform']
            coach_name = blog_form.cleaned_data['CoachNameform'] 
            manager_name = blog_form.cleaned_data['ManagerNameform'] 

                                       

            blog_object = RegistrationTable(TeamName = teamname , TeamMembers = playername , Coach = coach_name , Manager = manager_name)
            blog_object.save() # will save the data from the form to database
                
            return redirect('/polls/teamrg')
        

    else:
        team_count = RegistrationTable.objects.all().count()
        print(team_count)
        if team_count>=10:
            Schedule_maker()
            return redirect('/polls/schedule_list')
        else:

            blog_form = InsertForm(request.POST)
            
            return render(request, 'teamreg.html', {'form': blog_form})
        return HttpResponse ("Internal service error")


def Schedule_maker():
    startdate = date(2023, 8, 1)   
    enddate = date(2023, 8, 23)  
    delta = enddate - startdate
    reps = list(RegistrationTable.objects.all())  
    repsM = int(len(reps)/2)
    Req_col = []
    matches = []
    Req_col.append(reps[:repsM])
    Stelteam = reps[repsM:] 
    Stelteam.reverse() 
    Req_col.append(Stelteam)
    for i in range(0, 9):
        for j in range(0, 5):
            matches.append([Req_col[0][j], Req_col[1][j]])
        l_lim = Req_col[1][0]
        r_lim = Req_col[0][4]
        Req_col[0][4] = Req_col[0][3]
        Req_col[0][3] = Req_col[0][2]
        Req_col[0][2] = Req_col[0][1]
        Req_col[0][1] = l_lim
        Req_col[1][0] = Req_col[1][1]
        Req_col[1][1] = Req_col[1][2]
        Req_col[1][2] = Req_col[1][3]
        Req_col[1][3] = Req_col[1][4]
        Req_col[1][4] = r_lim

    sl_listers = []
    venue = ['Germany', 'France', 'Italy', 'Spain', 'Portugal']

    spar_lin = []
    day = datetime.date(2023, 8, 1)
    time = datetime.time(8)
    dt_sched = 1
    for match in matches:
        sl_listers.append([day, match, random.choice(venue)])
        match_instance = TeamMatches(
            date=day, team_a=match[0], team_b=match[1], venue=random.choice(venue), time=time)
        spar_lin.append(match_instance)
        time = datetime.time(16)
        if(dt_sched % 2 == 0):
            time = datetime.time(8)
            day += timedelta(days=1)
        dt_sched = dt_sched + 1

    TeamMatches.objects.bulk_create(spar_lin)
    return HttpResponse('done')



def schedulelist(request):


    client_details26 = TeamMatches.objects.all()

    paginator = Paginator(client_details26, 12)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    return render(request, "schlist.html",{"blogs":blogs})


def schedulelistadmin(request):
     client_details26 = TeamMatches.objects.all()
     paginator = Paginator(client_details26, 5)
     page = request.GET.get('page')
     blogs = paginator.get_page(page)

     return render(request, "schlistadmin.html",{"blogs":blogs})





def update_u(request,requested_blog_id):
    if request.method == 'POST':
        blog_form = UpdateForm(request.POST)
        if blog_form.is_valid():                        
            blog_details = TeamMatches.objects.get(id=requested_blog_id) # this will select datafrom database 
            blog_details.team_a_points = blog_form.cleaned_data['scoreAform']
            blog_details.team_b_points = blog_form.cleaned_data['scoreBform']
            
            blog_details.save()
            messages.success(request, 'updated successfully!',extra_tags='alert')                
            return redirect('/polls/schedule_listad')

    else:
        blog_form = UpdateForm()

        blog_details = TeamMatches.objects.get(id=requested_blog_id) # this will select datafrom database         

        return render(request, 'update.html', {'form': blog_form,'blog_id':requested_blog_id})


def squad(request):
     client_details26 = RegistrationTable.objects.all()
     return render(request, 'adminsquad.html' ,{"client_details26":client_details26})








