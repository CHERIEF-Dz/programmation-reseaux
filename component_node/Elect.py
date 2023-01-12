import random as rnd

#   Implemantation de l'algorithme d'election de Chang et Roberts

#   Definition de la classe Message
class Message:
    def __init__(self, Type, Id_elect, Port_elect):
        #   «Type» = toujours contient la chaîne de caractère «ELECT»
        #   «Id_elect» : contient l’identifiant du noeud élu
        #   «Port_elect» : contient le numéro de port du noeud élu.
        self.Type= Type
        self.Id_elect= Id_elect
        self.Port_elect= Port_elect
    
    def __init__(self, msg_str):
        #   «Type» = toujours contient la chaîne de caractère «ELECT»
        #   «Id_elect» : contient l’identifiant du noeud élu
        #   «Port_elect» : contient le numéro de port du noeud élu.
        self.Type, self.Id_elect, self.Port_elect= msg_str.split(";")
        self.Id_elect= int(self.Id_elect)

    #   Cette fonction modifie self.Id_elect
    def setId_elect(self,Id_elect):
        self.Id_elect= Id_elect
    
    #   Cette fonction modifie self.Port_elect
    def setPort_elect(self,Port_elect):
        self.Port_elect= Port_elect
    
    #   Cette fonction transforme cet objcet en chaine de caractere 
    def __str__(self):
        return self.Type+";"+str(self.Id_elect)+";"+str(self.Port_elect)

#   Initialisation de l’élection
def init_election(PORT_In,vaiable_globale):
    #1. générer une valeur aléatoire représentant l’identifiant du noeud. La
    #       valeur est stockée dans la variable «ID» entre 1 et 1000000
    vaiable_globale["ID"] = rnd.randint(1, 1000000)
    vaiable_globale["PORT_In"]= PORT_In

    #2. Leader_ID ← ID
    vaiable_globale["Leader_ID"] = vaiable_globale["ID"]

    #3. Leader_Port ← PORT_In (Numéro de port)
    vaiable_globale["Leader_Port"] = PORT_In


#   Réception du message M:
def reception_message( M, vaiable_globale, Sortie ):
    #   1.  si (M.Id_elect > Leader_ID) alors :
    if M.Id_elect >vaiable_globale["Leader_ID"]:
        vaiable_globale["Leader_ID"] = M.Id_elect # Leader_ID ← M.Id_elect
        vaiable_globale["Leader_Port"] = M.Port_elect # Leader_Port ← M.Port_elect
    else:
        M.Id_elect = vaiable_globale["Leader_ID"] # M.Id_elect ← Leader_ID
        M.Port_elect = vaiable_globale["Leader_Port"] # M.Port_elect ← Leader_Port
    
    #   2. envoyer au noeud suivant le message (M)
    Sortie.resume()