from django.shortcuts import render, redirect
from .forms import PersoneForm , MariageForm, DecesForm
from .models import Persone, Mariage, Deces, Homme, Femme
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import datetime



# Create your views here.
def extrait_deces(request, id):
    buf = io.BytesIO()
    # Create a canvas 
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 12)

   
    # add line to texte 
    
    
    deces = Deces.objects.get(id=id)
    
    
    # add text object to canvas
    c.drawString(130, 40, "République Algérienne Démocratique et Populaire") 
    c.drawString(30, 70, "Ministère de l'Intérieur et des Collectivités Locales")
    c.drawString(30, 90, "Direction de l'Etat Civil")
    c.drawString(30, 110, "Willaya:   "+(deces.personedeces.BuretatCivile.Commune.Daira.Wilaya).__str__())
    c.drawString(50,111, "............................................................") 
    c.drawString(30, 130, "Daira:   "+(deces.personedeces.BuretatCivile.Commune.Daira).__str__())
    c.drawString(50,131, "............................................................") 
    c.drawString(30, 150, "Commune:   "+(deces.personedeces.BuretatCivile.Commune).__str__()) 
    c.drawString(50,151, "............................................................")
    c.drawString(30, 170, "Bureau:   "+(deces.personedeces.BuretatCivile).__str__())
    c.drawString(50,171, "............................................................")
    c.drawString(240, 220, "ACTE DE DECES")
    c.drawString(148,260, "le  " +(deces.date_deces).__str__())
    c.drawString(180,261, "............................................................................................................................")
    c.drawString(30,290, "Numéro de l'acte        à:      " +(deces.heure_deces).__str__()+"           à           "+(deces.lieu_deces).__str__())
    c.drawString(180,291, "............................................................................................................................")
    
    c.drawString(35,320,(deces.id).__str__()+ "                                                              "+(deces.personedeces).__str__())
    c.drawString(148,321, "......................................................................................................................................")
    
    c.drawString(148,350, "né le:   "+(deces.personedeces.date_naiss).__str__()+"   à:   "+(deces.personedeces.lieun).__str__())
    c.drawString(180,351, "............................................................................................................................")
    c.drawString(148,380, "Du sexe:   "+(deces.personedeces.sexe).__str__())
    c.drawString(180,381, "............................................................................................................................")
    
    c.drawString(148,410, "Fils de   "+(deces.personedeces.pere).__str__())
    c.drawString(180,411, "............................................................................................................................")
    
    c.drawString(148,440, "Et de   "+(deces.personedeces.mere).__str__())
    c.drawString(180,441, "............................................................................................................................")
    
    c.drawString(148,470, "Dressé le       "+datetime.datetime.now().strftime("%d/%m/%Y"))
    c.drawString(180,471, "............................................................................................................................")
    
    c.drawString(148,500, "sur la déclaration de  "+(deces.annonceur).__str__())
    c.drawString(340,501, ".............................................................................")
    
    c.drawString(148,530, "domicilié en cette commune, qui lecture faite a signé avec Nous")
    c.drawString(148,560, "Mentions mentionnées sur l'acte de deces")
    c.drawString(380,561, "................................................................")
    c.drawString(148,590, "......................................................................................................................................")
    
    
    c.drawString(370,650, "Fait à :   "+(deces.personedeces.BuretatCivile).__str__()+"   le:   "+datetime.datetime.now().strftime("%d/%m/%Y"))
    c.drawString(360,651, "............................................................")
    c.drawString(370,670, "L'officier de l'etat civil ")
    c.drawString(370,690, "signature et cachet")
    c.drawString(30, 750, "Réf:  EC.4")
    
    
    
    
    
    c.showPage()
    c.save()
    buf.seek(0)
    
        
   
    return FileResponse(buf, as_attachment=True, filename='extrait_de_deces.pdf')

    



def extrait_mariage(request, id):
     # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas 
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 10)

   
    # add line to texte 
    
    
    mariage = Mariage.objects.get(id=id)
    marie_info=Persone.objects.get(id=mariage.marie.id)
    mariee_info=Persone.objects.get(id=mariage.mariee.id)

    c.drawString(130, 40, "République Algérienne Démocratique et Populaire") 
    c.drawString(30, 70, "Ministère de l'Intérieur et des Collectivités Locales")
    c.drawString(30, 90, "Direction de l'Etat Civil")
    c.drawString(30, 110, "Willaya:   "+(marie_info.BuretatCivile.Commune.Daira.Wilaya).__str__()) 
    c.drawString(50,111, "............................................................")
    c.drawString(30, 130, "Daira:   "+(marie_info.BuretatCivile.Commune.Daira).__str__())
    c.drawString(50,131, "............................................................") 
    c.drawString(30, 150, "Commune:   "+(marie_info.BuretatCivile.Commune).__str__()) 
    c.drawString(50,151, "............................................................")
    c.drawString(30, 170, "Bureau:   "+(marie_info.BuretatCivile).__str__())
    c.drawString(50,171, "............................................................")
    c.drawString(240, 220, "ACTE DE MARIAGE")
    c.drawString(250,240,"[Copie intégrale(1)Extrait(2)]")

    c.drawString(148,260, "le  " +(mariage.date_mariage).__str__())
    c.drawString(180,261, "............................................................................................................................")
    c.drawString(30,280, "Numéro de l'acte        à:      " +(mariage.heure_mariage).__str__()+"       à la Communede :           "+(mariage.lieu_mariage).__str__())
    c.drawString(180,281, "............................................................................................................................")
    c.drawString(35,300,(mariage.id).__str__()+ "                               Daira:       "+(mariage.BuretatCivile.Commune.Daira).__str__()+"          Willaya de :    "+(mariage.BuretatCivile.Commune.Daira.Wilaya).__str__())
    c.drawString(180,301, "............................................................................................................................")
    c.drawString(148,320, 'Comparu devant Nous publiquement au siége de la Commune(4) :')
    c.drawString(180,321, "                                                                                                  ..........................")
    c.drawString(170,340, "Le nommé:   "+(mariage.marie).__str__())
    c.drawString(180,341, "............................................................................................................................")
    c.drawString(148,360, "Profession:   "+(mariage.profession_marie).__str__()+"         ne le:   "+(mariage.marie.date_naiss).__str__())
    c.drawString(180,361, "............................................................................................................................")
    c.drawString(148,380, "Fils de    :"+(marie_info.pere).__str__()+ "                   Et de      : "+(marie_info.mere).__str__() )
    c.drawString(180,381, "............................................................................................................................")
    
    c.drawString(170,410, "Et la Nommée:   "+(mariage.mariee).__str__())
    c.drawString(180,411, "............................................................................................................................")
    c.drawString(148,430, "Profession:   "+(mariage.profession_mariee).__str__()+"       ne le:   "+(mariage.mariee.date_naiss).__str__())
    c.drawString(180,431, "............................................................................................................................")
    c.drawString(148,450, "File de    "+(mariee_info.pere).__str__()+ "                  Et de "+(mariee_info.mere).__str__() )
    c.drawString(180,451, "............................................................................................................................")
    c.drawString(148,470, "Lesquels ont déclaré publiquement vouloir se prendre pour Epoux,et Nous avouns" )
    c.drawString(148,490, "prononcé au nom de la Loi qu'ils sont unis par le mariage en présence de:                    ")
    
    c.drawString(148,510, (mariage.temoine1).__str__() +"       Et de :                    "+(mariage.temoine2).__str__())
    c.drawString(180,511, "............................................................................................................................")
    c.drawString(148,530, "Mentions marginales:  ")
    c.drawString(180,531, "............................................................................................................................")
    
    c.drawString(148,551, "......................................................................................................................................")
    c.drawString(148,571, "......................................................................................................................................")
    c.drawString(370,600, "Fait à :   "+(mariage.BuretatCivile).__str__()+"   le:   "+datetime.datetime.now().strftime("%d/%m/%Y"))
    c.drawString(400,601, "...................................................")
    c.drawString(370,620, "L'officier de l'etat civil ")
    c.drawString(370,640, "signature et cachet")
    c.drawString(30, 680, "-1 et 2 Rayer les mentions inutiles")
    c.drawString(30, 700, "-3 Extrait de l'acte de mariage conclus devant le notaire")
    c.drawString(30, 720, "-4 Extrait de l'acte de mariage conclus devant l'officier de l'etat civil")
    c.drawString(30, 750, "Réf:  EC.1")
    
    
        
   
    # add text object to canvas

    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='extrait_de_mariage.pdf')







def extrait_pdf(request, id):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas 
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

   
    # add line to texte 
    
    
    persone = Persone.objects.get(id=id)
    
    # add text object to canvas
    c.drawString(130, 40, "République Algérienne Démocratique et Populaire") 
    c.drawString(30, 70, "Ministère de l'Intérieur et des Collectivités Locales")
    c.drawString(30, 90, "Direction de l'Etat Civil")
    c.drawString(30, 110, "Willaya:   "+(persone.BuretatCivile.Commune.Daira.Wilaya).__str__()) 
    c.drawString(50,111, "............................................................")
    c.drawString(30, 130, "Daira:   "+(persone.BuretatCivile.Commune.Daira).__str__()) 
    c.drawString(50,131, "............................................................")
    c.drawString(30, 150, "Commune:   "+(persone.BuretatCivile.Commune).__str__()) 
    c.drawString(50,151, "............................................................")
    c.drawString(30, 170, "Bureau:   "+(persone.BuretatCivile).__str__())
    c.drawString(50,171, "............................................................")
    c.drawString(240, 220, "ACTE DE NAISSANCE")
    c.drawString(148,260, "le  " +(persone.date_naiss).__str__())
    c.drawString(153,261, "..............................................................................................................................")
    c.drawString(30,290, "Numéro de l'acte        à:      " +(persone.heure_naiss).__str__()+"       est né(e) à           "+(persone.lieun).__str__())
    c.drawString(153,291, "..............................................................................................................................")
    c.drawString(35,320,(persone.id).__str__()+ "                               Commune:       "+(persone.BuretatCivile.Commune).__str__()+"          Willaya de :    "+(persone.BuretatCivile.Commune.Daira.Wilaya).__str__())
    c.drawString(153,321, "..............................................................................................................................")
    c.drawString(148,350, "Le:   "+(persone.nom).__str__()+" "+(persone.prenoms).__str__())
    c.drawString(153,351, "..............................................................................................................................")
    c.drawString(148,380, "Du sexe:   "+(persone.sexe).__str__())
    c.drawString(153,381, "..............................................................................................................................")
    c.drawString(148,410, "Fils de   "+(persone.pere).__str__())
    c.drawString(153,411, "..............................................................................................................................")
    c.drawString(148,440, "Fils de   "+(persone.pere_pere).__str__())
    c.drawString(153,441, "..............................................................................................................................")
    c.drawString(148,470, "Et de   "+(persone.mere).__str__())
    c.drawString(153,471, "..............................................................................................................................")
    c.drawString(148,500, "Fils de   "+(persone.pere_mere).__str__())
    c.drawString(153,501, "..............................................................................................................................")
    c.drawString(148,530, "Mentions mentionnées sur l'acte de naissance")
    c.drawString(153,531, "..............................................................................................................................")
    c.drawString(153,531, "..............................................................................................................................")
    c.drawString(153,561, "..............................................................................................................................")
    c.drawString(370,600, "Fait à :   "+(persone.BuretatCivile).__str__()+"   le:   "+datetime.datetime.now().strftime("%d/%m/%Y"))
    c.drawString(400,601, "...................................................")
    c.drawString(370,620, "L'officier de l'etat civil ")
    c.drawString(370,640, "signature et cachet")
    c.drawString(30, 680, "-1 et 2 Rayer les mentions inutiles")
    c.drawString(30, 700, "-3 En toutse lettres")
    c.drawString(30, 720, "-4 Nom et Prénom de l'enfant")
    c.drawString(30, 750, "Réf:  EC.7")
    
    
    
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='extrait_de_naissance.pdf')


def venue_pdf(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas 
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

   
    # add line to texte 
    """
    lines = [
        "THis is line 1"
        "THis is line 2"
        "THis is line 3"
        "THis is line 4"

    ]"""
    persones = Persone.objects.all()
    lines = []

    for persone in persones:
        lines.append((persone.id).__str__())
        lines.append((persone.prenoms).__str__())
        lines.append((persone.sexe).__str__())
        lines.append((persone.date_naiss).__str__())
        lines.append((persone.heure_naiss).__str__())
        lines.append((persone.pere).__str__())
        lines.append((persone.pere_pere).__str__())
        lines.append((persone.mere).__str__())
        lines.append((persone.pere_mere).__str__())
        lines.append((persone.hopital).__str__())
        lines.append((persone.BuretatCivile).__str__())
        
    for line in lines:
        textob.textLine(line)
    # add text object to canvas
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='hello.pdf')






def ajouter(request):
    if request.method == 'POST':
        form = PersoneForm(request.POST)
        if form.is_valid():
            form.save()
            if form.cleaned_data['sexe'] == 'Feminin':
                femme = Femme(nom = form.cleaned_data['nom'], prenoms = form.cleaned_data['prenoms'], date_naiss=form.cleaned_data['date_naiss'] )
                femme.save()
                persone=Persone.objects.filter(nom__contains = form.cleaned_data['nom'], prenoms__contains = form.cleaned_data['prenoms'])
                return render(request,"show.html",{"data":persone})
            else:
                homme = Homme(nom = form.cleaned_data['nom'], prenoms = form.cleaned_data['prenoms'], date_naiss=form.cleaned_data['date_naiss'] )
                homme.save()
                persone=Persone.objects.filter(nom__contains = form.cleaned_data['nom'], prenoms__contains = form.cleaned_data['prenoms'])
                return render(request,"show.html",{"data":persone})     
    else:
        form = PersoneForm()
    return render(request,'ajouterper.html',{'form':form})

def ajoumariage(request):
    if request.method == 'POST':
        form1 = MariageForm(request.POST)
        if form1.is_valid():
            form1.save()
            if form1.cleaned_data['marie'] and form1.cleaned_data['mariee']:
                mariage=Mariage.objects.get(marie= form1.cleaned_data['marie'] ,mariee= form1.cleaned_data['mariee'])
                return render(request,"showmariage.html",{"data":mariage})
    else:
        form1 = MariageForm()
    return render(request,'mariage.html',{'form1':form1})




def ajoudeces(request):
    if request.method == 'POST':
        form2 = DecesForm(request.POST)
        if form2.is_valid():
            form2.save()
            if form2.cleaned_data['personedeces']:
                deces=Deces.objects.get(personedeces = form2.cleaned_data['personedeces'])
                return render(request,"showdeces.html",{"data":deces})
    else:
        form2 = DecesForm()
    return render(request,'ajoudeces.html',{'form2':form2})

def abf(request):
     return render(request, 'recherche.html')


def rechercher_persone(request):
    persone=""
    if request.method =="GET":
     query_nom=request.GET.get('nom')
     query_prenoms=request.GET.get('prenoms')
     if query_nom and query_prenoms:
       persone=Persone.objects.filter(nom__contains = query_nom, prenoms__contains = query_prenoms)
    return render(request,"search.html",{"data":persone}) 



def rechercher_mariage(request):
    mariage=""
    if request.method =="GET":
     query_num=request.GET.get('num_mariage')
     if query_num:
       mariage=Mariage.objects.filter(id__contains = query_num)
    return render(request,"searchmariage.html",{"data":mariage})                   
   

     
def recherche_deces(request):
    deces=""
    if request.method =="GET":
     query=request.GET.get('num_deces')
     if query:
       deces=Deces.objects.filter(id__contains = query)
    return render(request,"searchdeces.html",{"data":deces})

def edit(request, id):
    persone = Persone.objects.get(id=id)
    return render(request,'edit.html', {'persone':persone})     


def update(request, id):
    personne = Persone.objects.get(id=id)
    if request.method == 'POST':
        form = PersoneForm(request.POST, instance=personne)
        if form.is_valid():
            # mettre à jour l’objet dans la base de données
            form.save()
            #id=id+1
            # rediriger vers la page liste commandes
            persone=Persone.objects.filter(nom__contains = form.cleaned_data['nom'], prenoms__contains = form.cleaned_data['prenoms'])
            return render(request,"show.html",{"data":persone})
    else :
        form = PersoneForm(instance=personne)
        # on pré-remplir le formulaire avec l’objet ayant l’id spécifié

        return render(request, 'edit.html',{'form' : form} )  


def statistique(request):
    nbr_persone= Persone.objects.count()
    nbr_deces= Deces.objects.count()
    nbr_mariage= Mariage.objects.count()
    nbr_homme = Homme.objects.count()
    nbr_femme = Femme.objects.count()
    context={
        'nbr_homme':nbr_homme,
        'nbr_femme':nbr_femme,
        'nbr_persone':nbr_persone,
        'nbr_deces':nbr_deces,
        'nbr_mariage':nbr_mariage,


    }
    return render(request, 'datasatistique.html', context) 


