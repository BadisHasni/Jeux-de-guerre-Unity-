
from datetime import datetime
from exact_cover_x2 import ExactCover
m = []
k = 0

i = 0
formes = []
header = []

#with open('./input/entree10.txt', 'r') as fr:
#with open('./input/entree9.txt', 'r') as fr:
#with open('./input/entree3.txt', 'r') as fr:
#with open('./input/entree2.txt', 'r') as fr:
#with open('./input/entree1.txt', 'r') as fr:
with open('./input/entree0.txt', 'r') as fr:

    #lecture du fichier sous forme de coordonnées 
    for line in fr:
        if k == 0:
            N = int(line)
        elif k == 1:
            M = int(line)
        else:
            if line.find('#') != -1 and len(m) > 0:
                #print m
                formes.append(m)
               
                m = []
                i = 0
            elif line.upper().find('FIN') == -1 and k > 2:
                j = 0
                for c in list(line.strip()):
                    if '0' != c:
                        if c not in header:
                            header.append(c)
                        m.append((i, j))
                    j += 1
                i += 1
        k += 1

#Teste si la pièce de puzzle donnée peut être placée dans la grille initiale
def fits_in_grid(piece):
        
        for x, y in piece:
                if x < 0 or y < 0 or x >= N or y >= M:
                        return False
        return True

#translation d'une piéce donnée
    
def translate_piece(piece, dx, dy):
    
    return [(x + dx, y + dy) for x, y in piece]
# effectuer toutes les transaltions possibles

all_trans = []

longeur = len(header)
# header est utilisé dans l'algorithme X comme première ligne (indice) de la table 0/1
for i in range(N):
    for j in range(M):
        header.append('{0},{1}'.format(str(i), str(j)))
        
mat = [] # mat est le tableau 2D de 0 et de 1 utilisé dans l'algorithme X
mat.append(header)
k = 0
for m in formes:

    
    count = 0
    for y in range(M):
        for x in range(N):
            trans = translate_piece(m, x, y)
            if fits_in_grid(trans):
                count += 1
                row = len(header) * [0]
                row[k] = 1
                for u, v in trans:
                    row[u * M + v + longeur] = 1  # ajouter 1 à une position de remplissage (x, y)
        
                mat.append(row)
    
    k += 1
               


startTime = datetime.now()


puzzle = ExactCover(mat)
mx = [[0 for count in range(M)] for count in range(N)]
print mx
nb=0
for solution in puzzle.solve():
    fw =open("output.txt","a");
    fw.write("solution "+str(nb+1)+'\n')
    print "solution "+str(nb+1)
    nb=nb+1
    
    for p in solution:
        print p
        for c in p[1:]:
            l = c.split(',')
            mx[int(l[0])][int(l[1])] = p[0]
            
    for x in mx:
        print ''.join(map(str,x))
        fw =open("output.txt","w");
        fw.write(''.join(map(str,x))+'\n')

delta = datetime.now() - startTime
print "Temps ecoule = " + str(delta.seconds / 60) + "m:" + str(delta.microseconds / 100000) \
    + "s:" + str(delta.microseconds % 100000 / 1000) + "ms"
