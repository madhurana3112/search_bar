from django.shortcuts import render, redirect
from authentication_app.models import *
from django.contrib.auth import login, logout
from helper import send_otp, generate_otp
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

from django.db import connection
import chardet
from django.db import connection

def data_dump(request):
    # Path to your SQL file
    sql_file_path = '/home/madhurana/Documents/search bar/search_bar/world-4.sql'

    # Read the SQL file
    with open(sql_file_path, 'r') as sql_file:
        sql_statements = sql_file.read()

    # Split SQL statements into individual statements
    statements = sql_statements.split(';')

    # Execute each SQL statement
    with connection.cursor() as cursor:
        for statement in statements:
            # Skip empty statements
            if statement.strip():
                cursor.execute(statement)

    return render(request, "signup.html")




    
        

def signup(request):
    user=CustomUser.objects.all()
    print(len(user))
    if request.method == "POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        gender=request.POST["gender"]
        email=request.POST["email"]
        phone_no=request.POST["phone_no"]
        user=CustomUser.objects.create_user(first_name=first_name, last_name=last_name,
                                       gender=gender, email=email, phone_number=phone_no)
        user.save()
        return render(request,"login.html")
    return render(request,"signup.html")


    
def signin(request):
    
    if request.method == "POST":
        email = request.POST["email"]
        
        otp = generate_otp()
        user = CustomUser.objects.get(email=email)
        send_otp(user, otp)

        request.session['email'] = {
            'email': email,
            'otp': otp,
        }

        messages.success(request, "OTP sent to email, please check")
        return render(request, "verify_otp.html", {"email": email})

    return render(request, "login.html")

def verify_otp(request):
    if request.method == "POST":
        otp = int(request.POST["otp"])
        email = request.POST["email"]
        email_session = request.session.get("email")
        if email_session['otp'] == otp and email_session['email'] == email:
            user = CustomUser.objects.get(email=email)
            login(request, user)
            return render(request, "dashboard.html")
        else:
            messages.error(request, "Invalid OTP")

    return redirect("search")

def logout_view(request):
    logout(request)
    return redirect('signin')
        

# def avc(request):
#     code="a"
#     name="aaaaa"
#     continent="Europe"
#     region="region"
#     surface_area=11
#     indep_year=11
#     population=11
#     life_expectancy=12.2
#     gnp=11.1
#     gnpold=11.1
#     local_name="aaaa"
#     government_form="aaaa"
#     head_of_state="aaaaa"
#     capital=11
#     code2="aaaaa"
# Country.objects.create(code=code,name=name,continent=continent,region=region,surface_area=surface_area,indep_year=indep_year,population=population,life_expectancy=life_expectancy,gnp=gnp,gnpold=gnpold,local_name=local_name,government_form=government_form,head_of_state=head_of_state,capital=capital,code2=code2    )

def search(request):
    query = request.GET.get('q', '')
    results = Country.objects.filter(name__icontains=query)[:3]
    city_names = City.objects.filter(name__icontains=query)[:3]
    languages = CountryLanguage.objects.filter(Language__icontains=query)[:3]
    
    data = []

    for result in results:
        data.append({'name': result.name, 'type': 'Country'})
    
    for city_name in city_names:
        data.append({'name': city_name.name, 'type': 'City'})

    for language in languages:
        data.append({'name': language.Language, 'type': 'Language'})

    return JsonResponse(data, safe=False)

def search_page(request):
    return render(request, 'dashboard.html')

def descriptionView(request):
    if request.method == "POST":
        search_text = request.POST.get("search", "")
        countries = Country.objects.filter(name__icontains=search_text)
        cities = City.objects.filter(name__icontains=search_text)
        languages = CountryLanguage.objects.filter(Language__icontains=search_text)
        description = {
            "countries": countries,
            "cities": cities,
            "languages": languages
        }
        return render(request, "searched_text.html", {"description": description})
    return render(request, "dashboard.html")

def country_details(request,code):
    country=Country.objects.get(code=code)
    return render(request, "country_details.html",{"country_details":country})
    