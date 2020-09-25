from django.shortcuts import render

# Create your views here.
from requests.auth import HTTPBasicAuth
import requests

def index(request):
    return render(request, 'Login.html', {})

def api(request):

    # If this is POST request, then process the Form data
    if request.method == 'POST':
        userObj = {
            'username':'iqmalhaziq', 
            'password':'222d2cb18da63338',
        }
        # Sends POST data
        r = requests.post('http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/login', data = userObj, params=request.POST)
    else:
        r = request.get('http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/extendSession', params=request.GET)

    if r.status_code == 200:
        return HttpResponse('Yay, it worked')

    return HttpResponse('Could not save data')
