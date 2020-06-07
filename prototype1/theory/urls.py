from django.urls import path 
from . import views

urlpatterns=[
    path("add/",views.TheoryCreateView.as_view(),name="add"),
    path("ajax/load/subConcepts",views.loadSubConcepts,name="ajaxLoadSubConcepts")
]