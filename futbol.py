import json
import requests
import os
from datetime import date
from colorama import Back, Style, Fore, init
init(autoreset=True)

opcion=0 #Inicializamos la variable opcion a 0

def menu (opcion):
	print (Fore.RED + Style.BRIGHT +("-------------------------------"))
	print (Fore.RED + Style.BRIGHT +("---MENÚ OPCIONES API FÚTBOL---"))
	print (Fore.RED + Style.BRIGHT +("-------------------------------"))
	print (Fore.CYAN + Style.BRIGHT +("1. Posición y duración del contrato de un jugador del Paris Saint-Germain que pidamos por teclado."))
	print (Fore.CYAN + Style.BRIGHT +("2. Mostrar los 3 primeros clasificados de la Bundesliga."))
	print (Fore.CYAN + Style.BRIGHT +("3. Edad, precio y nacionalidad de un jugador del Real Betis Balompié."))
	print (Fore.CYAN + Style.BRIGHT +("4. Mostrar el nombre de los delanteros del Arsenal FC."))
	print (Fore.CYAN + Style.BRIGHT +("5. Mostrar el resultado de un partido de la liga italiana de dos equipos que pidamos por teclado."))
	print (Fore.CYAN + Style.BRIGHT +("6. Mostrar los puntos y la posicion de un equipo de la liga portuguesa que introduzcamos por teclado."))
	print (Fore.CYAN + Style.BRIGHT +("7. Mostrar el nombre de un equipo de la liga española con partidos(perdidos=1, empatados=2 o ganados=3) con el número que introduzca el usuario."))
	print (Fore.CYAN + Style.BRIGHT +("8. Vamos a jugar un partido, elige dos equipos de la liga inglesa."))
	print (Fore.CYAN + Style.BRIGHT +("9. Salir."))
	opcion = input(Fore.RED + Style.BRIGHT +"Selecciona una opción  del menú: ") #Seleccionamos el número y lo asignamos a la variable opción
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
		print(jugador["name"])
	print(" ")
	nombrejugador=str(input(Fore.GREEN + Style.BRIGHT +"Escribe el nombre de uno de estos jugadores: "))
	for jugador in data["players"]:
		if jugador["name"]==nombrejugador:
			print(" ")
			print("La posición de", Fore.YELLOW + jugador["name"], "es: ", Fore.CYAN + Style.BRIGHT + jugador["position"])
			print(Fore.YELLOW + jugador["name"], "tiene contrato con el PSG hasta: ", Fore.CYAN + Style.BRIGHT + jugador["contractUntil"] )
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

def betis ():
	response = requests.get('http://api.football-data.org/v1/teams/90/players' ,
	headers={
	"X-Auth-Token": "fe3a09bd5fcc47b0bf29d2645117fe1e",
	"Accept": "application/json"
	}
	)
	
	data=response.json()
	os.system("cls")
	print(Back.GREEN + Style.BRIGHT + "------ Lista de jugadores del Betis que no han ido al Mundial de Rusia -------")
	print(" ")
	for jugador in data["players"]:
		print(jugador["name"])
	print(" ")
	nombrejugador=str(input(Fore.GREEN + Style.BRIGHT +"Escribe el nombre de uno de estos jugadores: "))
	for jugador in data["players"]:
		if jugador["name"]==nombrejugador:
			year, month, day = map(int, jugador["dateOfBirth"].split("-"))
			fecha_nac = date(year, month, day)
			#fecha_nac= datetime.strptime(jugador["dateOfBirth"], '%Y-%m-%d')
			diferencia = date.today() - fecha_nac
			diferencia_dias = diferencia.days # .days convierte el resultado de la resta anterior en días
			edadN = diferencia_dias / 365.2425 #valor gregoriano de un año
			edad = int(edadN) # pasamos la variable anterior que es decimal a entero
			print(" ")
			print("La edad de", Fore.YELLOW + jugador["name"], "es de: ", Fore.CYAN + Style.BRIGHT +  str(edad), "años.")
			print("Su nacionalidad es: ", jugador["nationality"] )
			if jugador["marketValue"] is not None:
				print(" ")
				print("El precio de este jugador actualmente es de : ", jugador["marketValue"])
			else:
				print("En estos momentos no podemos facilitar el precio del jugador.")			
				print(" ")	

def delanteros (): #Función delantero que nos muestra los delanteros que tiene el equipo del Arsenal.
		
	response = requests.get('http://api.football-data.org/v1/teams/57/players' ,
	headers={
	"X-Auth-Token": "fe3a09bd5fcc47b0bf29d2645117fe1e",
	"Accept": "application/json"
	}
	)
	
	data=response.json()
	for jugador in data["players"]:
		if jugador["position"] == "Centre-Forward":
			print(" ")
			print(Back.CYAN + Style.BRIGHT + jugador["name"])

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
	print(Back.BLUE + Style.BRIGHT + "------ Lista de equipos de la Liga italiana (Serie A) -------")
	print(" ")
	for equipo in equipos["teams"]:
		print(equipo["name"])
	data=response.json()
	equipolocal=str(input(Style.BRIGHT + Fore.WHITE + "Introduce el nombre del equipo local: "))
	equipovisit=str(input(Style.BRIGHT + Fore.WHITE + "Introduce el nombre del equipo visitante: "))
	for partido in data["fixtures"]:
		if partido["homeTeamName"] == equipolocal and partido["awayTeamName"] == equipovisit:
			if partido["result"]["goalsHomeTeam"] > partido["result"]["goalsAwayTeam"]:
				print(" ")
				print("Ha ganado",equipolocal ,"por", partido["result"]["goalsHomeTeam"], "-", partido["result"]["goalsAwayTeam"])
				print(" ")
			elif partido["result"]["goalsAwayTeam"] > partido["result"]["goalsHomeTeam"]:
				print(" ")
				print("El",equipolocal ,"a perdido por", partido["result"]["goalsHomeTeam"], "-", partido["result"]["goalsAwayTeam"] )
				print(" ")
			else:
				print(" ")
				print("El resultado del partido es de un empate: ", partido["result"]["goalsHomeTeam"],"-", partido["result"]["goalsAwayTeam"])
				print(" ")

def portuguesa (): #Función delantero que nos muestra los delanteros que tiene el equipo del Arsenal.
		
	response = requests.get('http://api.football-data.org/v1/competitions/457/leagueTable' ,
	headers={
	"X-Auth-Token": "fe3a09bd5fcc47b0bf29d2645117fe1e",
	"Accept": "application/json"
	}
	)
	
	data=response.json()
	os.system("cls")
	print(Back.YELLOW + Style.BRIGHT + "------ Lista de equipos de la Liga portuguesa -------")
	print(" ")
	for equipo in data["standing"]:
		print(equipo["teamName"])
	print("---------------------------------------")
	nombreequipo=str(input(Fore.GREEN + Style.BRIGHT + "Introduce el nombre de un equipo: "))
	for equipo in data["standing"]:
		if equipo["teamName"]==nombreequipo:
			print(" ")
			print(Fore.MAGENTA + Style.BRIGHT + equipo["teamName"], "ha quedado en la posición", Fore.MAGENTA + str(equipo["position"]), "con", Fore.MAGENTA + str(equipo["points"]), "puntos.")
			print(" ")

while True:
	# Mostramos el menu sin parar para que el usuario siempre pueda ver las opciones a elegir
	opcion=menu(opcion)
	# solicitamos una opción al usuario
	if opcion=="1": #Condición de la primera opción
		posicion ()
	elif opcion=="2":#Condición de la segunda opción
		os.system("cls")
		print(Fore.BLUE + Style.BRIGHT + "Los tres primeros de la Bundesliga son: ")
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
		portuguesa() #Llamada a la función paises
	elif opcion=="7": #Condición de la séptima opción
		os.system("cls")
		print(Style.BRIGHT + "Los delanteros del Arsenal son: ")
		delanteros() #Llamada a la función paises
	elif opcion=="8": #Condición de la octava opción
		os.system("cls")
		delanteros() #Llamada a la función paises
	elif opcion=="9":#Condición de la opción de salir
		print(Fore.GREEN + Style.BRIGHT +("Saliendo de la aplicación..."))
		break #Salimos de la aplicación
	else:
		input(Fore.GREEN + Style.BRIGHT +"No has pulsado ninguna opción correcta...\nPulsa cualquier tecla para continuar") #En caso de no introducir una opción disponible nos muestra un error y vuelve al bucle.

