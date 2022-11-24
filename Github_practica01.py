#Bloc02 ->Python Github_Practica01.py  V03

# Importar la llibreria math i la constant PI Alumn@ 26 IsidroP
# L'alumn@ 26 ens explicarà què és la llibreria math i perquè la fem servir


import math # La llibrería math proporciona accés a les funcions matemàtiques definides per l'estàndard C. L'utilitzem per fer les funcions matemàtiques bàsiques.
PI = math.pi  # math.pi es el numero pi es a dir 3,14... dins la llibreria math.
# També utilitzem math.pow que fa retornar el valor de x elevat a la potència y.

# Àrees i perímetres
# Els números es corresponen amb el número que he assignat a cada figura de la taula
# Els números també es corresponen amb els de l'alumn@ que ha de fer el programa i enviar-lo
# El número de l'alumnat es correspon amb el seu número de llista

def quadrat(): # 1 Arnau A
    a = float(input("Costat = "))
    area = a * a
    perimetre = 4 * a
    return area, perimetre

def triangle(): # 2 Pau A
    h = float(input("Quan mesura l'altura?"))
    a = float(input("Quan mesura un costat?"))
    b = float(input("Quan mesura la base?"))
    c = float(input("Quan mesura el costat que falta?"))
    area = b*h/2
    perimetre = a+b+c
    return area, perimetre
    

def rectangle(): # 3
    

def paralellogram(): # 4
    print("Càlcul de l'àrea i del perímetre d'un rectangle ")
    a = float(input("Costat a = "))
    b = float(input("Costat b = "))
    h = float(input("Alçada = "))
    area = a*b
    perimetre = 2 * (a + b)
    return area, perimetre

def rombe(): # 5
    

<<<<<<< HEAD
def estel(): # 6
    
=======

def estel(): # 6 Biel B.
    print("Càlcul de l'àrea i del perímetre d'un estel ")
    a = float(input("Costat menor a = "))
    b = float(input("Costat major b = "))
    D = float(input("Diagonal major = "))
    d = float(input("Diagonal menor = "))
    area = (D * d) * (1/2)
    perimetre = 2 * (b + a)
    return area, perimetre

>>>>>>> b72706da70c6c136e6b3f088d33c946a36b3f18b
     
def trapezi(): # 7 Mariona B
    print("Càlcul de l'àrea i del perímetre d'un trapezi")
    B = float(input("Base major B = "))
    b = float(input("Base menor b = "))
    a = float(input("Costat a = "))
    c = float(input("Costat c = "))
    h = float(input("Alçada = "))
    area = (B + b) * h * (1/2)
    perimetre = B + b + a + c
    return area, perimetre

def cercle(): # 8 Eric.C
    print("Càlcul de l'àrea i del perímetre d'un cercle ")
    radi = float(input("radi = "))
    area = math.pow(radi, 2) * PI
    perimetre = 2 * PI * radi
    return area, perimetre

def poligon(): # 9 PolC
    print("Càlcul de l'àrea i del perímetre d'un polígon ")
    b = float(input("Costat = "))
    costats = float(input("Número de costats = "))
    a = float(input("Apotema = "))
    area = (b * a)/2 * costats
    perimetre = costats * b
    return area, perimetre
    

def corona(): # 10 Judit C
    print("Càlcul de l'àrea i del perímetre d'una corona circular ")
    R = float(input("Radi major = "))
    r = float(input("radi menor = "))
    area = PI * (R*R - r*r)
    perimetre = 2 * PI * (R + r)
    return area, perimetre
    
def sector(): # 11 Marc C
    print("Càlcul de l'àrea i del perímetre d'un sector circular ")
    angle = float(input("Angle en graus = "))
    R = float(input("radi = "))
    area = PI * pow(R,2) * angle/360
    perimetre = 2 * PI * R * (1-(angle/360))
    return area, perimetre

    

# Àrees i volums

def cub(): #12 Imran EK
    print("Càlcul de l'àrea i del volum d'un cub ")
    a = float(input("Aresta = "))
    area = 6 * pow(a,2)
    volum = pow(a,3)
    return area, volum

def cilindre(): # 13 joan.f 13
    print("Càlcul de l'àrea i del volum d'un cilindre ")
    R = float(input("Radi = "))
    h = float(input("Alçada = "))
    area = 2 * PI * R * (R + h)
    volum = PI * R*R * h
    return area, volum

def ortoedre(): # 14
    

def prisma_recte(): # 15
    

def con(): # 16 Ilyas G
    print("Càlcul de l'àrea i del volum d'un con ")
    r = float(input("Radi = "))
    g = float(input("generatriu = "))
    h = float(input("Alçada = "))
    area = PI * r * (r + g)
    volum = PI * pow(r,2) * h
    return area, volum 
   

def tronc_con(): # 17 AlexandraElenaG
   print("Calcul de l'area i del volum d'un tronc de con" )
    R = float(input("Radi major = "))
    r = float(input("radi menor = "))
    h = float(input("altura = "))
    g = float(input("generatriu = "))
    area = PI * (g * (r+R)+(r*r)+math.pow(R,2))
    volum = PI * h * ((R*R)+(r*r)+(R*r))/3
    return area, volum

def esfera(): # 18
    

def piramide(): # 19
    print("Càlcul de l'àrea i del volum d'una piràmide ")
    abase = float(input("Longitud del centre de la base al centre del costat = "))
    acostat = float(input("Longitud del vèrtex al centre del costat = "))
    h = float(input("Alçada = "))
    area = (2*abase) * 4 * (abase + acostat)/2
    volum = pow((2 * abase),2) * h * (1/3)
    return area, volum
                  
def tetraedre_regular(): # 20
   

def octaedre_regular(): # 21
    A = 0
    V = 0
    try:
        print("Càlcul de l'àrea i del volum d'un octaedre regular ")
        l = float(input("Escriu l'aresta del octaedre regular >> "))
        A = (l**2)*(2*(3**0.5))
        V = (l**3)*(2**0.5)*(1/3)
        return A,V
    except:
        print("Alguna cosa ha anat malament, tornem-ho a intentar!")
        octaedre_regular()

def tronc_piramide(): # 22 Irina M
    print("Càlcul de l'àrea i del volum d'un tronc de piràmide ")
    
    h = float(input("Alçada = "))
    costats = float(input("Número de costats = "))
    a = float(input("Mida de la cara inclinada a = "))
    
    print("Càlcul de l'àrea i del perímetre de la base major ")
    b_gran = float(input("Costat gran = "))
    a1 = float(input("Apotema base gran = "))
    area_major = (b_gran * a1)/2 * costats
    perimetre_major = costats * b_gran
    
    print("Càlcul de l'àrea i del perímetre de la base menor ")
    b_petit = float(input("Costat petit = "))
    a2 = float(input("Apotema base petita = "))
    area_menor = (b_petit * a2)/2 * costats
    perimetre_menor = costats * b_petit
    
    area  = (0.5 * (perimetre_major + perimetre_menor) * a) + area_major + area_menor
    volum = (area_major + area_menor + pow(area_major * area_menor , 1/2)) * h * 1/3
    
    return area, volum
 
def casquet_esferic(): # 23 Pere M.
    print("Càlcul de l'àrea i del volum d'un casquet_esfèric ")
    r = float(input("Radi = "))
    h = float(input("Alçada del casquet = "))
    area = 2 * PI * r * h
    volum = PI * h*h * (3 * r - h) * 1/3
    return area, volum    
    
def fus_falcaEsferica(): # 24
    
    
def segment_esferic(): # 25 Eduardo O.
    print("Càlcul de l'àrea i del volum d'un segment esfèric ")
    h = float(input("Alçada de la zona o segment esfèric = "))
    R = float(input("Radi de l'esfera = "))
    r_gran = float(input("Radi gran del segment = "))
    r_petit = float(input("Radi petit del segment = "))
    area = 2 * PI * R * h
    volum = 1/6 * PI * h * (pow(h,2) + 3 * pow(r_gran,2) + 3 * pow(r_petit,2))
    return area, volum
    

# Els alumnes 27 i 28 buscaran les taules a treballar i comprobaran resultats d'execució
# Programa principal  Alumn@ 27 OscarAlejandroP

print(" Menú Mides en cm , cm2 i cm3   ")
print("================================")
print("")
print("1. L'àrea i el perímetre d'un quadrat ")
print("2. L'àrea i el perímetre d'un triangle ")
print("3. L'àrea i el perímetre d'un rectangle ")
print("4. L'àrea i el perímetre d'un paral·lelogram ")
print("5. L'àrea i el perímetre d'un rombe ")
print("6. L'àrea i el perímetre d'un estel ")
print("7. L'àrea i el perímetre d'un trapezi ")
print("8. L'àrea i el perímetre d'un cercle ")
print("9. L'àrea i el perímetre d'un polígon regular ")
print("10. L'àrea i el perímetre d'una corona circular ")
print("11. L'àrea i el perímetre d'un sector circular ")
print("")
print("12. L'àrea i el volum d'un cub ") # Alumne 28 PauR
print("13. L'àrea i el volum d'un cilindre ")
print("14. L'àrea i el volum d'un ortoedre ")
print("15. L'àrea i el volum d'un prisma recte ")
print("16. L'àrea i el volum d'un con ")
print("17. L'àrea i el volum d'un tronc de con ")
print("18. L'àrea i el volum d'una esfera ")
print("19. L'àrea i el volum d'una piràmide ")
print("20. L'àrea i el volum d'un tetraedre regular ")
print("21. L'àrea i el volum d'un octaedre regular ")
print("22. L'àrea i el volum d'un tronc de piràmide ")
print("23. L'àrea i el volum d'un casquet esfèric ")
print("24. L'àrea i el volum d'un fus -falca esfèrica- ")
print("25. L'àrea i el volum d'una zona o segment esfèric ")
print("")
print("==============================================")

menu = int(input("escull un element del menú: "))

# Àrees i perímetres  Alumn@ 29 jan.r

if menu == 1 :
    area, perimetre = quadrat()
    print("L'àrea és ", area)
    print("El perímetre és ", perimetre)
    
elif menu == 2 :
    area, perimetre = triangle()
    print("L'àres és ", area)
    print("El perímetre és ", perimetre)
    
elif menu == 3 :
    area, perimetre = rectangle()
    print("L'àrea és ", area)
    print("El perímetre és ", perimetre)
    
elif menu == 4 : # 30 Anaís S.
    area, perimetre = paralellogram()
    print("L'àrea és ", area)
    print("El perímetre és ", perimetre)
    
elif menu == 5 :
    area, perimetre = rombe()
    print("L'àrea és ", area)
    print("El perímetre és ",perimetre)
    
elif menu == 6 :
    area, perimetre = estel()
    print("L'àrea és ", area)
    print("El perímetre és ",perimetre)
    
elif menu == 7 :  
     area, perimetre = trapezi()
    print("L'àrea és ", area)
    print("El perímetre és ", perimetre)
    
elif menu == 8 : # Alumn@ 31
    
    
elif menu == 9 :
    

   
elif menu == 10 :
    
    
elif menu == 11 :
    

# Àrees i volums Alumn@ 32 JanS

elif menu == 12 :
    area, volum = cub()
    print("L'àrea és ",area)
    print("El volum és ",volum)
    
elif menu == 13 :
    area, volum = cilindre()
    print("L'àrea és ",area)
    print("El volum és ",volum)
    
elif menu == 14 :
    area, volum = ortoedre()
    print("L'àrea és ",area)
    print("El volum és ",volum)
elif menu == 15 :
<<<<<<< HEAD
    
elif menu == 16 : # 33 DiegoV
    area, volum = con()
    print("L'àrea és ",area)
    print("El volum és ",volum)
=======
    area, volum = prisma_recte()
    print("L'àrea és ",area)
    print("El volum és ",volum)
elif menu == 16 : # Alumn@ 33
    
>>>>>>> 62e3fdb612022ac0f320c0a88cb562ddfe5188d7
elif menu == 17 :
    area,volum = tronc_con()
    print("L'àrea és ", area)
    print("El volum en cm és ",volum, "cm'3'.")
elif menu == 18 :
    area, volum = esfera()
    print("L'àrea és ",area)
    print("El volum és ",volum)
elif menu == 19 :
    area, volum = piramide()
    print("L'àrea és ",area)
    print("El volum és ",volum)
elif menu == 20 :
    area, volum = tetraedre_regular()
    print("L'àrea és ",area)
    print("El volum és ",volum)
    
elif menu == 21 : # Alumn@ 34 AnnaW
    area, volum = octaedre_regular()
    print("L'àrea és ",area)
    print("El volum és ",volum)
elif menu == 22 :
    area, volum = tronc_piramide()
    print("L'àrea és ",area)
    print("El volum és ",volum)
elif menu == 23 :
    area, volum = casquet_esferic()
    print("L'àrea és ",area)
    print("El volum és ",volum)
elif menu == 24 :
    area, volum = fus_falcaEsferica()
    print("L'àrea és ",area)
    print("El volum és ",volum)
elif menu == 25 :
    area, volum = segment_esferic()
    print("L'àrea és ",area)
    print("El volum és ",volum)


# Git commands Alumn@ 35 WeihaoY

# git clone [https:// --- adreça de l'enllaç del codi que us poso tot seguit
# https://github.com/EscolaIndustrial-Programacio/Github_Practica01.git

# El git clone nomes s'ha de fer UNA VEGADA!!!, ja teniu les carpetes al PC

# Si voleu, per tornar a començar, esborreu la carpeta Github_Practica01 sencera...
# ... botó dreta -> Actualizar i torneu a fer un git clone a:

# https://github.com/EscolaIndustrial-Programacio/Github_Practica01.git

# Ara us heu de posar dins la carpeta Github_Practica01, on teniu els arxius
# Seguiu amb la llista de gits que ve tot seguit

# git pull (recuperar l'estat actual del programa, tal i com es troba al remot)
# Afegiu la vostra part del programa
# On hi ha el comentari amb el vostre número, poseu per exemple 36 JosepMariaB
# Configuració de correu (vosaltres amb el vostre correu)
# git config -- user.email "elvostreusuari@escolaindustrial.org"
# git config -- user.name "nom d'usuari de l'alumn@", el de l'Escola 


# git status ( si heu fet modificacions, us marcarà en vermell)
# git add . -> afegeix tots els arxius. Deixa l'espai abans del punt
# git status (ja surten les modificacins en verd)
# git commit -m "Nom+inicialcognom + Numero [el vostre]-> "Exemple JosepMariaB Num 36"
# git status
# git push -> pujar al repositori

# Us demanarà un codi:
# Usuari: EscolaIndustrial
# Contrasenya: GithubEscolaIndustrial
# També us pot demanar un codi que us donarà just abans
# git status

# cada alumn@ vetllaà perquè la seva part de codi funcioni
#YO SOY WEIHAO

""" Prèviament cada alumn@ haurà programat algunes de les figures
primer amb programació estructurada i després amb programació modular.

Cada alumn@ comprobarà la part de codi que envia des del seu ordinador local
"""