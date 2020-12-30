## BREIZHIBUS
**fonctionnement de l'application**

L'application se concentre sur une page.
Chaque bouton appelle une fonction qui a été crée indépendemment.


![images1](https://github.com/celine29730/Breizhibus/blob/main/Annotation%202020-12-30%20142533.png)

Le premier bouton permet d'afficher toutes les lignes présentes dans la base de données.

J'ai crée ensuite une liste déroulante (**combobox**) afin de pouvoir choisir une ligne de bus. En fonction de ce choix j'ai réalisé un bouton et une **Entry** qui permet d'afficher les arrêts associées en fonction de la ligne choisie. Le bouton crée fait appel en commande à la fonction aff_arret et j'ai utilisé la fonction temporaire **lambda** pour pouvoir mettre en paramètre de ma fonction le choix de ma liste déroulante. 

J'ai crée ensuite tout un bloc consacré à l'insertion d'un bus directement dans la base de données.
pour celà, j'ai procédé à la création de toutes les **Entry** nécessaires et qui constituent tous les champs de ma table **Bus**.
L'utilisatur doit y entrer **le numéro de bus**, **l'immatriculation**, **le nombre de places du bus** ainsi que **l'identifiant lignes** qui correspond à l'Id lignes de ma table lignes (numéro compris entre 8 et 11).

Une fois les informations rentrées, l'utilisateur n'a plus qu'à appuyer sur le bouton **ajout bus**, afin de pouvoir ajouter le bus directement dans la base de données.
La commande du bouton ajout se rapporte à la fonction ins_bus crée.





