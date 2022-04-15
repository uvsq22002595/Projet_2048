#############################################
# Groupe MI TD 03
# Bertrand Noah
# Wickramasinghe  Adipthya Iduwara
# https://github.com/uvsq22002595/Projet_2048
#############################################

import tkinter as tk

racine = tk.Tk()
racine.title("Jeu 2048")


# Variables
HAUTEUR = 600
LARGEUR = 600
N = 4
o = 0

x1 = 0
x2 = 0
y1 = 0 
y2 = 0
# Fonction

def creation_grille():
    global N
    grille = []
    Largeur = LARGEUR // N
    Hauteur = HAUTEUR // N
    for i in range(N):
        grille = ([0]*N)
        print(grille)
    for x in range(N):
        for y in range(N):
            x1 = x*Largeur 
            y1 = y*Hauteur
            x2 = (x+1)*Largeur
            y2 = (y+1)*Hauteur
            carre = canvas.create_rectangle((x1,y1), (x2,y2), fill = "red")
            grille[x][y] = carre

# Appelle de fonction
creation_grille()
    

# Fenêtre graphiques
canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR, bg = "white")
bouton_play = tk.Button(racine, text = "Play")
bouton_droit = tk.Button(racine, text = "Right")
bouton_gauche = tk.Button(racine, text = "Left")
bouton_haut = tk.Button(racine, text = "Up")
bouton_bas = tk.Button(racine, text = "Down")
bouton_exit = tk.Button(racine, text = "Finir")
bouton_save = tk.Button(racine, text = "Save")
bouton_load = tk.Button (racine, text = "load")
# Placement des widgets
canvas.grid(column = 1,row = 1, rowspan = 10)
bouton_play.grid(column = 1, row = 11)
bouton_haut.grid(row= 1)
bouton_bas.grid(row = 2)
bouton_gauche.grid(row = 3)
bouton_droit.grid(row= 4)
bouton_exit.grid(row= 5)
bouton_save.grid(row= 6)
bouton_load.grid(row= 7)

racine.mainloop()
