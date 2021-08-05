"""proyecto_Residencia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.conf.urls.static import static
from aplicaciones.principal.views import inicio
from aplicaciones.principal.views import login
from aplicaciones.principal.views import register
from aplicaciones.principal.views import home
from aplicaciones.principal.views import dashboard
from aplicaciones.principal.views import leccion1_1, leccion1_1p2, leccion1_1p3, leccion1_2, leccion1_3, leccion1_3p2, leccion1_4, leccion1_4p2, leccion1_4p3, leccion1_5, leccion1_6
from aplicaciones.principal.views import leccion2_1, leccion2_1p2, leccion2_2, leccion2_2p2, leccion2_3, leccion2_4, leccion2_4p2, leccion2_5, leccion2_5p2
from aplicaciones.principal.views import leccionradios, leccion3_1, leccion3_1p2, leccion3_2, leccion3_2p2, leccion3_2p3, leccion3_2p4, leccion3_3, leccion3_3p2,leccion3_4, leccion3_4p2, leccion3_5, leccion3_5p2, leccion3_5p3
from aplicaciones.principal.views import ejercicio1
from aplicaciones.principal.views import evaluacion1, evaluacionEmail, enviarCorr
from aplicaciones.principal.views import examenUnidad1, examenUnidad2, examenUnidad3
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from proyecto_Residencia import settings

urlpatterns = [
    re_path('admin/', admin.site.urls),
    path('', inicio,name='index'),
    re_path('^[a-z]+/login/', login, name='login'),
    re_path('registro/', register, name='register'),
    path('home/', home, name='home'),
    path('leccion1_3/', leccion1_3, name='leccion1_3'),
    path('leccion1_3/leccion1_3p2/', leccion1_3p2, name='leccion1_3p2'),
    path('leccion1_1/', leccion1_1, name='leccion1_1'),
    path('leccion1_1/leccion1_1p2/', leccion1_1p2, name='leccion1_1p2'),
    re_path('leccion1_1/leccion1_1p2/leccion1_1p3/', leccion1_1p3, name='leccion1_1p3'),
    re_path('leccion1_2/', leccion1_2, name='leccion1_2'),
    path('leccion1_4/', leccion1_4, name='leccion1_4'),
    path('leccion1_4/leccion1_4p2/', leccion1_4p2, name='leccion1_4p2'),
    path('leccion1_4/leccion1_4p2/leccion1_4p3/', leccion1_4p3, name='leccion1_4p3'),
    re_path('leccion1_5/', leccion1_5, name='leccion1_5'),
    re_path('leccion1_6/', leccion1_6, name='leccion1_6'),
    path('leccion2_1/', leccion2_1, name='leccion2_1'),
    path('leccion2_1/leccion2_1p2/', leccion2_1p2, name='leccion2_1p2'),
    path('leccion2_2/', leccion2_2, name='leccion2_2'),
    path('leccion2_2/leccion2_2p2/', leccion2_2p2, name='leccion2_2p2'),
    path('leccion2_3/', leccion2_3, name='leccion2_3'),
    path('leccion2_4/', leccion2_4, name='leccion2_4'),
    path('leccion2_4/leccion2_4p2/', leccion2_4p2, name='leccion2_4p2'),
    path('leccion2_5/', leccion2_5, name='leccion2_5'),
    path('leccion2_5/leccion2_5p2/', leccion2_5p2, name='leccion2_5p2'),
    path('leccion3_1/', leccion3_1, name='leccion3_1'),
    path('leccion3_1/leccion3_1p2/', leccion3_1p2, name='leccion3_1p2'),
    path('leccion3_2/', leccion3_2, name='leccion3_2'),
    path('leccion3_2/leccion3_2p2/', leccion3_2p2, name='leccion3_2p2'),
    path('leccion3_2/leccion3_2p2/leccion3_2p3/', leccion3_2p3, name='leccion3_2p3'),
    path('leccion3_2/leccion3_2p2/leccion3_2p3/leccion3_2p4/', leccion3_2p4, name='leccion3_2p4'),
    path('leccion3_3/', leccion3_3, name='leccion3_3'),
    path('leccion3_3/leccion3_3p2/', leccion3_3p2, name='leccion3_3p2'),
    path('leccion3_4/', leccion3_4, name='leccion3_4'),
    path('leccion3_4/leccion3_4p2/', leccion3_4p2, name='leccion3_4p2'),
    path('leccion3_5/', leccion3_5, name='leccion3_5'),
    path('leccion3_5/leccion3_5p2/', leccion3_5p2, name='leccion3_5p2'),
    path('leccion3_5/leccion3_5p2/leccion3_5p3/', leccion3_5p3, name='leccion3_5p3'),
    path('leccionradios/', leccionradios, name='leccionradios'),
    path('ejercicio1/', ejercicio1, name='ejercicio1'),
    path('evaluacion1/', evaluacion1, name='evaluacion1'),
    path('evaluacionEmail/', enviarCorr, name='evaluacionEmail'),
    path('dashboard/', dashboard, name='dashboard'),
    path('examenUnidad1/', examenUnidad1, name='examenUnidad1'),
    path('examenUnidad2/', examenUnidad2, name='examenUnidad2'),
    path('examenUnidad3/', examenUnidad3, name='examenUnidad3'),

]

urlpatterns += staticfiles_urlpatterns()
