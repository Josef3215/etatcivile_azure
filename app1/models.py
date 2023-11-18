from django.db import models
import datetime



class Wilaya(models.Model):
    NomW = models.CharField(max_length=50, verbose_name="Wilaya ")
    CodePostalW = models.CharField(max_length=5, verbose_name="Code Postal")
    

    #def __unicode__(self):
     #   return self.libelle_wilaya
    class Meta:
        ordering = ['NomW']

    def __str__(self):
        return f"{self.NomW }"


class Daira(models.Model):
    NomD = models.CharField(max_length=50, verbose_name="Daira de Naissance")
    CodePostalD = models.CharField(max_length=5, verbose_name="Code Postal")
    Wilaya = models.ForeignKey(Wilaya, verbose_name='Wilaya', on_delete=models.CASCADE)

    #def __unicode__(self):
     #   return self.libelle_daira
    class Meta:
        ordering = ['NomD']

    def __str__(self):
        return f"{self.NomD}"

class Commune(models.Model):
    NomC= models.CharField(max_length=50, verbose_name="Commune de Naissance")
    CodePostalC = models.CharField(max_length=5, verbose_name="Code Postal")
    Daira = models.ForeignKey(Daira, verbose_name='Daira', on_delete=models.CASCADE)

    #def __unicode__(self):
     #   return self.libelle_commune
    class Meta:
        ordering = ['NomC']

    def __str__(self):
        return f"{self.NomC }"

class BuretatCivile(models.Model):
    libelle_betat = models.CharField(max_length=200, verbose_name="Bureau d'etat Civil")
    Commune = models.ForeignKey(Commune, verbose_name='Commune', on_delete=models.CASCADE)

    #def __unicode__(self):
        #   return self.libelle_betat
    class Meta:
        ordering = ['libelle_betat']

    def __str__(self):
        return f"{self.libelle_betat }"



class Persone(models.Model):

    Sexe = (
        ('Masculin', 'Masculin'),
        ('Feminin', 'Feminin'),
    )
    nom = models.CharField(max_length=250, verbose_name='Nom')
    prenoms = models.CharField(max_length=250, verbose_name='Prenoms')
    sexe = models.CharField(max_length=150, verbose_name='sexe', choices=Sexe)
    date_naiss = models.DateField(verbose_name='Date de Naissance')
    heure_naiss = models.TimeField(verbose_name='Heure de Naissance')
    pere = models.ForeignKey('self', verbose_name='Nom et Prénoms du Pere', on_delete=models.CASCADE, blank=True, null=True, related_name='peres')
    pere_pere = models.ForeignKey('self', verbose_name='Nom et Prénoms du Pere du Pere', on_delete=models.CASCADE, blank=True, null=True, related_name='peres_pere')
    mere = models.ForeignKey('self', verbose_name='Nom et Prénoms du Mere', on_delete=models.CASCADE, blank=True, null=True, related_name='meres')
    pere_mere = models.ForeignKey('self', verbose_name='Nom et Prénoms du Pere du Mere', on_delete=models.CASCADE, blank=True, null=True, related_name='meres_mere')
    lieun  = models.ForeignKey(Commune, verbose_name='Lieu de Naissance', on_delete=models.CASCADE)
    BuretatCivile = models.ForeignKey(BuretatCivile, verbose_name='Bureau d etat Civil', on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Personne"
        verbose_name = "Acte de naissance"
        ordering = ['nom', 'prenoms']
   

    def __str__(self):
        return f"{self.nom} {self.prenoms}" 

class Homme(models.Model):
    nom = models.CharField(max_length=30, verbose_name="Nom l homme")
    prenoms = models.CharField(max_length=30, verbose_name="Prenoms de homme")
    date_naiss = models.DateField(verbose_name='Date de Naissance')

    class Meta:
        verbose_name_plural = "Homme"
        verbose_name = "Homme"
    def __str__(self):
        return f"{self.nom} {self.prenoms}" 

class Femme(models.Model):
    nom = models.CharField(max_length=30, verbose_name="Nom la Femme")
    prenoms = models.CharField(max_length=30, verbose_name="Prenoms de la Femme")
    date_naiss = models.DateField(verbose_name='Date de Naissance')

    class Meta:
        verbose_name_plural = "Femme"
        verbose_name = "Femme"
    def __str__(self):
        return f"{self.nom} {self.prenoms} " 



class Mariage(models.Model):
    
    marie = models.ForeignKey(Homme, verbose_name="Nom et Prenoms du Marie(e)", on_delete=models.CASCADE, related_name='marie')
    profession_marie = models.CharField(max_length=50, verbose_name="Profession du Marie(e)")
    domicile   = models.CharField(max_length=50, verbose_name="Lieu de Domicile du Marie(e)")
   
    mariee = models.ForeignKey(Femme, verbose_name="Nom et Prenoms du CONJOINT(E)", on_delete=models.CASCADE, related_name='conjoint')
    profession_mariee = models.CharField(max_length=50, verbose_name="Profession du CONJOINT(E)")
    
    date_mariage = models.DateField(verbose_name="Date du Mariage")
    heure_mariage = models.TimeField(verbose_name="Heure du Mariage")
    lieu_mariage = models.CharField(max_length=50, verbose_name="Lieu de Celebartion du Mariage")
    BuretatCivile = models.ForeignKey(BuretatCivile, verbose_name='Bureau d etat Civil', on_delete=models.CASCADE)
    temoine1 = models.ForeignKey(Homme, verbose_name="Nom et Prenoms du Temoin 1", on_delete=models.CASCADE, related_name='temoin1')
    temoine2 = models.ForeignKey(Homme, verbose_name="Nom et Prenoms du Temoin 2", on_delete=models.CASCADE, related_name='temoin2')


    class Meta:
        verbose_name_plural = "Actes de Mariage"
        verbose_name = "Acte de Mariage"
    def __str__(self):
        return f"{self.marie} {self.mariee}" 




class Deces(models.Model):
    personedeces = models.OneToOneField(Persone, verbose_name="Nom et Prenoms du Decede", on_delete=models.PROTECT, related_name='deces')
    annonceur = models.OneToOneField(Persone, verbose_name="Nom et Prenoms d", on_delete=models.PROTECT, related_name='annonceur')
    date_deces = models.DateField(verbose_name="Date du Deces")
    heure_deces = models.TimeField(verbose_name="Heure du Deces")
    lieu_deces = models.CharField(max_length=500, verbose_name="Lieu du Deces")
    cause_deces = models.CharField(max_length=500, verbose_name="Cause du Deces")

    class Meta:
        verbose_name_plural = "Actes de Deces"
        verbose_name = "Acte de Deces"

    def __str__(self):
        return f"{self. personedeces} "    








