#Bloc02 ->Python Github_Practica01.py  V03

# Importar la llibreria math i la constant PI Alumn@ 26
# L'alumn@ 26 ens explicarà què és la llibreria math i perquè la fem servir

import math
PI = math.pi  

# Àrees i perímetres
# Els números es corresponen amb el número que he assignat a cada figura de la taula
# Els números també es corresponen amb els de l'alumn@ que ha de fer el programa i enviar-lo

def quadrat(): # 1 (figura 1 alumn@ 1 i així fins al 25    print("Càlcul de l'àrea i del perímetre d'un quadrat ")
    a = float(input("Costat = "))
    area = a * a
    perimetre = 4 * a
    return area, perimetredef triangle(): # 2
    

def rectangle(): # 3
    

def paralellogram(): # 4
    

def rombe(): # 5
    

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 046ce1fce90d4e3da0784d7d21b998f5cfa8f186
def estel(): # 6
    
=======
def estel(): # 5
    print("Càlcul de l'àrea i del perímetre d'un estel ")
    a = float(input("Costat menor a = "))
    b = float(input("Costat major b = "))
    D = float(input("Diagonal major = "))
    d = float(input("Diagonal menor = "))
    area = (D * d) * (1/2)
    perimetre = 2 * (b + a)
    return area, perimetre
>>>>>>> 1f1f3c158bbdcbd99602fcbe076317add8a88bc7
     
def trapezi(): # 7
    

def cercle(): # 8
    

def poligon(): # 9
    
    

def corona(): # 10
    print("Càlcul de l'àrea i del perímetre d'una corona circular ")
    R = float(input("Radi major = "))
    r = float(input("radi menor = "))
    area = PI * (R*R - r*r)
    perimetre = 2 * PI * (R + r)
    return area, perimetre
    
def sector(): # 11
    

# Àrees i volums

def cub(): # 12
   

def cilindre(): # 13
    

def ortoedre(): # 14
    

def prisma_recte(): # 15
    

def con(): # 16
   

def tronc_con(): # 17
   

def esfera(): # 18
    

def piramide(): # 19
   
                  
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

def tronc_piramide(): # 22
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
 
def casquet_esferic(): # 23
    
    
def fus_falcaEsferica(): # 24
    
    
def segment_esferic(): # 25

# Els alumnes 27 i 28 buscaran les taules a treballar i comprobaran resultats d'execució
# Programa principal  Alumn@ 27

print(" Menú -- Mides en unitat donada ")
print("================================")
print("")
print("1. ")
print("2. ")
print("3. ")
print("4. ")
print("5. ")
print("6. ")
print("7. ")
print("8. ")
print("9. ")
print("10. ")
print("11. ")
print("")

print("12. ") # Alumn@ 28
print("13. ")
print("14. ")
print("15. ")
print("16. ")
print("17. ")
print("18. ")
print("19. ")
print("20. ")
print("21. ")
print("22. ")
print("23. ")
print("24. ")
print("25. ")
print("")
print("==============================================")

menu = int(input("escull un element del menú: "))

# Àrees i perímetres  Alumn@ 29

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
    
elif menu == 4 : # Alumn@ 30
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
    

# Àrees i volums Alumn@ 32

elif menu == 12 :
    
    
elif menu == 13 :
    
    
elif menu == 14 :
    
elif menu == 15 :
    
elif menu == 16 : # Alumn@ 33
    
elif menu == 17 :
    
elif menu == 18 :
    
elif menu == 19 :
    
elif menu == 20 :
    
elif menu == 21 : # Alumn@ 34
    
elif menu == 22 :
    
elif menu == 23 :
    
elif menu == 24 :
    
elif menu == 25 :
    

# Git commands Alumn@ 35

# git clone [https:// --- adreça de l'enllaç del codi que us poso tot seguit
# https://github.com/EscolaIndustrial-Programacio/Github_Practica01.git

# El git clone nomes s'ha de fer UNA VEGADA!!!, ja teniu les carpetes al PC

# Si voleu, per tornar a començar, esborreu la carpeta Github_Practica01 sencera...
# ... botó dreta -> Actualizar i torneu a fer un git clone a:

# https://github.com/EscolaIndustrial-Programacio/Github_Practica01.git

# Ara us heu de posar dins la carpeta Github_Practica01, on teniu els arxius
# Seguiu amb la llista de gits que ve tot seguit

# Configuració de correu (vosaltres amb el vostre correu)
# git config -- user.email "josepmaria.bergada@escolaindustrial.org"
# git config -- user.name "nom d'usuari de l'alumn@", el de l'Escola


# git status ( si heu fet modificacions, us marcarà en vermell)
# git add . -> afegeix tots els arxius. Deixa l'espai abans del punt
# git status (ja surten les modificacins en verd)
# git commit -m "elvostreusuari@escolaindustrial.org Cadascu ha de posar el que ha fet sense accents"
# git status
# git push -> pujar al repositori

# Us demanarà un codi:
# Usuari: EscolaIndustrial
# Contrasenya: GithubEscolaIndustrial
# També us pot demanar un codi que us donarà just abans
# git status

# cada alumn@ vetllarà perquè la seva part de codi funcioni


""" Prèviament cada alumn@ haurà programat algunes de les figures
primer amb programació estructurada i després amb programació modular.

Cada alumn@ comprobarà la part de codi que envia des del seu ordinador local
"""