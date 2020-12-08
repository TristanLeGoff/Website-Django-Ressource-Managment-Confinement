from ConfinAide.models import Client


def Verification(request):
    mail = request.POST.get("email",request.session.get("id_mail",None))
    password = request.POST.get("password",request.session.get("id_password",None))
    if(mail == None or password == None): return False
    test = Client.objects.filter(mail=mail,password=password)
    if(len(test)!=0):
        request.session["id_mail"]=str(mail)
        request.session["id_password"]=str(password)
        return True
    else: return False
        
    
def Inscription (request):
    name = request.POST["name-input-field"]
    first_name = request.POST["firstname-input-field"]
    mail = request.POST["email-input-field"]
    adress = request.POST["adress-input-field"]
    tel = request.POST["name-input-field"]
    password = request.POST["password-input-field"]
    password2 = request.POST["repeat-password-field"]
    nbr_personne = request.POST["nbrpeople"]
    
    if(password!=password2):
        return False
    else:
        new_client = Client(nom=name,prenom=first_name,mail=mail,adresse=adress,tel=tel,password=password,nbr_personne=nbr_personne)
        new_client.save()
        request.session["id_mail"]=str(mail)
        request.session["id_password"]=str(password)
        return True
    
    
def Deconnexion(request):
    request.session["id_mail"] = None
    request.session["id_password"] = None
    
