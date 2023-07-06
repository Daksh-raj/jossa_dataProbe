from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns=[
    path("",views.index,name="index"),
    path("predictor",views.predictor,name="predictor"),
    path("questions",views.questions,name="questions")
]

