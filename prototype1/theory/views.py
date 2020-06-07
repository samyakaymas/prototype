from django.shortcuts import render, redirect , reverse
from django.http import HttpResponse
from django.views.generic import ListView,CreateView, UpdateView
from .models import *
from .forms import *
from django.apps import apps
User = apps.get_model('accounts', 'User')
# Create your views here.

class TheoryCreateView(CreateView):
    model=Theory
    form_class = TheoryForm
    def get_form_kwargs(self):
        kwargs = super(TheoryCreateView, self).get_form_kwargs()
        kwargs['chapter_id'] = User.objects.get(id=self.request.user.id).chapter
        return kwargs
    def form_invalid(self, form):
        return super().form_invalid(form)
    

def loadSubConcepts(request):
    conceptId = request.GET.get('concept')
    subConcepts=SubConcept.objects.filter(concept=Concept.objects.get(pk=conceptId))
    return render(request,"theory/sub_concept_dropdown_list.html",{'subConcepts':subConcepts})
