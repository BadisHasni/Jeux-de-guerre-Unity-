
from datetime import datetime
from exact_cover_x2 import ExactCover
m = []
k = 0

i = 0
Liste1 = [] #liste de liste
Liste_tete = []

with open('./input/entree10.txt', 'r') as fr:
#with open('./input/entree9.txt', 'r') as fr:
#with open('./input/entree3.txt', 'r') as fr:
#with open('./input/entree2.txt', 'r') as fr:
#with open('./input/entree1.txt', 'r') as fr:
#with open('./input/entree0.txt', 'r') as fr:

    #lecture du fichier(les formes initiales et l'entete)
    for ligne in fr:
        if k == 0:
            N = int(ligne)
        elif k == 1:
            M = int(ligne)
        else:
            if ligne.find('#') != -1 and len(m) > 0:
                #print m
                Liste1.append(m)
                #print Liste1
                m = []
                i = 0
            elif ligne.find('fin') == -1 and k > 2:
                j = 0
                for c in list(ligne.strip()):
                    if c != '0' :
                        if c not in Liste_tete:
                            Liste_tete.append(c)
                        m.append((i, j)) # m contient les coordonnée du chaque matrice initiale (A,B,C)
                    j += 1
                i += 1
        k += 1

#Teste si la pièce de puzzle donnée peut être placée dans la grille initiale
def teste_piece(piece):
        
        for x, y in piece:
                if x < 0 or y < 0 or x >= N or y >= M:
                        return False
        return True

#translation d'une piéce donnée
    
def translation_piece(piece, dx, dy):
    
    return [(x + dx, y + dy) for x, y in piece]

# effectuer toutes les transaltions possibles


longeur = len(Liste_tete)
# Liste_tete est utilisé dans l'algorithme  comme première ligne (indice) de la table 0/1
for i in range(N):
    for j in range(M):
        Liste_tete.append('{0},{1}'.format(str(i), str(j))) # on ajoute a liste_tete les coordonnée du matrice finale
        
mat = [] # mat est le tableau 2D de 0 et de 1 utilisé dans l'algorithme 
mat.append(Liste_tete)
k = 0
for m in Liste1:
    
    b = 0
    for y in range(M):
        for x in range(N):
            translater = translation_piece(m, x, y)
            if teste_piece(translater):
                b += 1
                lig = len(Liste_tete) * [0]
                lig[k] = 1
                for u, v in translater:
                    lig[u * M + v + longeur] = 1  # ajouter 1 à une position de remplissage (x, y)
        
                mat.append(lig)
    
    k += 1
               


debut_temps = datetime.now()


puzzle = ExactCover(mat)
mx = [[0 for b in range(M)] for b in range(N)]   # c'est une matrice vide avec hauteur(N) et largeur(M)
#print mx     
nb=0
for sol in puzzle.solve():
    fw =open("output.txt","a");
    fw.write("solution "+str(nb+1)+'\n')
    print "solution "+str(nb+1)
    nb=nb+1
    
    for p in sol:
      # les coordonnée de chaque piece quand va mette dans le matrice final
        for c in p[1:]:
            l = c.split(',') #les cases séparer par virgule(,)
            mx[int(l[0])][int(l[1])] = p[0]  # les position ou b1 les coordonnée de chaque piece et remplir par P[0] (c'est le nom de piéce )
            
    for x in mx:
        print ''.join(map(str,x))
        fw =open("output.txt","w");
        fw.write(''.join(map(str,x))+'\n')

delta = datetime.now() - debut_temps
print "Temps ecoule = " + str(delta.seconds / 60) + "m:" + str(delta.microseconds / 100000) \
    + "s:" + str(delta.microseconds % 100000 / 1000) + "ms"
