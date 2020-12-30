import mysql.connector as mysqlpyth
import tkinter as tk
from tkinter import ttk
from functools import partial


#Python se connecte sur la bdd
    
bdd = mysqlpyth.connect(user='root', 
    password='root', 
    host='localhost', 
    port="8081", 
    database='breizhinbus')

# récupèration du curseur 
cursor = bdd.cursor()



# Création de la fenêtre de l'application
root = tk.Tk()
root.title("Application Breizhibus")
root.geometry("400x400") 
root.configure(bg="black") 

#frame titre
frame_titre = tk.Frame(root, bg="red")
frame_titre.pack()
titre = tk.Label(frame_titre, text='Breizhibus', font=("Helvetica", 20), bg='orange', fg='white')
titre.pack(pady=10, padx=10) 




#Affichage des lignes de bus
def aff_lignes():
    cursor.execute("SELECT nom_ligne FROM lignes;")
    req_lignes = cursor.fetchall()
    #print(req_lignes)
    saisi_aff_lignes.insert(0, req_lignes)



# Création du bouton affichage de lignes
bouton = tk.Button(root, text='liste des lignes', font=("Helvetica", 10), height=5, width=15, bd=10, bg='orange', fg='Black')
bouton.place(x=5, y=100)

bouton.configure(command=aff_lignes) 

saisi_aff_lignes = tk.Entry(root, width=50, justify="center", font=("Helvetica", 15), bg="white", fg="black")
saisi_aff_lignes.place(x=200, y=120)



##Affichage des arrets en fonction de la ligne sélectionnée.

cursor.execute("SELECT nom_ligne FROM lignes;")
req_lignes = cursor.fetchall()

label_choix_ligne = tk.Label(root, text='veuillez choisir une ligne', font=("Helvetica", 16), bg='orange', fg='black')
label_choix_ligne.place(x=5, y=250) 
listecombo = ttk.Combobox(root, values=req_lignes)
listecombo.place(x=250, y=250)
listecombo_val = listecombo.get() 
#print(listecombo_val)

    #return choix_ligne

#demand_choix_ligne()

def aff_arret(lignes):
    
    cursor.execute(f"""SELECT nom, adresse FROM arret
    INNER JOIN arret_ligne ON arret.id_arret = arret_ligne.id_arret
    INNER JOIN lignes ON arret_ligne.id_lignes = lignes.id_lignes
    WHERE nom_ligne = '{lignes}'""")
    req_arret_ligne = cursor.fetchall()
        
    saisi_aff_arret.insert(0, req_arret_ligne)
    print(req_arret_ligne)
         
    
    #bdd.commit    
    

#aff_arret('Noire')   

saisi_aff_arret = tk.Entry(root, width=150, justify="left", font=("Helvetica", 15), bg="white", fg="black")
saisi_aff_arret.place(x=200, y=300)
   

# Création du bouton affichage des arrets en fonction de la ligne
bouton_arret = tk.Button(root, text='liste des arrêts', font=("Helvetica", 10), height=5, width=15, bd=10, bg='orange', fg='Black')
bouton_arret.place(x=5, y=300)

bouton_arret.configure(command=lambda: aff_arret(listecombo.get()))




#insérer un nouveau bus dans la bdd.

    #création des labels pour l'insertion des bus
label_insertion_bus = tk.Label(root, text='insertion de bus', font=("Helvetica", 20), bg='orange', fg='black')
label_insertion_bus.pack(pady=300, padx=10) 
label_numero_bus = tk.Label(root, text='veuillez insérer un numéro de bus', font=("Helvetica", 16), bg='orange', fg='black')
label_numero_bus.place(x=5, y=450) 
label_immatriculation = tk.Label(root, text='veuillez insérer une immatriculation', font=("Helvetica", 16), bg='orange', fg='black')
label_immatriculation.place(x=5, y=500) 
label_nombre_place = tk.Label(root, text='veuillez insérer le nombre de places', font=("Helvetica", 16), bg='orange', fg='black')
label_nombre_place.place(x=5, y=550) 
label_id_ligne = tk.Label(root, text='veuillez insérer un identifiant ligne', font=("Helvetica", 16), bg='orange', fg='black')
label_id_ligne.place(x=5, y=600) 

    #création des entry pour l'insertion des bus
numero1 = tk.Entry(root, width=50, justify="center", font=("Helvetica", 15), bg="white", fg="black")
numero1.place(x=400, y=450)
immatriculation1 = tk.Entry(root, width=50, justify="center", font=("Helvetica", 15), bg="white", fg="black")
immatriculation1.place(x=400, y=500)
nombre_place1 = tk.Entry(root, width=50, justify="center", font=("Helvetica", 15), bg="white", fg="black")
nombre_place1.place(x=400, y=550)
id_lignes1 = tk.Entry(root, width=50, justify="center", font=("Helvetica", 15), bg="white", fg="black")
id_lignes1.place(x=400, y=600)



def ins_bus():
    

    numero = numero1.get()
    immatriculation = immatriculation1.get()
    nombre_place = nombre_place1.get()
    id_lignes = id_lignes1.get()
    
    requete2 = "INSERT INTO bus (numero, immatriculation, nombre_place, id_lignes) VALUES (%s, %s, %s, %s)" 
    parametre2 = (numero, immatriculation, nombre_place, id_lignes, )
    cursor.execute(requete2, parametre2)
    bdd.commit()
    req_bus_ligne = cursor.fetchall
    #print(req_bus)        

#ins_bus()

bouton_ajout = tk.Button(root, text='ajout bus', font=("Helvetica", 10), height=5, width=15, bd=10, bg='orange', fg='Black')
bouton_ajout.place(x=1100, y=500)

bouton_ajout.configure(command=ins_bus)



#suppression d'un bus

label_suppression_bus = tk.Label(root, text='suppression de bus', font=("Helvetica", 20), bg='orange', fg='black')
label_suppression_bus.pack(pady=500, padx=10) 
label_suppr_bus = tk.Label(root, text='Entrez le numero de bus à supprimer', font=("Helvetica", 16), bg='orange', fg='black')
label_suppr_bus.place(x=5, y=700) 
bus_suppr = tk.Entry(root, width=50, justify="center", font=("Helvetica", 15), bg="white", fg="black")
bus_suppr.place(x=400, y=700)



def suppression_bus():
    
    numero = bus_suppr.get()
    requete3 = "DELETE FROM bus WHERE numero = %s" 
    parametre3 = (numero, )
    cursor.execute(requete3, parametre3)
    bdd.commit()# pour agir et faire l'action sur la bdd

#suppression_bus()

bouton_suppression = tk.Button(root, text='suppression bus', font=("Helvetica", 10), height=5, width=15, bd=10, bg='orange', fg='Black')
bouton_suppression.place(x=1100, y=700)

bouton_suppression.configure(command=suppression_bus)



root.mainloop()    

#Fermeture du curseur et de la base de données 
cursor.close()
bdd.close()
    

 # for i in range(len(req_arret_ligne)):
    #     label_arret = tk.Label(root, text= req_arret_ligne[i], font=("Helvetica", 16), bg='orange', fg='black')
    #     label_arret.grid(rows=i, column=1, padx=35) 
       