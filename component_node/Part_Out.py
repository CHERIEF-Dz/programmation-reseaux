# Etape 2:
# Dans ce module Part_Out, on défini la structure d’une classe Part_Out dérivée 
# d’un thread

from Lib import *
from component_node.Elect import *

class Part_Out(threading.Thread):
    def __init__(self,vaiable_globale):
        threading.Thread.__init__(self)

        # Initialisation le port du voisin
        self.port_next_Neighbor= 0

        # Creer socket appele s (self.s)
        self.s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Etape 1: Créer un objet event:
        # Dans ce TP, on déclare un objet event nommé: 
        # __flag dans le constructeur de la classe «Part_Out» de type Event:
        # On le défini par défaut à False, pour qu’on puisse directement le bloqué
        self.__flag= threading.Event()
        self.__flag.clear() # Set to False

        self.vaiable_globale= vaiable_globale

        # Initialisation du message
        msg= "ELECT"+";"+str(vaiable_globale["Leader_ID"])+";"+str(vaiable_globale["Leader_Port"])
        self.M= Message( msg )

        self.end= False

    def run(self):
        
        try:
            # Se connecter au socket sd_In du noeud suivant
            # avec le port "self.port_next_Neighbor"
            self.s.connect(("127.0.0.1",self.port_next_Neighbor))
        except:
            print("La partie OUT n'arrive pas à se connecter voisin")
            sys.exit()
        
        while not self.end:
            # Etape 2: Bloquer l’envoie du Token:
            # Une fois le socket s’est connecté au socket suivant, 
            #  on bloque le thread en question pour qu’il
            # n’envoie pas systématiquement le token.
            self.__flag.wait()
            self.s.send( str(self.M).encode())
            print("Node envoie un message à ",self.port_next_Neighbor)
            self.__flag.clear()

        # fermer la connexion
        self.s.close()

    # Étape 3: Méthode resume()
    # On défini une méthode à l’intérieur de la classe Part_Out qui défini 
    # la valeur de __flag à True. Ainsi,
    # débloquer le thread pour qu’il continu sont exécution        
    def resume(self):
        self.__flag.set()

    