import os

#verif_nb_arg : pour vérifier le nombre d’arguments;
def verif_nb_arg(argv):
    return len(argv)==3

#verif_type_PORT : vérifier que le numéro de port saisit est un entier;
def verif_type_PORT( port):
    try:
        int(port)
        return True
    except:
        return False

#verif_PORT_In_Liste : vérifier dans un fichier texte si le numéro de port n’est pas enregistré;
def verif_PORT_In_Liste(port):
    if not os.path.isfile("ports.txt"):
        return True
    
    with open("ports.txt","r") as f:
        for ligne in f:
            if ligne.strip() == str(port):
                return False
    return True

#Add_PORT_List : enregistrer le numéro de port dans un fichier texte.
def Add_PORT_List(port):
    with open("ports.txt", "a") as f:
        f.write(str(port))
        f.write("\n")