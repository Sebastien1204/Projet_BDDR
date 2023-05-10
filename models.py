from django.db import models
from django.contrib import admin
from sqlalchemy import ForeignKey
from django.template.defaultfilters import urlize

class Thematique(models.Model):
    thematique_id = models.AutoField(primary_key = True)
    nom = models.CharField(max_length = 100)
    class Meta : 
        managed = False
        db_table = 'thematique'

class Sous_thematique(models.Model):
    sous_thematique_id = models.AutoField(primary_key = True)
    thematique_id = models.IntegerField()
    nom = models.CharField(max_length = 100)
    class Meta :
        managed = False
        db_table = 'sous_thematique'

class Auteur(models.Model):
    auteur_id = models.AutoField(primary_key = True)
    article = models.ManyToManyField(Article, through="lien_auteur_article")
    titre = models.CharField(max_length = 10485760)
    nom = models.CharField(max_length = 10485760)
    prenom = models.CharField(max_length = 10485760)
    mail = models.CharField(max_length = 10485760)
    institution = models.CharField(max_length = 10485760)
    laboratoire = models.CharField(max_length = 10485760)
    class Meta :
        managed = False
        db_table = 'auteur'

class Article(models.Model):
    article_id = models.IntegerField(primary_key = True)
    auteur = models.ManyToManyField(Auteur, through="lien_auteur_article")
    titre = models.CharField(max_length = 10485760)
    date = models.CharField(max_length = 10485760)
    journal = models.CharField(max_length = 10485760)
    url = models.CharField(max_length = 10485760)
    thematique = models.CharField(max_length = 10485760)
    sous_thematique = models.CharField(max_length = 10485760)
    institution = models.CharField(max_length = 10485760)
    laboratoire = models.CharField(max_length = 10485760)

    def lien_url(self):
        return urlize(self.url)
    
    class Meta :
        managed = False
        db_table = 'article'

class Lien_auteur_article(models.Model):
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta :
        managed = False
        db_table = 'auteur'

class Journaux(models.Model):
    journal_id = models.IntegerField(primary_key = True)
    journal = models.CharField(max_length = 10485760)
    quantite = models.IntegerField()
    class Meta :
        managed = False
        db_table = 'journaux'

class Dates(models.Model):
    date_id = models.IntegerField(primary_key = True)
    date = models.CharField(max_length = 10485760)
    quantite = models.IntegerField()
    class Meta :
        managed = False
        db_table = 'dates'

class Laboratoires(models.Model):
    laboratoire_id = models.IntegerField(primary_key = True)
    laboratoire = models.CharField(max_length = 10485760)
    quantite = models.IntegerField()
    class Meta :
        managed = False
        db_table = 'laboratoires'

"""
class Lien_laboratoire_article(models.Model):
    laboratoire = models.ForeignKey(Laboratoire, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    class Meta :
        managed = False
        db_table = 'auteur'
"""
class Institutions(models.Model):
    institution_id = models.IntegerField(primary_key = True)
    institution = models.CharField(max_length = 10485760)
    quantite = models.IntegerField()
    class Meta :
        managed = False
        db_table = 'institutions'