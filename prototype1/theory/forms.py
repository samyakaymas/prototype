from django.forms import ModelForm
from django import forms
from .models import *

TARGET_EXAM=[
    ("IIT","IIT"),
    ("NEET","NEET")
]

class TheoryForm(ModelForm):

    class Meta:
        model= Theory
        exclude=['prerequisites','twinConcepts']
    def __init__(self,chapter_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['theory'].widget=forms.HiddenInput()
        # self.fields['prerequisites'].widget=forms.HiddenInput()
        # self.fields['twinConcepts'].widget=forms.HiddenInput()
        # self.fields['easyExampleQues1'].widget=forms.HiddenInput()
        # self.fields['easyExampleSol1'].widget=forms.HiddenInput()
        # self.fields['easyExampleQues2'].widget=forms.HiddenInput()
        # self.fields['easyExampleSol2'].widget=forms.HiddenInput()
        # self.fields['easyExampleQues3'].widget=forms.HiddenInput()
        # self.fields['easyExampleSol3'].widget=forms.HiddenInput()
        # self.fields['easyExampleQues4'].widget=forms.HiddenInput()
        # self.fields['easyExampleSol4'].widget=forms.HiddenInput()
        # self.fields['easyExampleQues5'].widget=forms.HiddenInput()
        # self.fields['easyExampleSol5'].widget=forms.HiddenInput()
        
        # self.fields['mediumExampleQues1'].widget=forms.HiddenInput()
        # self.fields['mediumExampleSol1'].widget=forms.HiddenInput()
        # self.fields['mediumExampleQues2'].widget=forms.HiddenInput()
        # self.fields['mediumExampleSol2'].widget=forms.HiddenInput()
        # self.fields['mediumExampleQues3'].widget=forms.HiddenInput()
        # self.fields['mediumExampleSol3'].widget=forms.HiddenInput()
        # self.fields['mediumExampleQues4'].widget=forms.HiddenInput()
        # self.fields['mediumExampleSol4'].widget=forms.HiddenInput()
        # self.fields['mediumExampleQues5'].widget=forms.HiddenInput()
        # self.fields['mediumExampleSol5'].widget=forms.HiddenInput()
        
        # self.fields['hardExampleQues1'].widget=forms.HiddenInput()
        # self.fields['hardExampleSol1'].widget=forms.HiddenInput()
        # self.fields['hardExampleQues2'].widget=forms.HiddenInput()
        # self.fields['hardExampleSol2'].widget=forms.HiddenInput()
        # self.fields['hardExampleQues3'].widget=forms.HiddenInput()
        # self.fields['hardExampleSol3'].widget=forms.HiddenInput()
        # self.fields['hardExampleQues4'].widget=forms.HiddenInput()
        # self.fields['hardExampleSol4'].widget=forms.HiddenInput()
        # self.fields['hardExampleQues5'].widget=forms.HiddenInput()
        # self.fields['hardExampleSol5'].widget=forms.HiddenInput()
        # self.fields['summary'].widget=forms.HiddenInput()
        # self.fields['mnemonics'].widget=forms.HiddenInput()
        # self.fields['wowTheory'].widget=forms.HiddenInput()
        # self.fields['wowQues'].widget=forms.HiddenInput()
        # self.fields['wowReason'].widget=forms.HiddenInput()

        self.fields['difficulty']=forms.IntegerField(widget=forms.Select(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)]))
        self.fields['importance']=forms.IntegerField(widget=forms.Select(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)]))
        self.fields['duration']=forms.IntegerField(widget=forms.Select(choices=[(15,15),(30,30),(45,45),(60,60),(75,75),(90,90)]))
        self.fields['subConcept'].queryset = SubConcept.objects.none()
        self.fields['targetExam']=forms.CharField(widget=forms.Select(choices=TARGET_EXAM))
        self.fields['concept'].queryset=Concept.objects.filter(chapter=Chapter.objects.get(pk=chapter_id))
        if 'concept' in self.data:
            try:
                concept_id = int(self.data.get('concept'))
                self.fields['subConcept'].queryset = SubConcept.objects.filter(concept=Concept.objects.get(pk=concept_id)).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset