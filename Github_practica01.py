#Bloc02 ->Python Github_Practica01.py  V03

# Importar la llibreria math i la constant PI Alumn@ 26
# L'alumn@ 26 ens explicarà què és la llibreria math i perquè la fem servir
# La llibrería math proporciona accés a les funcions matemàtiques definides per l'estàndard C. L'utilitzem per fer les funcions matemàtiques bàsiques.
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
>>>>>>> 5b45db3a2bb343e876f3364324fbfcb5370b435e
def estel(): # 6
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 046ce1fce90d4e3da0784d7d21b998f5cfa8f186
def estel(): # 6
    
=======
def estel(): # 5
>>>>>>> 38087740f2cdf39453492f6081d8a1931d2cf2cf
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
    

<<<<<<< HEAD
def cercle(): # 8
=======
<<<<<<< HEAD
def cercle(): # 7
    print("Càlcul de l'àrea i del perímetre d'un cercle ")
    radi = float(input("radi = "))
    area = math.pow(radi, 2) * PI
    perimetre = 2 * PI * radi
    return area, perimetre
=======
def cercle(): # 8
<<<<<<< HEAD
    print("Càlcul de l'àrea i del perímetre d'un cercle ")
    radi = float(input("radi = "))
    area = math.pow(radi, 2) * PI
    perimetre = 2 * PI * radi
    return area, perimetre
=======
>>>>>>> 38087740f2cdf39453492f6081d8a1931d2cf2cf
    
<<<<<<< HEAD
>>>>>>> 5b45db3a2bb343e876f3364324fbfcb5370b435e
=======
>>>>>>> 046ce1fce90d4e3da0784d7d21b998f5cfa8f186
>>>>>>> b820cb2cd834ee863c2d84cb7cb1de8abfd1304f

def poligon(): # 9
    

def corona(): # 10
    print("Càlcul de l'àrea i del perímetre d'una corona circular ")
    R = float(input("Radi major = "))
    r = float(input("radi menor = "))
    area = PI * (R*R - r*r)
    perimetre = 2 * PI * (R + r)
    return area, perimetre
    
def sector(): # 11
    print("Càlcul de l'àrea i del perímetre d'un sector circular ")
    angle = float(input("Angle en graus = "))
    R = float(input("radi = "))
    area = PI * pow(R,2) * angle/360
    perimetre = 2 * PI * R * (1-(angle/360))
    return area, perimetre

    

# Àrees i volums

def cub(): # 12
   

def cilindre(): # 13
    

def ortoedre(): # 14
    

def prisma_recte(): # 15
    

def con(): # 16
   

def tronc_con(): # 17
   

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
print("12. L'àrea i el volum d'un cub ")
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