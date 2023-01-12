# Etape 4:
# Importer Lib
from Lib import *
from component_node.Elect import *


# Etape 7: Fonction Handle_Neighbor
def Handle_Neighbor(con, add, t, Sortie):
    condition_arret= True

    # Ancien message
    ancien_msg= b""

    while condition_arret:
        if t==0:
            msg= con.recv(1024)
            print("Ce noued a reçu le message",str(msg))
            
            #Appeler l'Algorithme de reception
            Sortie.M= Message(msg.decode())
            reception_message( Sortie.M , Sortie.vaiable_globale ,Sortie )
            
            # Si le noeud reçoit le meme message 2 fois
            if ancien_msg==msg:
                print("Le LEADER est",Sortie.vaiable_globale["Leader_ID"]," qui a le PORT_In",Sortie.vaiable_globale["Leader_Port"])
                condition_arret= False
                Sortie.end= True
            else:
                ancien_msg= msg
        if t==1:
            input("Vous etes l'intiateur du token, tapez Entrer commencer la simulation")
            # on appelle la méthode «resume()» de l’objet «Sd_Out» dans la focntion «Handle_Neighbor()
            Sortie.resume()
            t=0 # S'il étais l'initiateur, il ne l'est pas
    # Fermer la connexion
    con.close()


# Etape 5: Implémenter la classe :
# Dans ce module Part_In, on défini la structure d’une classe Part_In
#    dérivée d’un thread
class Part_In(threading.Thread):

    def __init__(self, port, T, S):
        threading.Thread.__init__(self)#appeler le constructeur de la classe Thread

        # Initialisation le port
        self.port= port

        # Initialisation de la valeur de T
        self.T= T

        # Thread Sd_Out
        self.Sortie= S

        # Creer socket appelee ss (self.ss)
        self.ss= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Attacher le socket declarer une addresse IP <<localhost>>
            #             et le numero de port recuperer dans self.port 
            self.ss.bind(('127.0.0.1', self.port))

        except:
            print("Le Sd_In n'arrive pas à s'attacher à l'addresse et le numero de port")
            sys.exit()
        
        # Mettre la socket en mode ecoute passive
        self.ss.listen()
    
    # Etape 6: Méthode run ():
    # Dans la topologie proposée dans ce TP, le serveur de chaque noeud traitera 
    # uniquement avec le client du noeud précédent. Donc, le serveur sera de 
    # type itératif (i.e: pas besoin d’avoir une boucle pour accepter plusieurs clients)
    def run(self):
        # dans la methode run(), socket accepte une seule demande de connexion
        self.connexion,self.add = self.ss.accept()

        # Appel la fonction <<Handle_Neighbor>> qui est defini en haute de ce module 
        Handle_Neighbor( self.connexion, self.add, self.T, self.Sortie)

        # Cependant, la gestion du service de réception des message se fera 
        # dans une fonction à part: Handle_Neighbor. 
        # Cette fonction est définie en haut en dessus de la classe «Part_In».

        # Fermer la connexion
        self.ss.close()