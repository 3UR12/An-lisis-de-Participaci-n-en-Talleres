# Datos de los talleres (almacenados como conjuntos)
taller1 = {"Ana", "Luis", "Carlos", "Marta"}
taller2 = {"Ana", "Carlos", "Jorge", "Pedro"}
taller3 = {"Luis", "Marta", "Pedro", "Ana"}
taller4 = {"Carlos", "Jorge", "Marta", "Ana"}

#1. Participantes en todos los talleres
#(&) este se llama intersección, su función es devolver los elementos presentes en todos los conjuntos
# en este caso encontrar a quienes asistieron a todos los talleres
todos_talleres = taller1 & taller2 & taller3 & taller4
print("Participantes en todos los talleres:", todos_talleres)  # Imprimir conjunto resultante




#2. Participantes en al menos 2 talleres
#Se crea un conjunto vacío para almacenar los resultados llamado al_menos_2_talleres
#set(), es un conjunto vacío).
al_menos_2_talleres = set()

#(|)<-- eso se llama unión de conjuntos.
#Devuelve un conjunto con todos los elementos únicos presentes en cualquiera de los conjuntos
#combina todos los nombres únicos de los talleres
for persona in taller1 | taller2 | taller3 | taller4:  #se  itera por cada participante único
    #sum para contar los talleres en que aparece cada persona
    talleres_asistidos = sum(persona in taller for taller in [taller1, taller2, taller3, taller4])
    if talleres_asistidos >= 2:  # Si asistió a 2 o más talleres, se añade al conjunto?
        al_menos_2_talleres.add(persona)

# Mostramos los participantes que asistieron a al menos 2 talleres
print("Participantes en al menos 2 talleres:", al_menos_2_talleres)




# 3. Participantes únicos (solo en un taller)
#se crea: un_solo_taller = set() para almacenar los resultados
un_solo_taller = set()

# se usa union de nuevo (|) para cada particiante unico de todos los talleres
for persona in taller1 | taller2 | taller3 | taller4:
    #logica para cortar en cuántos talleres aparece cada persona
    talleres_asistidos = sum(persona in taller for taller in [taller1, taller2, taller3, taller4])
    if talleres_asistidos == 1:  # Si asistió a un solo taller, lo añadimos al conjunto
        un_solo_taller.add(persona)

# Verificamos si hay participantes únicos
if un_solo_taller:  # Si el conjunto no está vacío, lo mostramos
    print("Participantes únicos (solo en un taller):", un_solo_taller)
else:  # Si está vacío, mostramos un mensaje alternativo
    print("Participantes únicos: No se encontraron participantes que hayan asistido solo a un taller.")



#


# 4. Participantes que asistieron al taller 2
# Mostramos directamente el conjunto de participantes del taller 2
print("Participantes en el taller 2:", taller2)