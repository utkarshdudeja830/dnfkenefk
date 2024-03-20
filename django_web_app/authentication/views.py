import os
from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
import datetime
import json

def login_attempt(request):
    if request.method == 'POST':
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

        # Log the login attempt to the console or perform any additional actions
        
        # Render the index.html template

    return render(request, 'index.html')
