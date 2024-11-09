from django.urls import path, include
from registroo.views import *

urlpatterns=[
    path("accounts/",include("django.contrib.auth.urls")),
    path("",Portada,"pagina_principal"),
    path("signup/",SignupView.as_view(),name="signup")
]