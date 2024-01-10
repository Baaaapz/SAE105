"""
Programme SAE 105: Traitement de données:
Fichier: ville_france.csv contenant des informations sur les 36700 Villes de France
BUT1 : Année 2022-2023
@author: A compléter avec Votre NOM - Prénom - Groupe_TP
"""
# pour afficher la carte avec les villes
"""
import folium,branca
import matplotlib.pyplot as plt
import math
"""

#-----------------------------------------------------------
# Fonction qui extrait les 12 informations sur chaque ville
#-----------------------------------------------------------

def lire_fichier_csv(nomFich):
    """
    Cette fonction permet de LIRE les données du fichier villes_france.csv
    le fait d'utiliser readlines permet de récupérer une liste dont chaque élément correspond à une ville
    ainsi que toutes les données associées
    :param nomFich: fichier "villes_france.csv"
    :return: une liste "liste_villes" dont chaque élément est une str qui comporte toutes les données d'une ville
    (27 données par ville au total)
    """
    fich = open(nomFich,'r')
    liste_villes = fich.readlines()

    print("Fin de l'Extraction des infos du fichier",nomFich)
    fich.close()
    return liste_villes

def extract_info_villes(uneListe):
    """
    Fonction qui extrait les 12 informations de la liste[str] extraite du fichier Excel
    :param : uneListe:
    :return: L: une liste dont chaque élément contient les 12 infos de la ville
    la taille de la liste L[] retournée est de 36700 villes
    """
    L= []
    temp = []
    for i in uneListe:
        temp.append(i.split(','))
    print("taille = ",len(temp))

    """
    Il faut faire attention aux Départements de Corse : 2A et 2B
    et également aux département d'Outre-Mer : 971, 972, ...,977
    """
    for i in temp:
        # eval(..) transforme "Annecy" en Annecy, et "18.59" en 18.59 donc une chaîne de caractères sans les "..."
        # ensuite il faut transformer le type str() en int() ou float()
        # Pour tous les départements sauf la Corse 2A et 2B
        # et les territoires d'Outre-Mer : les derniers champs sont à 'NULL'
        if ((eval(i[1]) != '2A') and (eval(i[1]) != '2B')) and i[25] != 'NULL':
            L.append([int(eval(i[1])),      # numéro du Département
                    eval(i[3]),             # Nom de la ville en MAJUSCULE
                    eval(i[8]),             # Code postal
                    int(eval(i[14])),       # population en 2010
                    int(eval(i[15])),       # population en 1999
                    int(eval(i[16])),       # population en 2012
                    float(eval(i[17])),     # densité
                    float(eval(i[18])),     # surface
                    float(eval(i[19])),     # longitude
                    float(eval(i[20])),     # latitude
                    int(eval(i[25])),       # altitude min
                    int(eval(i[26]))])      # altitude max
        elif i[13] == 'NULL': # pour gérer les départements et territoires d'Outre-Mer : 971, 972, 974, ...
            L.append([int(eval(i[1])),
                      eval(i[3]),
                      eval(i[8]),
                      int(eval(i[14])),
                      int(eval(i[15])),
                      int(eval(i[16])),
                      float(eval(i[17])),
                      float(eval(i[18])),
                      float(eval(i[19])),
                      float(eval(i[20])),
                      "NULL",
                      "NULL"])
        else:
            L.append([eval(i[1]),
                      eval(i[3]),
                      eval(i[8]),
                      int(eval(i[14])),
                      int(eval(i[15])),
                      int(eval(i[16])),
                      float(eval(i[17])),
                      float(eval(i[18])),
                      float(eval(i[19])),
                      float(eval(i[20])),
                      i[25],
                      i[26]])


    return L

#====================================================================
# Compte le Nombre de villes en fonction de l'indicatif téléphonique
#====================================================================
def appelNombre_Villes_Indicatif(indTel, unelisteInfo):
    """
        Fonction qui compte l'ensemble des villes en fonction de l'indicatif téléphonique 
        (01 = Île-de-France, 02 = Nord-Ouest, ...

        :param listeDept: qui est la liste des départements ayant cet indicatif
        :param listeInfo: liste du nom de villes
        :return: nbVilles = nombre de villes
    """
    departements_par_indicatifs = [["CE01", 75,77,78,91,92,93,94,95],
    ["NO02", 14,18,22,27,28,29,35,36,37,41,44,45,49,50,53,56,61,72,76,85,974,976],
    ["NE03", 2,8,10,21,25,39,51,52,54,55,57,58,59,60,62,67,68,70,71,80,88,89,90],
    ["SE04", 1,3,4,5,6,7,11,13,15,"2A","2B",26,30,34,38,42,43,48,63,66,69,73,74,83,84],
    ["SO05", 9,12,16,17,19,23,24,31,32,33,40,46,47,64,65,79,81,82,86,87,971,972,973,975,977,978]]
    listeDept = departements_par_indicatifs[indTel-1]
    nbVilles = extract_villes_depart_indicatif(listeDept, unelisteInfo)
    print(f"nombre de villes pour l'indicatif {indTel} : {nbVilles}")
    return nbVilles

#--------------------------------------------------------
# Fonction extract_villes_depart_indicatif(listeInfo)
#--------------------------------------------------------
def extract_villes_depart_indicatif(listeDept, listeInfo):
    """
    Fonction qui extrait l'ensemble des villes pour chaque département,
    en fonction de l'indicatif téléphonique (01 = Île-de-France, 02 = Nord-Ouest, ...

    :param listeDept: qui est la liste des départements ayant cet indicatif
    :param listeInfo: liste du nom de villes
    :return: nbVilles = nombre de villes
    """
    nbVilles = 0

    with open(f"{listeDept[0]}.txt", 'w') as file:
        for ville in listeInfo:
            if  ville[0] in listeDept:
                nbVilles += 1
                file.write(f"{nbVilles} {ville[1]} {ville[0]}\n")
    return nbVilles

#--------------------------------------------------------
# Procédure qui permet d'appeler la fonction
# qui extrait les informations sur les villes
#---------------------------------------------------------
def appelExtractionVilles():
    print("Extraction des informations des Villes de France")
    listeVillesFr = lire_fichier_csv("villes_france.csv")
    print("une ligne = ",listeVillesFr[0])

    # la liste info contient les 12 Informations retenues pour la suite du programme
    info = extract_info_villes(listeVillesFr)

    return info
#==========================================================
# Recherche les infos d'une Ville dans la liste
#==========================================================
def rechercheVille(name,listeVilles):
    """
    :param name: nom de la ville recherchée doit être en MAJUSCULE
    :param listeVilles: liste de toutes les villes
    :return: listeVilles[i] : la ville recherchée
    """
    index = 0
    while listeVilles[index][1] != name:
        index += 1
    return listeVilles[index]

# --------------------------------------------------------
# Fonction extract_villes_depart_indicatif(listeInfo)
# --------------------------------------------------------
def extract_villes_NumDepart(numDept, listeVilles):
    """
    Fonction qui extrait l'ensemble des villes pour chaque département,
    en fonction du numéro du Département

    :param numDept: numéro du département
    :param listeVilles: liste des noms de villes
    :return: nbVilles = nombre de villes du département
    """
    with open(f"villes_{numDept}.txt", 'a') as file:
        nbVilles = 0
        for ville in listeVilles:
            if str(ville[0]) == str(numDept):
                file.write(str(ville) + '\n')
                nbVilles += 1
    return nbVilles



# ================================================
# Fonctions Utiles pour le Tri Bulle lié à la POPULATION
# ================================================

def Tri_Bulle(liste):
    for i in range(len(liste)-1, 1):
        trie = True
        for j in range(0, i-1):
            if liste[j+1] > liste[j]:
                (liste[j+1], liste[j]) = (liste[j], liste[j+1])
                trie = False
        if trie:
            return liste
    return liste

print(Tri_Bulle([5, 4, 2, 3, 1]))

def MinMax5_villes_Habitants(listeInfoDept, numDep=-1):
    """

    :param numDept:
    :param listeInfoDept:
        traite tout les départements si numDept reste a -1
        recherche de 5 villes ayant le MOINS d'habitants dans un tableau
        recherche de 5 villes ayant le PLUS d'habitants dans un tableau
        on peut trier la liste par ordre croissant
        *** On IMPOSE le TRI BULLE vu au TP7 ****
        puis extraire les 5 premières valeurs
    """
    


#-------------------------------------------------------------------------
# Procédure qui permet d'afficher sur une carte OpenStreetMap
# les 10 villes (5 ayant la population MAX, et 5 ayant la population MIN)
#-------------------------------------------------------------------------
def mapTenVilles(maxPopul, minPopul):
    """

    :param maxPop: fichier contenant les 5 villes de forte densité
    :param minPop: fichier contenant les 5 villes de faible densité
    :return:
    """

    """
        A compléter
    """



def MinMax10Accroissement(lstVillesDepart):
    """
    :param lstVillesDepart:

        recherche de 10 villes ayant la plus FORTE BAISSE de sa population entre 1999 et 2012
        recherche de 10 villes ayant le plus FORT ACCROISSEMENT de sa population entre 1999 et 2012
        on peut trier la liste par ordre croissant
        *** On IMPOSE le TRI BULLE vu au TP7 ****
        puis extraire les 10 premières valeurs et 10 dernières valeurs
    """
"""
    A compléter
"""


def MinMax5Alt_Dept(lstVillesDepart):
    """
    :param lstVillesDepart:

        recherche de 5 villes ayant la plus FAIBLE différence d'altitude dans un tableau
        recherche de 5 villes ayant la plus FORTE différence d'altitude dans un tableau
        on peut trier la liste par ordre croissant
        *** On IMPOSE le TRI BULLE vu au TP7 ****
        puis extraire les 5 premières valeurs
        Numéro du département = lstVillesDepart[0][0]
    """


"""
    A compléter
"""


#-------------------------------------------------------------------------
# Procédure qui permet d'afficher sur une carte OpenStreetMap
# les 10 villes (5 ayant la différence d'ALTITUDE MAX
# et 5 ayant la différence d'ALTITUDE MIN)
#-------------------------------------------------------------------------
def mapTenAlt(maxAlt, minAlt):
    """

    :param maxAlt: fichier contenant les 5 villes de forte différence d'altitude
    :param minAlt: fichier contenant les 5 villes de faible différence d'altitude
    :return:
    """

    """
        A compléter
    """


#===================================================================
# Construction de l'HISTOGRAMME
#===================================================================
def traceHistoVilles(lstVillesDepart):
    """
        A compléter
    """

#====================================================================
# Distance EUCLIDIENNE entre 2 villes (en km)
#====================================================================
def dist_Euclidienne(ville1, ville2):
# Méthode par le calcul de Pythagore
    """
        A compléter
    """

#====================================================================
# Distance GEODESIQUE (surface de la terre) entre 2 villes (en km)
# Formule de Haversine
#====================================================================
def dist_GEOdesique(ville1, ville2):
# calcul par la méthode HAVERSINE
    """
        A compléter
    """

#===============================================================
# ETAPE 5 : Parcours Ville1 ==> Ville2
#===============================================================

#=================================================================
# Recherche un ensemble de villes distante de R km dans une liste
#=================================================================
def ensembleVilles(name, rayon, listeVilles):
    """

    :param name: centre = ville avec les 12 infos
    :param rayon: distance de la ville retenue
    :param listeVilles: liste de toutes les villes
    :return: listeVilles[i] : la ville recherchée
    """


    """
        A compléter
    """

#===================================================================
# ETAPE 5 : Plus court chemin entre les 2 Villes vil1 et vil2
#===================================================================
def parcoursVilles(vil1, vil2, listeRef, rayon):
    """
        A compléter
    """

#----------------------------------------------------------------------------------
# On sauvegarde le trajet dans un fichier html pour l'afficher dans un navigateur
#----------------------------------------------------------------------------------
def map_trajet(villes_traversees):
    """
        A compléter
    """

#===============================================================
# AFFICHE MENU
#===============================================================

def afficheMENU():
    print("\n================ MENU ==================")
    print("taper 1: Nombre de villes en fonction de l'indicatif téléphonique")
    print("taper 2: Extraire des Statistiques des Villes d’un département")
    print("taper 3: Distance Euclidienne et Géodésique entre 2 villes")
    print("taper 4: Plus court chemin entre 2 villes")
    print("F: pour finir")


def afficheSOUS_MENU(unDepartement):
    print("\n================ SOUS MENU : STATISTIQUES du Département ", unDepartement, "==================")
    print("taper 1: Lister les 5 Villes ayant le plus/le moins d'habitants")
    print("taper 2: Afficher les 10 Villes en fonction de la DENSITE sur une carte")
    print("taper 3: Lister les 10 Villes ayant le plus fort/faible taux d'accroissement")
    print("taper 4: HISTOGRAMME des villes par habitants")
    print("taper 5: Lister les 5 Villes ayant la différence d'altitude max/min")
    print("taper 6: Afficher les 10 Villes en fonction de l'ALTITUDE sur une carte")
    print("Q: pour Quitter le sous-menu")


#=============================================================================================
# Programme principal
# Appel de la procédure afficheMENU()
#=============================================================================================

fini = False
while fini == False:
    afficheMENU()
    choix = input("votre choix: ")
    if choix == '1':
        # Pour débuter il faut extraire des informations du fichier CSV
        listeInfo = appelExtractionVilles()
        #=====================================
        indicatif = input("veuillez entrer l'indicatif téléphonique souhaité : ")
        #on vérie que la valeur entrée est valide
        if len(indicatif) == 1 and indicatif.isdigit() and 1 <= int(indicatif) <= 5:
            appelNombre_Villes_Indicatif(int(indicatif), listeInfo)
        else:
            print("Indicatif Invalide")
    elif choix == '2':
        print("\n**** Nombre de Villes par Département *****")
        print("A compléter")
        #=====================================
        finiBis = False
        while finiBis == False:
            # ==> Changer le numéro du Département <==
            afficheSOUS_MENU(74)
            choixBis = input("votre choix: ")
            if choixBis == '1':
                print("\nappel de la stat1 : Min/Max Habitants : 5 villes\n")
                """
                    A compléter
                """
            elif choixBis == '2':
                print("\nappel de la stat2: Afficher les 10 villes (DENSITE) sur la carte\n")
                """
                    A compléter
                """
            elif choixBis == '3':
                print("\nappel de la stat3: ACCROISSEMENT/BAISSE population entre 1999 et 2012\n")
                """
                    A compléter
                """
            elif choixBis == '4':
                print("\nappel de la stat4 : HISTOGRAMME du nombre des Villes par habitants\n")
                """
                    A compléter
                """
            elif choixBis == '5':
                print("\nappel de la stat5 : ALTITUDE Min/Max : 5 villes\n")
                """
                    A compléter
                """
            elif choixBis == '6':
                print("\nappel de la stat6: Afficher les 10 villes (ALTITUDE) sur la carte\n")
                """
                    A compléter
                """
            else:
                finiBis = True
    elif choix == '3':
        print("\nDistance Euclidienne entre 2 villes")
        """
            A compléter
        """

        print("\nDistance Géodésique entre 2 villes")
        """
            A compléter
        """
    elif choix == '4':
        print("\nPLus court chemine entre 2 villes")
        """
            A compléter
        """
        print("*** Traitement terminé, Map réalisée ****")
    elif choix == '5':
        print("\nAppel de la fonction4\n")
    elif choix == 'F':
        fini = True

print("Fin du programme")
