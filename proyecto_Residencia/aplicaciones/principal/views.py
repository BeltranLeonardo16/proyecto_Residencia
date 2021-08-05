from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
# Create your views here.

def enviarCorr(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        asunto = request.POST.get('asunto')
        content = request.POST.get('content')
        send_mail(
            asunto,
            content,
            settings.EMAIL_HOST_USER,
            [to]
        )
        return render(
            request,
            'evaluacionEmail.html',
            {
                'title':'send an email'
            }
        )
    else:
        return render(
           request,
            'evaluacionEmail.html',
            {
                'title':'send an email'
            } 
        )


def inicio(request):
    return render(request,'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def leccion1_1(request):
    return render(request, 'leccion1_1.html')

def leccion1_1p2(request):
    return render(request, 'leccion1_1p2.html')

def leccion1_1p3(request):
    return render(request, 'leccion1_1p3.html')

def leccion1_2(request):
    return render(request, 'leccion1_2.html')

def leccion1_3(request):
    return render(request, 'leccion1_3.html')

def leccion1_3p2(request):
    return render(request, 'leccion1_3p2.html')

def leccion1_4(request):
    return render(request, 'leccion1_4.html')

def leccion1_4p2(request):
    return render(request, 'leccion1_4p2.html')

def leccion1_4p3(request):
    return render(request, 'leccion1_4p3.html')

def leccion1_5(request):
    return render(request, 'leccion1_5.html')

def leccion1_6(request):
    return render(request, 'leccion1_6.html')

def leccion2_1(request):
    return render(request, 'leccion2_1.html')

def leccion2_1p2(request):
    return render(request, 'leccion2_1p2.html')

def leccion2_2(request):
    return render(request, 'leccion2_2.html')

def leccion2_2p2(request):
    return render(request, 'leccion2_2p2.html')

def leccion2_3(request):
    return render(request, 'leccion2_3.html')

def leccion2_4(request):
    return render(request, 'leccion2_4.html')

def leccion2_4p2(request):
    return render(request, 'leccion2_4p2.html')

def leccion2_5(request):
    return render(request, 'leccion2_5.html')

def leccion2_5p2(request):
    return render(request, 'leccion2_5p2.html')

def leccion3_1(request):
    return render(request, 'leccion3_1.html')

def leccion3_1p2(request):
    return render(request, 'leccion3_1p2.html')

def leccion3_2(request):
    return render(request, 'leccion3_2.html')

def leccion3_2p2(request):
    return render(request, 'leccion3_2p2.html')

def leccion3_2p3(request):
    return render(request, 'leccion3_2p3.html')

def leccion3_2p4(request):
    return render(request, 'leccion3_2p4.html')

def leccion3_3(request):
    return render(request, 'leccion3_3.html')

def leccion3_3p2(request):
    return render(request, 'leccion3_3p2.html')

def leccion3_4(request):
    return render(request, 'leccion3_4.html')

def leccion3_4p2(request):
    return render(request, 'leccion3_4p2.html')

def leccion3_5(request):
    return render(request, 'leccion3_5.html')

def leccion3_5p2(request):
    return render(request, 'leccion3_5p2.html')

def leccion3_5p3(request):
    return render(request, 'leccion3_5p3.html')

def leccionradios(request):
    return render(request, 'leccionradios.html')

def ejercicio1(request):
    return render(request, 'ejercicio1.html')

def evaluacion1(request):
    return render(request, 'evaluacion1.html')

def evaluacionEmail(request):
    return render(request, 'evaluacionEmail.html')

def examenUnidad1(request):
    return render(request, 'examenUnidad1.html')

def examenUnidad2(request):
    return render(request, 'examenUnidad2.html')

def examenUnidad3(request):
    return render(request, 'examenUnidad3.html')