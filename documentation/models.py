from django.db import models

# Create your models here.


DOCUMENTATION_TYPE = (
    ('fondsdocumentaire', 'Fonds Documentaire'),
    ('cataloguebib', 'Catalogue Bibliothéque'),
)
        


class Documentation(models.Model):
    #fondsdocumentaire=models.CharField(max_length=100)
    #cataloguebib=models.CharField(max_length=100)
    documentation_type=models.CharField(max_length=25,choices=DOCUMENTATION_TYPE)


    


