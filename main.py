import socket
from fonctions import *
from colors import *

def netcat(host, port, msg):
    try:
        # Creation de socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))  # connexion avec serveur
        reponse = s.recv(256); # reception des donnes par block de 256 byte
        print("Response de serveur:\n",reponse.decode(),"\n")
        i=0
        while i < (len(msg)):
            s.sendall(msg[i].encode()); # envoie des donnes vers serveur
            print("Reponse:\n", msg[i].encode(),"\n")
            reponse = s.recv(256); # reception des donnes par block de 256 byte
            print("Response de serveur:\n",reponse.decode(),"\n")
            txt = reponse.decode()
            if i == 1:
                q3(txt)  #appel a la fonction pour reponse sur question 3
            elif i == 2:
                q4(txt)  #appel a la fonction pour reponse sur question 4
            elif i == 3:
                q5(txt)  #appel a la fonction pour reponse sur question 5      
            elif i == 4:
                q6(txt)  #appel a la fonction pour reponse sur question 6
            elif i == 5:
                q7(txt)  #appel a la fonction pour reponse sur question 7
            elif i == 6:
                q8(txt)  #appel a la fonction pour reponse sur question 8
            elif i == 7:
                q9(txt)  #appel a la fonction pour reponse sur question 9
            elif i == 8:
                q10(msg) #appel a la fonction pour reponse sur question 10
            elif i == 9:
                q11(txt) #appel a la fonction pour reponse sur question 11
            i=i+1
        
        reponse = s.recv(256); # reception des donnes par block de 256 byte
        print("Response de serveur:\n",reponse.decode(),"\n")

    except Exception as e:
        print(f"Erreur: {e}")
    finally:
        s.close()  # cloture de connexion
        print("\nConnexion ferme")
                
# donnes de connexion
host = "148.113.42.34"  # Adres IP de serveur
port = 37782         # port de serveur

netcat(host, port, msg)
