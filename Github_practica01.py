#Bloc02 ->Python Github_Practica01.py V03

# Importar la llibreria math i la constant PI alumn@ 26 Isidro P
# L'alumn@ 26 ens explicarà què és la llibreria math i perquè la fem servir

# math és una llibreria que permet incorporar diverses funcions matemàtiques al programa,
# amb el consegüent estalvi de temps: https://docs.python.org/es/3/library/math.html

import math # importem la llibreria math sencera
PI = math.pi  # creem PI, amb majúscules per conveni, ja que és una constant que no canvia

# Àrees i perímetres
# Els números es corresponen amb el número que he assignat a cada figura de la taula
# Els números també es corresponen amb els de l'alumn@ que ha de fer el programa i enviar-lo
# El número de l'alumnat es correspon amb el seu número de llista
# L'alumnat, un cop acabat el seu enviament, ajudarà al grup



# Àrees i perímetres

def quadrat(): # alumn@ 1 Arnau A
    print("Càlcul de l'àrea i del perímetre d'un quadrat ")
    a = float(input("Costat = "))
    area = a * a
    perimetre = 4 * a
    return area, perimetre

def triangle(): # alumn@ 2 Pau A
    print("Càlcul de l'àrea i del perímetre d'un triangle ")
    a = float(input("Costat a = "))
    b = float(input("Costat b = "))
    c = float(input("Costat c = "))
    base = float(input("Base = "))
    h = float(input("Alçada h = "))
    area = (base * h)* (1/2)
    perimetre = a + b + c
    return area, perimetre

def rectangle(): # alumn@ 3 Oriol A
    print("Càlcul de l'àrea i del perímetre d'un rectangle ")
    a = float(input("Costat a = "))
    b = float(input("Costat b = "))
    area = a * b
    perimetre = 2 * (a + b)
    return area, perimetre

def paralellogram(): # alumn@ 4 Alex A
    print("Càlcul de l'àrea i del perímetre d'un paral·lelogram ")
    a = float(input("Costat major a = "))
    b = float(input("Coatat menor b = "))
    h = float(input("Alçada = "))
    area = b * h
    perimetre = 2 * (a + b)
    return area, perimetre

def rombe(): # alumn@ 5 Adam O
    print("Càlcul de l'àrea i del perímetre d'un rombe ")
    a = float(input("Costat = "))
    D = float(input("Diagonal major = "))
    d = float(input("Diagonal menor = "))
    area = (D * d) * (1/2)
    perimetre = 4 * a
    return area, perimetre

def estel(): # alumn@ 6 Biel B
    print("Càlcul de l'àrea i del perímetre d'un estel ")
    a = float(input("Costat menor a = "))
    b = float(input("Costat major b = "))
    D = float(input("Diagonal major = "))
    d = float(input("Diagonal menor = "))
    area = (D * d) * (1/2)
    perimetre = 2 * (b + a)
    return area, perimetre
     
def trapezi(): # alumn@ 7 Mariona B
    print("Càlcul de l'àrea i del perímetre d'un trapezi")
    B = float(input("Base major B = "))
    b = float(input("Base menor b = "))
    a = float(input("Costat a = "))
    c = float(input("Costat c = "))
    h = float(input("Alçada = "))
    area = (B + b) * h * (1/2)
    perimetre = B + b + a + c
    return area, perimetre

def cercle(): # alumn@ 8 Eric C
    print("Càlcul de l'àrea i del perímetre d'un cercle ")
    radi = float(input("radi = "))
    area = math.pow(radi, 2) * PI
    perimetre = 2 * PI * radi
    return area, perimetre

def poligon(): # alumn@ 9 Pol C
    print("Càlcul de l'àrea i del perímetre d'un polígon ")
    b = float(input("Costat = "))
    costats = float(input("Número de costats = "))
    a = float(input("Apotema = "))
    area = (b * a)/2 * costats
    perimetre = costats * b
    return area, perimetre
    

def corona(): # alumn@ 10 Judit C
    print("Càlcul de l'àrea i del perímetre d'una corona circular ")
    R = float(input("Radi major = "))
    r = float(input("radi menor = "))
    area = PI * (R*R - r*r)
    perimetre = 2 * PI * (R + r)
    return area, perimetre

def sector(): # alumn@ 11 Marc C
    print("Càlcul de l'àrea i del perímetre d'un sector circular ")
    angle = float(input("Angle en graus = "))
    R = float(input("radi = "))
    area = PI * pow(R,2) * angle/360
    perimetre = 2 * PI * R * (1-(angle/360))
    return area, perimetre

# Àrees i volums

def cub(): # alumn@ 12 Imran E
    print("Càlcul de l'àrea i del volum d'un cub ")
    a = float(input("Aresta = "))
    area = 6 * pow(a,2)
    volum = pow(a,3)
    return area, volum

def cilindre(): # alumn@ 13 Joan F
    print("Càlcul de l'àrea i del volum d'un cilindre ")
    R = float(input("Radi = "))
    h = float(input("Alçada = "))
    area = 2 * PI * R * (R + h)
    volum = PI * R*R * h
    return area, volum

def ortoedre(): # alumn@ 14 Pau F
    print("Càlcul de l'àrea i del volum d'un ortoedre ")
    a = float(input("Costat a = "))
    b = float(input("Costat b = "))
    c = float(input("Costat c = "))
    area = 2 * (a * b + a * c + b * c)
    volum = a * b * c
    return area, volum

def prisma_recte(): # alumn@ 15 Adrián de G
    print("Càlcul de l'àrea i del volum d'un prisma recte ")
    a = float(input("Apotema de la base = "))
    c = float(input("Costat = "))
    n = float(input("Número de costats = "))
    h = float(input("Alçada = "))
    area = c * n * (a + h)
    volum = c * a * 0.5 * n * h
    return area, volum

def con(): # alumn@ 16 Ilyas G
    print("Càlcul de l'àrea i del volum d'un con ")
    r = float(input("Radi = "))
    g = float(input("generatriu = "))
    h = float(input("Alçada = "))
    area = PI * r * (r + g)
    volum = PI * pow(r,2) * h
    return area, volum

def tronc_con(): # alumn@ 17 AlexandraElena G
    print("Càlcul de l'àrea i del volum d'un tronc de con" )
    R = float(input("Radi major = "))
    r = float(input("radi menor = "))
    h = float(input("altura = "))
    g = float(input("generatriu = "))
    area = PI * (g * (r+R)+(r*r)+math.pow(R,2))
    volum = PI * h * ((R*R)+(r*r)+(R*r))/3
    return area, volum

def esfera(): # alumn@ 18 Iván J
    print("Càlcul de l'àrea i del volum d'una esfera ")
    r = float(input("radi = "))
    area = 4 * PI * r*r
    volum = (4/3)* PI * pow(r,3)
    return area, volum

def piramide(): # alumn@ 19 Isolda J
    print("Càlcul de l'àrea i del volum d'una piràmide ")
    abase = float(input("Longitud del centre de la base al centre del costat = "))
    acostat = float(input("Longitud del vèrtex al centre del costat = "))
    h = float(input("Alçada = "))
    area = (2*abase) * 4 * (abase + acostat)/2
    volum = pow((2 * abase),2) * h * (1/3)
    return area, volum
                  
def tetraedre_regular(): # alumn@ 20 Lluc J
    print("Càlcul de l'àrea i del volum d'un tetraedre regular ")
    aresta = float(input("aresta = "))
    area = pow(3,0.5) * pow(aresta,2)
    volum = pow(2,0.5) * pow(aresta, 3) * (1/12)
    return area, volum

def octaedre_regular(): # alumn@ 21 Oriol M
    print("Càlcul de l'àrea i del volum d'un octaedre regular ")
    aresta = float(input("aresta = "))
    area = 2 * pow(3, 0.5) * pow(aresta, 2)
    volum = pow(2, 0.5) * pow(aresta, 3) * (1/3)
    return area, volum

def tronc_piramide(): # alumn@ 22 Irina M
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
 
def casquet_esferic(): # alumn@ 23 Pere M
    print("Càlcul de l'àrea i del volum d'un casquet_esfèric ")
    r = float(input("Radi = "))
    h = float(input("Alçada del casquet = "))
    area = 2 * PI * r * h
    volum = PI * h*h * (3 * r - h) * 1/3
    return area, volum
    
def fus_falcaEsferica(): # alumn@ 24 Alex N
    print("Càlcul de l'àrea i del volum d'un fus (falca esfèrica) ")
    angle = float(input("Angle en graus = "))
    r = float(input("Radi = "))
    area = 4 * PI * r*r * angle/360
    volum = 4/3 * PI * pow(r,3) * angle/360
    return area, volum
    
def segment_esferic(): # alumn@ 25 Eduardo O
    print("Càlcul de l'àrea i del volum d'un segment esfèric ")
    h = float(input("Alçada de la zona o segment esfèric = "))
    R = float(input("Radi de l'esfera = "))
    r_gran = float(input("Radi gran del segment = "))
    r_petit = float(input("Radi petit del segment = "))
    area = 2 * PI * R * h
    volum = 1/6 * PI * h * (pow(h,2) + 3 * pow(r_gran,2) + 3 * pow(r_petit,2))
    return area, volum
  
# Programa principal
# Els alumnes 27 i 28 buscaran les taules a treballar i comprobaran resultats d'execució

# Programa principal  Alumn@ 27 OscarAlejandro P

print(" Menú Mides en cm , cm2 i cm3   ")
print("================================")
print("")
print("1. Àrea i perímetre d'un quadrat ")
print("2. Àrea i perímetre d'un triangle ")
print("3. Àrea i perímetre d'un rectangle ")
print("4. Àrea i perímetre d'un paral·lelogram ")
print("5. Àrea i perímetre d'un rombe ")
print("6. Àrea i perímetre d'un estel ")
print("7. Àrea i perímetre d'un trapezi ")
print("8. Àrea i perímetre d'un cercle ")
print("9. Àrea i perímetre d'un polígon regular ")
print("10. Àrea i perímetre d'una corona circular ")
print("11. Àrea i perímetre d'un sector circular ")
print("")
print("12. Àrea i volum d'un cub ") # alumn@ 28 Pau R
print("13. Àrea i volum d'un cilindre ")
print("14. Àrea i volum d'un ortoedre ")
print("15. Àrea i volum d'un prisma recte ")
print("16. Àrea i volum d'un con ")
print("17. Àrea i volum d'un tronc de con ")
print("18. Àrea i volum d'una esfera ")
print("19. Àrea i volum d'una piràmide ")
print("20. Àrea i volum d'un tetraedre regular ")
print("21. Àrea i volum d'un octaedre regular ")
print("22. Àrea i volum d'un tronc de piràmide ")
print("23. Àrea i volum d'un casquet esfèric ")
print("24. Àrea i volum d'un fus -falca esfèrica- ")
print("25. Àrea i volum d'una zona o segment esfèric ")
print("")
print("==============================================")

menu = int(input("escull un element del menú: "))

# Àrees i perímetres alumn@ 29 Jan R

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
    
elif menu == 4 : # alumn@ 30 Anaís S
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
    
elif menu == 8 : # alumn@ 31 Adrià S
    area,perimetre = cercle()
    print("L'àrea és ", area)
    print("El perímetre és: ", perimetre)
    
elif menu == 9 :
    area, perimetre = poligon()
    print("L'àrea és ", area)
    print("El perímetre és ", perimetre)

    """ if menu <= 11:
    print("El perímetre és: ", perimetre)
    elif menu>=12:
    print("El volum és: ", volum)
    """
elif menu == 10 :
    area, perimetre = corona()
    print("L'àrea és ",area)
    print("El perímetre és ",perimetre)
    
elif menu == 11 :
    area, perimetre = sector()
    print("L'àrea és ",area)
    print("El perímetre és ",perimetre)

# Àrees i volums alumn@ 32 Jan S

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
    area, volum = prisma_recte()
    print("L'àrea és ",area)
    print("El volum és ",volum)
elif menu == 16 : # alumn@ 33 Diego V
    area, volum = con()
    print("L'àrea és ",area)
    print("El volum és ",volum)
elif menu == 17 :
    area,volum = tronc_con()
    print("L'àrea és  ", area)
    print("El volum en cm és  ",volum, "cm'3'.")
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
elif menu == 21 : # alumn@ 34 Anna W
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

# Git commands alumn@ 35 Wei Y

# git clone [https:// --- adreça de l'enllaç del codi:
# https://github.com/EscolaIndustrial-Programacio/Github_Practica01.git

# El git clone nomes s'ha de fer UNA VEGADA!!!, ja tenim les carpetes al PC

# Si voleu, per tornar a començar, esborreu la carpeta Github_Practica01 sencera...
# ... botó dreta -> Actualizar i torneu a fer un git clone a:

# https://github.com/EscolaIndustrial-Programacio/Github_Practica01.git

# Ara us heu de posar dins la carpeta Github_Practica01, on teniu els arxius
# Seguiu amb la llista de gits que ve tot seguit

# git pull (recuperar l'estat actual del programa, tal i com es troba al remot)
# Afegiu la vostra part del programa
# Configuració de correu (vosaltres amb el vostre correu)
# Més endavant ja hi posarem l'opció global abans del user per fer-ho només 1 cop:
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

""" Prèviament cada alumn@ haurà programat algunes de les figures
primer amb programació estructurada i després amb programació modular.

Cada alumn@ comprobarà la part de codi que envia des del seu ordinador local
"""

