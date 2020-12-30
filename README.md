## BREIZHIBUS
# 1.**fonctionnement de l'application**

L'application se concentre sur une page.
Chaque bouton appelle une fonction qui a été crée indépendamment.


![images1](https://github.com/celine29730/Breizhibus/blob/main/Annotation%202020-12-30%20142533.png)

* Le premier bouton permet d'afficher toutes les lignes présentes dans la base de données.

* J'ai crée ensuite une liste déroulante (**combobox**) afin de pouvoir choisir une ligne de bus. En fonction de ce choix j'ai réalisé un bouton et une **Entry** qui permet d'afficher les arrêts associées en fonction de la ligne choisie. Le bouton crée fait appel en commande à la fonction aff_arret et j'ai utilisé la fonction temporaire **lambda** pour pouvoir mettre en paramètre de ma fonction le choix de ma liste déroulante. 

* J'ai crée ensuite tout un bloc consacré à l'insertion d'un bus directement dans la base de données.
pour celà, j'ai procédé à la création de toutes les **Entry** nécessaires et qui constituent tous les champs de ma table **Bus**.
L'utilisatur doit y entrer **le numéro de bus**, **l'immatriculation**, **le nombre de places du bus** ainsi que **l'identifiant lignes** qui correspond à l'Id lignes de ma table lignes (numéro compris entre 8 et 11).

Une fois les informations rentrées, l'utilisateur n'a plus qu'à appuyer sur le bouton **ajout bus**, afin de pouvoir ajouter le bus directement dans la base de données.
La commande du bouton ajout se rapporte à la fonction ins_bus crée.

![images 2](https://github.com/celine29730/Breizhibus/blob/main/Annotation%202020-12-30%20142707.png)

* Le processus est le même pour la suppression d'un bus directement dans la base de données.
J'ai crée pour celà une **Entry** où l'utilisateur doit rentrer le numéro de bus à supprimer. Une fois saisi, il suffit d'appuyer sur le bouton **suppression bus** et toute la ligne correspondant à ce numéro sera supprimer dans la base de données.

# 2. **Choix techniques**

J'ai utlisé TKinter pour l'interface graphique. J'ai privilégié le choix de différentes fonctions indépendantes afin de pouvoir les associer plus facilement à mes boutons.

La connection à la base de données s'est faite gràce à **mysql connector**.
La base de données est constituée de 3 tables principales: "arret", "bus", "lignes" et d'une table intermédiare "arret_ligne"


![images 3](https://github.com/celine29730/Breizhibus/blob/main/sh%C3%A9ma_bdd_breizhibus.png)


# 3. **Difficultés**
* La première difficulté a résidé dans la structure du code. le fait d'utiliser différentes fonctions m'a paru la slolution la plus simple à mon niveau.

* La difficulté majeure pour l'interface graphique a eté de pouvoir entrer des paramètres dans ma fonction pour la commande de mon bouton **"liste des arrêts"**. j'ai découvert la fonction temporarire **lambda** qui m'a permis de résoudre ce problème.
Le site suivant m'a beaucoup aidé [fonction lambda](https://www.delftstack.com/fr/howto/python-tkinter/how-to-pass-arguments-to-tkinter-button-command/)!














