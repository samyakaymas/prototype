from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class Chapter(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject,related_name="chapters",on_delete=models.CASCADE)
    class Meta:
        unique_together=('name','subject')
    def __str__(self):
        return self.name

class Concept(models.Model):
    name = models.CharField(max_length=100)
    chapter = models.ForeignKey(Chapter,related_name="concepts",on_delete=models.CASCADE)
    class Meta:
        unique_together=('name','chapter')
    def __str__(self):
        return self.name

class SubConcept(models.Model):
    name = models.CharField(max_length=100)
    concept = models.ForeignKey(Concept,related_name="subConcepts",on_delete=models.CASCADE)
    class Meta:
        unique_together=('name','concept')
    def __str__(self):
        return self.name



class Theory(models.Model):
    
    concept=models.ForeignKey(Concept,related_name="Theory",on_delete=models.CASCADE)
    subConcept=models.ForeignKey(SubConcept,related_name="Theory",on_delete=models.CASCADE)
    
    theory = models.TextField(null=False)
    easyExampleQues1=models.TextField(null=False)
    easyExampleQues2=models.TextField(null=False)
    easyExampleQues3=models.TextField(null=False)
    easyExampleQues4=models.TextField(null=False)
    easyExampleQues5=models.TextField(null=False)

    easyExampleSol1=models.TextField(null=False)
    easyExampleSol2=models.TextField(null=False)
    easyExampleSol3=models.TextField(null=False)
    easyExampleSol4=models.TextField(null=False)
    easyExampleSol5=models.TextField(null=False)
    
    mediumExampleQues1=models.TextField(null=False)
    mediumExampleQues2=models.TextField(null=False)
    mediumExampleQues3=models.TextField(null=False)
    mediumExampleQues4=models.TextField(null=False)
    mediumExampleQues5=models.TextField(null=False)

    mediumExampleSol1=models.TextField(null=False)
    mediumExampleSol2=models.TextField(null=False)
    mediumExampleSol3=models.TextField(null=False)
    mediumExampleSol4=models.TextField(null=False)
    mediumExampleSol5=models.TextField(null=False)
    
    hardExampleQues1=models.TextField(null=False)
    hardExampleQues2=models.TextField(null=False)
    hardExampleQues3=models.TextField(null=False)
    hardExampleQues4=models.TextField(null=False)
    hardExampleQues5=models.TextField(null=False)

    hardExampleSol1=models.TextField(null=False)
    hardExampleSol2=models.TextField(null=False)
    hardExampleSol3=models.TextField(null=False)
    hardExampleSol4=models.TextField(null=False)
    hardExampleSol5=models.TextField(null=False)
    
    difficulty=models.IntegerField(null=False)
    importance=models.IntegerField(null=False)

    duration=models.IntegerField(null=False)
    prerequisites=models.ManyToManyField(SubConcept,related_name="prerequisiteOf")
    summary=models.TextField(null=False)
    mnemonics=models.TextField(null=True)
    twinConcepts=models.ManyToManyField(SubConcept,related_name="twinConceptOf")
    videoUrl=models.CharField(max_length=100,null=False,)
    targetExam=models.CharField(max_length=100,null=False,)
    
    wowTheory=models.TextField()
    wowQues=models.TextField()
    wowReason=models.TextField()

