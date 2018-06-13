import json
import requests
import os
from datetime import date
from colorama import Back, Style, Fore, init
init(autoreset=True)

opcion=0 #Inicializamos la variable opcion a 0

def menu (opcion):
	print (Fore.RED + Style.BRIGHT +("-------------------------------"))
	print (Fore.RED + Style.BRIGHT +("---MENÚ OPCIONES API FÚTBOL----"))
	print (Fore.RED + Style.BRIGHT +("-------------------------------"))
	print (Fore.CYAN + Style.BRIGHT +("1. Posición y duración del contrato de un jugador del Paris Saint-Germain que pidamos por teclado."))
	print (Fore.CYAN + Style.BRIGHT +("\n2. Mostrar los 3 primeros clasificados de la Bundesliga."))
	print (Fore.CYAN + Style.BRIGHT +("\n3. Edad, precio y nacionalidad de un jugador del Real Betis Balompié."))
	print (Fore.CYAN + Style.BRIGHT +("\n4. Mostrar el nombre de los delanteros del Arsenal FC."))
	print (Fore.CYAN + Style.BRIGHT +("\n5. Mostrar el resultado de un partido de la liga italiana de dos equipos."))
	print (Fore.CYAN + Style.BRIGHT +("\n6. Mostrar los puntos y la posicion de un equipo de la liga portuguesa."))
	print (Fore.CYAN + Style.BRIGHT +("\n7. Mostrar equipo/s de la liga española con mayor número de partidos ganados,perdidos o empatados."))
	print (Fore.CYAN + Style.BRIGHT +("\n8. Vamos a jugar un partido, elige dos equipos de la liga inglesa."))
	print (Fore.CYAN + Style.BRIGHT +("\n9. Salir."))
	opcion = input("\nSelecciona una opción  del menú: ") #Seleccionamos el número y lo asignamos a la variable opción
	return opcion #retornamos el resultado de la opción para trabajar con ella en el bucle while


def posicion (): # Funcion opcion 1 que busca dentro de la API los jugadores que queramos buscar
#busqueda jugador PSG
	response = requests.get('http://api.football-data.org/v1/teams/524/players' ,
	headers={
	"X-Auth-Token": "fe3a09bd5fcc47b0bf29d2645117fe1e",
	"Accept": "application/json"
	}
	)
	data=response.json()
	os.system("cls")
	print(" ")
	print(Back.RED + Style.BRIGHT + "------ Lista de jugadores del PSG que no han ido al Mundial de Rusia -------")
	print(" ")
	for jugador in data["players"]:
		print(Style.BRIGHT + Fore.BLACK + jugador["name"])
	print(" ")
	nombrejugador=str(input("Escribe el nombre de uno de estos jugadores: "))
	for jugador in data["players"]:
		if jugador["name"]==nombrejugador:
			print(" ")
			print("La posición de", Fore.YELLOW + jugador["name"], "es: ", Fore.BLUE + Style.BRIGHT + jugador["position"])
			print(Fore.YELLOW + jugador["name"], "tiene contrato con el PSG hasta: ", Fore.BLUE + Style.BRIGHT + jugador["contractUntil"] )
			print(" ")
def clasi3 (): #Funcion clasi3 que busca dentro de la API los 3 primeros clasificados de la Bundesliga.

	response = requests.get('http://api.football-data.org/v1/competitions/452/leagueTable' ,
	headers={
	"X-Auth-Token": "fe3a09bd5fcc47b0bf29d2645117fe1e",
	"Accept": "application/json"
	}
	)
	data=response.json()

	for equipo in data["standing"]:
		if equipo["position"]==1 or equipo['position']==2 or equipo['position']==3:			
			print(" ")
			print(Back.MAGENTA + Style.BRIGHT + equipo['teamName'])

def betis (): #Esta funcion muestra una lista de jugadores del betis y del que introduzcamos nos dirá su edad, nacionalidad y precio.
	response = requests.get('http://api.football-data.org/v1/teams/90/players' ,
	headers={
	"X-Auth-Token": "fe3a09bd5fcc47b0bf29d2645117fe1e",
	"Accept": "application/json"
	}
	)
	
	data=response.json()
	os.system("cls")
	print(Back.GREEN + Style.BRIGHT + "***************************************************************")
	print(Back.GREEN + Style.BRIGHT + "Lista de jugadores del Betis que no han ido al Mundial de Rusia")
	print(Back.GREEN + Style.BRIGHT + "***************************************************************")
	print(" ")
	for jugador in data["players"]: #Recorremos los jugadores
		print(Style.BRIGHT + Fore.MAGENTA + jugador["name"]) #mostramos la lista de jugadores
	print(" ")
	nombrejugador=str(input("Escribe el nombre de uno de estos jugadores: "))
	for jugador in data["players"]:
		if jugador["name"]==nombrejugador:
			year, month, day = map(int, jugador["dateOfBirth"].split("-")) #esta variable coge la fecha en cadena y le quita el "-"
			fecha_nac = date(year, month, day) #En esta variable ya tenemos la fecha del jugador pasada a formato fecha
			#fecha_nac= datetime.strptime(jugador["dateOfBirth"], '%Y-%m-%d') #otra forma de convertir una cadena a fecha
			diferencia = date.today() - fecha_nac #restamos la fecha actual con la fecha del jugador
			diferencia_dias = diferencia.days # .days convierte el resultado de la resta anterior en días
			edadN = diferencia_dias / 365.2425 #valor gregoriano de un año
			edad = int(edadN) # pasamos la variable anterior que es decimal a entero
			print(" ")
			print("\nLa edad de", Fore.GREEN + jugador["name"], "es de: ",Style.BRIGHT + Fore.YELLOW + str(edad), Fore.YELLOW + Style.BRIGHT + "años.")
			print("\nSu nacionalidad es: ", Style.BRIGHT + Fore.YELLOW + jugador["nationality"] )
			if jugador["marketValue"] is not None:
				print(" ")
				print("\nEl precio de este jugador actualmente es de : ", Fore.YELLOW + Style.BRIGHT + jugador["marketValue"])
			else:
				print(Fore.RED + Back.YELLOW + Style.BRIGHT +"\nEn estos momentos no podemos facilitar el precio del jugador.")			
				print(" ")	

def delanteros (): #Función delantero que nos muestra los delanteros que tiene el equipo del Arsenal.
		
	response = requests.get('http://api.football-data.org/v1/teams/57/players' ,
	headers={
	"X-Auth-Token": "fe3a09bd5fcc47b0bf29d2645117fe1e",
	"Accept": "application/json"
	}
	)
	
	data=response.json()
	for jugador in data["players"]: #Recorremos los jugadores del arsenal
		if jugador["position"] == "Centre-Forward": #El que coincidad con "Centre-Forward"(delantero)
			print(" ")
			print(Back.BLUE + Style.BRIGHT + Fore.YELLOW + jugador["name"]) #nos lo muestra

def serieA (): #Función serieA que nos pide por teclado dos equipos y nos dice el resultado del partido que se ha jugado en casa del primer equipo introducido.
		
	response = requests.get('http://api.football-data.org/v1/competitions/456/fixtures' ,
	headers={
	"X-Auth-Token": "fe3a09bd5fcc47b0bf29d2645117fe1e",
	"Accept": "application/json"
	}
	)
	ligaitaliana='http://api.football-data.org/v1/competitions/456/teams'
	equipos=requests.get(ligaitaliana).json()
	os.system("cls")
	print(Back.BLUE + Style.BRIGHT + "··············································")
	print(Back.BLUE + Style.BRIGHT + "Lista de equipos de la Liga italiana (Serie A)")
	print(Back.BLUE + Style.BRIGHT + "··············································")	
	print(" ")
	for equipo in equipos["teams"]:
		print(Fore.YELLOW + Style.BRIGHT + equipo["name"]) #Mostramos los equipos de la liga italiana
	data=response.json()
	equipolocal=str(input("Introduce el nombre del equipo local: ")) #Pedimos un equipo
	equipovisit=str(input("\nIntroduce el nombre del equipo visitante: ")) #Pedimos otro equipo
	for partido in data["fixtures"]:
		if partido["homeTeamName"] == equipolocal and partido["awayTeamName"] == equipovisit: #Condición: si el nombre del equipo local y el nombre del equipo visitante coincide con el nombre de los equipos, miramos el resultado 
			if partido["result"]["goalsHomeTeam"] > partido["result"]["goalsAwayTeam"]: #Si la diferencia de goles del equipo local es mayor que los goles del equipo visitante, ha ganado
				print(" ")
				print(Fore.GREEN + Style.BRIGHT + "Ha ganado en su campo",equipolocal ,Fore.GREEN + Style.BRIGHT +"por", Fore.MAGENTA + str(partido["result"]["goalsHomeTeam"]),Fore.MAGENTA + "-",Fore.MAGENTA + str(partido["result"]["goalsAwayTeam"]))
				print(" ")
			elif partido["result"]["goalsAwayTeam"] > partido["result"]["goalsHomeTeam"]: #Si el equipo local ha marcado menos goles que el visitante, ha perdido
				print(" ")
				print(Fore.GREEN + Style.BRIGHT + "El",equipolocal ,Fore.GREEN + Style.BRIGHT + "a perdido en su campo por", Fore.MAGENTA + str(partido["result"]["goalsHomeTeam"]),Fore.MAGENTA + "-",Fore.MAGENTA + str(partido["result"]["goalsAwayTeam"]))
				print(" ")
			else:
				print(" ")
				print(Fore.GREEN + Style.BRIGHT + "El resultado del partido es de un empate: ",Fore.MAGENTA + str(partido["result"]["goalsHomeTeam"]),Fore.MAGENTA + "-",Fore.MAGENTA + str(partido["result"]["goalsAwayTeam"]))
				print(" ")

def portuguesa (): #Función liga portuguesa que nos pide un equipo y mostramos la posicion y el número de puntos que tiene.
		
	response = requests.get('http://api.football-data.org/v1/competitions/457/leagueTable' ,
	headers={
	"X-Auth-Token": "fe3a09bd5fcc47b0bf29d2645117fe1e",
	"Accept": "application/json"
	}
	)
	
	data=response.json()
	os.system("cls")
	print(Back.YELLOW + Style.BRIGHT + ".......................................")
	print(Back.YELLOW + Style.BRIGHT + " Lista de equipos de la Liga portuguesa")
	print(Back.YELLOW + Style.BRIGHT + ".......................................")
	print(" ")
	for equipo in data["standing"]:
		print(Style.BRIGHT + Fore.GREEN + equipo["teamName"])
	print("---------------------------------------")
	nombreequipo=str(input("\nIntroduce el nombre de un equipo: "))
	for equipo in data["standing"]:
		if equipo["teamName"]==nombreequipo:
			print(" ")
			print(Fore.MAGENTA + Style.BRIGHT + equipo["teamName"], "ha quedado en la posición", Fore.MAGENTA + str(equipo["position"]), "con", Fore.MAGENTA + str(equipo["points"]), "puntos.")
			print(" ")

def puntos (): #Función puntos que muestra otro menú para comparar el nº de partidos ganados,perdidos o empatados según elijamos. Muestra una lista de equipos que han ganado,perdido o empatado más partidos que el número introducido.	
	response = requests.get('http://api.football-data.org/v1/competitions/455/leagueTable' ,
	headers={
	"X-Auth-Token": "fe3a09bd5fcc47b0bf29d2645117fe1e",
	"Accept": "application/json"
	}
	)
	data=response.json()
	os.system("cls")
	def submenu ():
		print(" ")
		print(Style.BRIGHT + Fore.GREEN + "======= Menú partidos =======\n")
		print(Style.BRIGHT + Fore.MAGENTA + "1. Comparar partidos ganados.")
		print(Style.BRIGHT + Fore.MAGENTA + "2. Comparar partidos perdidos.")
		print(Style.BRIGHT + Fore.MAGENTA + "3. Comparar partidos empatados.")
		print(Style.BRIGHT + Fore.MAGENTA + "4. Salir.")
	submenu()

	opcion=int(input("\nElige una opción: "))
	print(" ")
	while opcion != 4:
		if opcion ==1:
			listaganado=[]
			ganados=int(input("Número de partidos ganados: "))
			for equipo in data["standing"]:
				if equipo["wins"] > ganados:
					listaganado.append(equipo["teamName"])
			if (len(listaganado) > 0):
				print(Style.BRIGHT + Fore.MAGENTA + "\nEquipo/s que han ganado más partidos que el número introducido anteriormente: \n")
				for nombre in listaganado:
					print(Style.BRIGHT + Fore.WHITE + Back.BLUE + (nombre)) 				
			else:	
				print(Style.BRIGHT + Fore.WHITE + Fore.BLUE +"\nNo hay equipos con ese número de partidos ganados.")
					
					
		elif opcion ==2:
			listaperdido=[]
			perdidos=int(input("\nNúmero de partidos perdidos: "))
			for equipo in data["standing"]:
				if equipo["losses"] > perdidos:
					listaperdido.append(equipo["teamName"])
			if len(listaperdido) > 0:
				print(Style.BRIGHT + Fore.CYAN + "\nEquipo/s que han perdido más partidos que el número anteriormente introducido: \n")
				for nombre in listaperdido:
					print(Style.BRIGHT + Fore.WHITE + Back.RED + nombre)
			else:
				print(Style.BRIGHT + Fore.WHITE + Fore.RED +"\nNo hay equipos con ese número de partidos perdidos.")

		elif opcion==3:
			listaempate=[]
			empatados=int(input("Número de partidos empatados: "))
			for equipo in data["standing"]:			
				if equipo["draws"] > empatados:
					listaempate.append(equipo["teamName"])
			if len(listaempate) > 0:
				print(Style.BRIGHT + Fore.RED + "\nEquipo/s que han empaado más partidos que el número anteriormente introducido: \n")
				for nombre in listaempate:
					print(Style.BRIGHT + Fore.WHITE + Back.YELLOW + nombre)
			else:
				print(Style.BRIGHT + Fore.WHITE + Fore.YELLOW + "\nNo hay equipos con ese número de partidos empatados.")

		elif opcion==5:
			submenu()
		else:
			print("\nOpción incorrecta.")
		print(" ")
		opcion=int(input("Elige una opción (5 para mostrar el menú): "))
	print("Hasta pronto!")			


def partido(): #función partido, según la estadística de los puntos y partidos perdidos gana un equipo u otro o se produce un empate.
	response = requests.get('http://api.football-data.org/v1/competitions/445/leagueTable' ,
	headers={
	"X-Auth-Token": "fe3a09bd5fcc47b0bf29d2645117fe1e",
	"Accept": "application/json"
	}
	)
	data=response.json()
	os.system("cls")
	print("===============================")
	print(Back.RED + Style.BRIGHT + Fore.CYAN + "\nLista de equipos Premier League")
	print("===============================")
	print(" ")
	for equipo in data["standing"]:
		print(Style.BRIGHT + Fore.BLUE + Back.WHITE + equipo["teamName"])

	print(" ")
	print(Fore.MAGENTA + "Elige dos equipos de esta liga para que jueguen un partido: \n")
	equipolocal=input("Introduce el primer equipo: ")
	equipovisitante=input("Introduce el segundo equipo: ")
	error=False
	for equipo in data["standing"]:
		if equipo["teamName"]==equipolocal:
			puntoslocal=equipo["points"]
			perdidoslocal=equipo["draws"]
			print("Puntos local: ",puntoslocal, perdidoslocal)
		elif equipo["teamName"]==equipovisitante:
			puntosvisit=equipo["points"]
			perdidosvisit=equipo["draws"]
			print("Puntos visitante:",puntosvisit,perdidosvisit)
		else:
			error=True
	if error:
		input("\nNombre de equipo incorrecto! \nPulse Intro para continuar: ")
		partido()
	else:
		if puntoslocal > puntosvisit and perdidoslocal < perdidosvisit:
			print(Fore.YELLOW + Style.BRIGHT +"\nHa ganado el", Fore.YELLOW + Style.BRIGHT + equipolocal) 
		elif puntoslocal > puntosvisit and perdidoslocal > perdidosvisit:
			print(Fore.YELLOW + Style.BRIGHT + "\nSe ha producido un empate entre estos dos equipos.\n")
		elif puntoslocal > puntosvisit and perdidoslocal == perdidosvisit:
			print(Fore.YELLOW + Style.BRIGHT + "\nHa ganado el", Fore.YELLOW + Style.BRIGHT + equipolocal)
		elif puntoslocal < puntosvisit and perdidoslocal < perdidosvisit:
			print(Fore.YELLOW + Style.BRIGHT + "\nSe ha producido un empate entre estos dos equipos.\n")
		elif puntoslocal < puntosvisit and perdidoslocal > perdidosvisit:
			print(Fore.YELLOW + Style.BRIGHT + "\nHa ganado el", Fore.YELLOW + Style.BRIGHT + equipovisitante)
		elif puntoslocal < puntosvisit and perdidoslocal == perdidosvisit:
			print(Fore.YELLOW + Style.BRIGHT + "\nHa ganado el", Fore.YELLOW + Style.BRIGHT + equipovisitante)
		elif puntoslocal == puntosvisit and perdidoslocal < perdidosvisit:
			print(Fore.YELLOW + Style.BRIGHT +"\nHa ganado el", Fore.YELLOW + Style.BRIGHT + equipolocal)
		elif puntoslocal == puntosvisit and perdidoslocal > perdidosvisit:
			print(Fore.YELLOW + Style.BRIGHT + "\nHa ganado el", Fore.YELLOW + Style.BRIGHT + equipovisitante)
		elif puntoslocal == puntosvisit and perdidoslocal == perdidosvisit:
			print(Fore.YELLOW + Style.BRIGHT + "\nSe ha producido un empate entre estos dos equipos.\n")
"""
Un equipo gana cuando:										
	-Tiene más puntos y menos partidos perdidos
	-Tiene más puntos y el mismo nº de partidos perdidos.
	-Tiene los mismos puntos y menos partidos perdidos.

Un equipo pierde cuando:
	-Tiene menos puntos y mas partidos perdidos.
	-Tiene menos puntos e igual partidos perdidos.
	-Tiene los mismos puntos y más partidos perdidos.

Ocurre un empate cuando:
	-Un equipo tiene más puntos pero mayor nº de partidos perdidos
	-Un equipo tiene menos puntos y menor nº de partidos perdidos
	-Los dos equipos tienen los mismos puntos y los mismo partidos perdidos.
"""
while True:
	# Mostramos el menu sin parar para que el usuario siempre pueda ver las opciones a elegir
	opcion=menu(opcion)
	# solicitamos una opción al usuario
	if opcion=="1": #Condición de la primera opción
		posicion ()
	elif opcion=="2":#Condición de la segunda opción
		os.system("cls")
		print(Fore.YELLOW + Style.BRIGHT + "\nLos tres primeros de la Bundesliga son: ")
		clasi3() #Llamada a la función cancion
		print(" ")
	elif opcion=="3":#Condición de la tercera opción
		betis ()
	elif opcion=="4": #Condición de la cuarta opción
		os.system("cls")
		print(Style.BRIGHT + "Los delanteros del Arsenal son: ")
		delanteros() #Llamada a la función delanteros
		print(" ")
	elif opcion=="5": #Condición de la quinta opción
		serieA() #Llamada a la función serieA
	elif opcion=="6": #Condición de la sexta opción
		portuguesa() #Llamada a la función portuguesa
	elif opcion=="7": #Condición de la séptima opción
		os.system("cls")
		puntos() #Llamada a la función puntos
	elif opcion=="8": #Condición de la octava opción
		partido()
	elif opcion=="9":#Condición de la opción de salir
		print(Fore.GREEN + Style.BRIGHT +("Saliendo de la aplicación..."))
		break #Salimos de la aplicación
	else:
		input(Fore.GREEN + Style.BRIGHT +"No has pulsado ninguna opción correcta...\nPulsa cualquier tecla para continuar") #En caso de no introducir una opción disponible nos muestra un error y vuelve al bucle.

