#Bloc02 ->Python Github_Practica01.py  V03

# Importar la llibreria math i la constant PI Alumn@ 26
# L'alumn@ 26 ens explicarà què és la llibreria math i perquè la fem servir

import math
PI = math.pi  

# Àrees i perímetres
# Els números es corresponen amb el número que he assignat a cada figura de la taula
# Els números també es corresponen amb els de l'alumn@ que ha de fer el programa i enviar-lo

def quadrat(): # 1 (figura 1 alumn@ 1 i així fins al 25)
    
def triangle(): # 2
    

def rectangle(): # 3
    

def paralellogram(): # 4
    

def rombe(): # 5
    

def estel(): # 5
    
     
def trapezi(): # 6
    

def cercle(): # 7
    

def poligon(): # 9
    
    

def corona(): # 10
    

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
    
 
def casquet_esferic(): # 23
    
    
def fus_falcaEsferica(): # 24
    
    
def segment_esferic(): # 25

# Els alumnes 27 i 28 buscaran les taules a treballar i comprobaran resultats d'execució
# Programa principal  Alumn@ 27

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
    
    
elif menu == 2 :
    
    
elif menu == 3 :
    
elif menu == 4 : # Alumn@ 30
    
    
elif menu == 5 :
    
    
elif menu == 6 :
    
    
elif menu == 7 :  
    
    
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