from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import pickle
import pandas as pd
import pickle
global scaler
import warnings
warnings.filterwarnings('ignore')
from django.core.mail import send_mail
from django.conf import settings



def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def getPredictions(a,b,c,d,e,f,g,h,i,j,k):
    model = pickle.load(open('DT.pkl', 'rb'))
    new_data = {
                'protocol_type': a,
                'service': b,
                'flag': c,
                'src_bytes': d,
                'is_host_login': e,
                'is_guest_login': f,
                'count': g,
                'srv_count': h,
                'rerror_rate': i,
                'srv_rerror_rate': j,
                'same_srv_rate': k
            }
    new_df = pd.DataFrame([new_data])
    prediction = model.predict(new_df)
    return prediction[0]

# def result(request):
#     a = str(request.GET['protocol_type'])
#     b = str(request.GET['service'])
#     c = str(request.GET['flag'])
#     d = int(request.GET['src_bytes'])
#     e = str(request.GET['is_host_login'])
#     f = str(request.GET['is_guest_login'])
#     g = str(request.GET['count'])
#     h = str(request.GET['srv_count'])
#     i = int(request.GET['rerror_rate'])
#     j = str(request.GET['srv_rerror_rate'])
#     k = str(request.GET['same_srv_rate'])
    
#     prediction = getPredictions(a,b,c,d,e,f,g,h,i,j,k)

#     return render(request, 'result.html', {'prediction': prediction})

def result(request):
    a = str(request.GET['protocol_type'])
    b = str(request.GET['service'])
    c = str(request.GET['flag'])
    d = int(request.GET['src_bytes'])
    e = str(request.GET['is_host_login'])
    f = str(request.GET['is_guest_login'])
    g = str(request.GET['count'])
    h = str(request.GET['srv_count'])
    i = int(request.GET['rerror_rate'])
    j = str(request.GET['srv_rerror_rate'])
    k = str(request.GET['same_srv_rate'])
    
    prediction = getPredictions(a, b, c, d, e, f, g, h, i, j, k)

    # If anomaly is detected (assuming 'anomaly' is represented as 1)
    if prediction == "anomaly":
        subject = "Anomaly Detected Alert"
        message = f"""
        An anomaly was detected in the system with the following details:
        Protocol Type: {a}
        Service: {b}
        Flag: {c}
        Src Bytes: {d}
        Host Login: {e}
        Guest Login: {f}
        Count: {g}
        Srv Count: {h}
        Rerror Rate: {i}
        Srv Rerror Rate: {j}
        Same Srv Rate: {k}
        """
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['naveenvaliant007@gmail.com']  # Replace with actual recipient
        send_mail(subject, message, from_email, recipient_list)

    return render(request, 'result.html', {'prediction': prediction})