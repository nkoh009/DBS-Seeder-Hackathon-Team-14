from django.shortcuts import render

# Create your views here.
from requests.auth import HTTPBasicAuth
import requests
import json
from.forms import LoginForm

def index(request):
    return render(request, 'Login.html')

def api(request):

    # If this is POST request, then process the Form data
    if request.method == 'POST':
        name = request.POST.get('uname')
        pwd = request.POST.get('psw')
        userObj = {
            'username': name, 
            'password': pwd,
        }

        # Sends POST data
        response = requests.post('http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/login', data = userObj, params=request.POST)
        response_dict = json.loads(response.text);
        for i in response_dict:
            print("key: ", i, "val: ", response_dict[i])
    else:
        response = request.get('http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/extendSession', params=request.GET)

    
    if response.status_code == 200:
        # process JWT token
        return HttpResponse('Authenticated!')

    elif response.status_code == 400:
        return HttpResponse('Bad Request. The request parameters are incorrect')

    else:
        return HttpResponse('Not found')
