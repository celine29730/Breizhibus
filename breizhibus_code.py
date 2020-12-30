import mysql.connector as mysqlpyth



#Python se connecte sur la bdd
    
bdd = mysqlpyth.connect(user='root', 
    password='root', 
    host='localhost', 
    port="8081", 
    database='breizhinbus')

# récupèration du curseur 
cursor = bdd.cursor()


#Affichage des lignes de bus
def aff_lignes():
    cursor.execute("SELECT nom_ligne FROM lignes;")
    req_lignes = cursor.fetchall()
    print(req_lignes)

aff_lignes()


#Affichage des arrets en fonction de la ligne sélectionnée.
#def demand_choix_ligne():
choix_ligne = input("Veuillez choisir un nom de ligne : ")
print(choix_ligne)
cursor.execute("SELECT nom_ligne FROM lignes;")
req_lignes = cursor.fetchall()


    #return choix_ligne

#demand_choix_ligne()

def aff_arret(lignes):
    
    cursor.execute(f"""SELECT nom, adresse FROM arret
    JOIN arret_ligne ON arret.id_arret = arret_ligne.id_arret
    JOIN lignes ON arret_ligne.id_lignes = lignes.id_lignes
    WHERE nom_ligne = '{lignes}';""")
    req_arret_ligne = cursor.fetchall()
    print(req_arret_ligne)
    

    bdd.commit    
    

aff_arret(choix_ligne)   


#print(aff_arret(choix_ligne))

#insérer un nouveau bus dans la bdd.

def ins_bus():
    #id = input("veuillez rentrer l'id_bus: ")
    numero = str(input("veuillez rentrer le numéro de bus: "))
    immatriculation = str(input("veuillez l'immatriculation du bus: "))
    nombre_place = int(input("veuillez rentrer un nombre de place: "))
    id_lignes = int(input("veuillez rentrer l'id_lignes: "))
    requete1 = "SELECT * FROM bus WHERE numero = %s"
    parametre1 = (numero, )
    cursor.execute(requete1, parametre1)
    req_exist = cursor.fetchall()
    print(req_exist)    
    if req_exist:
       print("l'élément est déjà dans la bdd!!!")
    else:
        requete2 = "INSERT INTO bus (numero, immatriculation, nombre_place, id_lignes) VALUES (%s, %s, %s, %s)" 
        parametre2 = (numero, immatriculation, nombre_place, id_lignes, )
        cursor.execute(requete2, parametre2)
    bdd.commit()
    #req_bus_ligne = cursor.fetchall
    #print(req_bus)        

ins_bus()


#suppression d'un bus
def suppression_bus():
    bus_suppr = str(input("veuillez rentrer le numéro de bus à supprimer: "))
    requete3 = "DELETE FROM bus WHERE numero = %s" 
    parametre3 = (bus_suppr, )
    cursor.execute(requete3, parametre3)
    bdd.commit()# pour agir et faire l'action sur la bdd

suppression_bus()



#appel des fonctions
#aff_lignes()
#demand_choix_ligne()
#print(aff_arret(choix_ligne))
#ins_bus()
#suppression_bus()

#choix_ligne = demand_choix_ligne() #pour stocker le résultat de la fonction
    

#Fermeture du curseur et de la base de données 
cursor.close()
bdd.close()
    

    