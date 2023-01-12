# Etape 2:
from Lib import *
from component_node.Part_In import *
from component_node.Part_Out import *
from component_node.Checking import *
from component_node.Elect import *

# Verifier le nombre d'argument
if not verif_nb_arg(sys.argv):
    print("Le nombre d'argument passe en parametre n'est pas correcte")
    print("python Node.py <port> <jeton>\n")
    sys.exit()

# Verifier si le numero de port est entier
if not verif_type_PORT(sys.argv[1]):
    print("Le numero de port passe en parametre n'est pas entier")
    sys.exit()

# Etape 3:
PORT_In= int(sys.argv[1])       #Le numero du port
Have_Token= int(sys.argv[2])    #Est-ce que le noeud a le jeton

# Verifier si le numero de port existe
if verif_PORT_In_Liste(PORT_In):
    Add_PORT_List(PORT_In)
else:
    print("Le numero de port peut etre occuper par un autre processus")
    sys.exit()

# Declaration de variables globale
vaiable_globale={}

# Initialisation de l'election
init_election(PORT_In,vaiable_globale)
print("Le noued ",vaiable_globale["Leader_ID"],"a le PORT_In",vaiable_globale["Leader_Port"])


# Etape 4:
# Lancer un thread pour Part_Out
Sd_Out= Part_Out(vaiable_globale)

# Etape 5:
# Lancer un thread pour Part_In
Sd_In= Part_In(PORT_In, Have_Token, Sd_Out)
Sd_In.start()

# Etape 6:
# Le programme attend voir le numero du PORT_In du prochain voisin,
# et pour laisser temps au prochain voisin d'etre en ecoute
Sd_Out.port_next_Neighbor= int(input("Numero de port du voisin:\t"))
Sd_Out.start()


# Attendre la fin des threads
Sd_In.join()
Sd_Out.join()

print("Fin")