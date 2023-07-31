

import requests
import tkinter as tk
from tkinter import *


#----------------------------------------------------------------------------------------------------------


# Fonctions pour effectuer les actions sur les vols et les passagers
def get_flights():
    response = requests.get('http://localhost:5000/flights')
    flights = response.json()
    result_text.delete(1.0, tk.END)
    flight_id_entry.delete(0, tk.END)
    airline_entry.delete(0, tk.END)
    departure_entry.delete(0, tk.END)
    arrival_entry.delete(0, tk.END)
    result_text.insert(tk.END, f"Liste des vols : {flights}")


def get_flight():
#    flightsuite de la réponse :

    flight_id = flight_id_entry.get()
    response = requests.get(f'http://localhost:5000/flights/{flight_id}')
    if response.status_code == 200:
        flight = response.json()
        result_text.delete(1.0, tk.END)
        flight_id_entry.delete(0, tk.END)
        airline_entry.delete(0, tk.END)
        departure_entry.delete(0, tk.END)
        arrival_entry.delete(0, tk.END)
        result_text.insert(tk.END, f"Informations du vol {flight_id} : {flight}")
    else:
        result_text.delete(1.0, tk.END)
        flight_id_entry.delete(0, tk.END)
        airline_entry.delete(0, tk.END)
        departure_entry.delete(0, tk.END)
        arrival_entry.delete(0, tk.END)
        result_text.insert(tk.END, f"Le vol {flight_id} n'existe pas.")


def add_flight():
    flight_data = {
        "id": int(flight_id_entry.get()),
        "compagnie": str(airline_entry.get()),
        "depart": str(departure_entry.get()),
        "arrivée": str(arrival_entry.get())
    }
    response = requests.post('http://localhost:5000/flights', json=flight_data)
    if response.status_code == 200:
        flight = response.json()
        result_text.delete(1.0, tk.END)
        flight_id_entry.delete(0, tk.END)
        airline_entry.delete(0, tk.END)
        departure_entry.delete(0, tk.END)
        arrival_entry.delete(0, tk.END)
        result_text.insert(tk.END, "Le vol a été ajouté avec succès. ID du vol :" + str({flight_data['id']}))
    else:
        result_text.delete(1.0, tk.END)
        flight_id_entry.delete(0, tk.END)
        airline_entry.delete(0, tk.END)
        departure_entry.delete(0, tk.END)
        arrival_entry.delete(0, tk.END)
        result_text.insert(tk.END, "Erreur lors de l'ajout du vol.")


def update_flight():
    flight_id = int(flight_id_entry.get())
    flight_data = {
        "compagnie": str(airline_entry.get()),
        "depart": str(departure_entry.get()),
        "arrivée": str(arrival_entry.get())
    }
    response = requests.put(f'http://localhost:5000/flights/{flight_id}', json=flight_data)
    if response.status_code == 200:
        result_text.delete(1.0, tk.END)
        flight_id_entry.delete(0, tk.END)
        airline_entry.delete(0, tk.END)
        departure_entry.delete(0, tk.END)
        arrival_entry.delete(0, tk.END)
        result_text.insert(tk.END, f"Les informations du vol {flight_id} ont été modifiées avec succès.")
    else:
        result_text.delete(1.0, tk.END)
        flight_id_entry.delete(0, tk.END)
        airline_entry.delete(0, tk.END)
        departure_entry.delete(0, tk.END)
        arrival_entry.delete(0, tk.END)
        result_text.insert(tk.END, f"Le vol {flight_id} n'existe pas.")


def delete_flight():
    flight_id = int(flight_id_entry.get())
    response = requests.delete(f'http://localhost:5000/flights/{flight_id}')
    if response.status_code == 200:
        result_text.delete(1.0, tk.END)
        flight_id_entry.delete(0, tk.END)
        airline_entry.delete(0, tk.END)
        departure_entry.delete(0, tk.END)
        arrival_entry.delete(0, tk.END)
        result_text.insert(tk.END, f"Le vol {flight_id} a été supprimé avec succès.")
    else:
        result_text.delete(1.0, tk.END)
        flight_id_entry.delete(0, tk.END)
        airline_entry.delete(0, tk.END)
        departure_entry.delete(0, tk.END)
        arrival_entry.delete(0, tk.END)
        result_text.insert(tk.END, f"Le vol {flight_id} n'existe pas.")


def get_passengers():
    response = requests.get('http://localhost:5000/passengers')
    passengers = response.json()
    result_text.delete(1.0, tk.END)
    name_entry.delete(0, tk.END)
    passenger_id_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    flight_id_entry_2.delete(0, tk.END)
    result_text.insert(tk.END, f"Liste des passagers : {passengers}")


def get_passenger():
    passenger_id = passenger_id_entry.get()
    response = requests.get(f'http://localhost:5000/passengers/{passenger_id}')
    if response.status_code == 200:
        passenger = response.json()
        result_text.delete(1.0, tk.END)
        name_entry.delete(0, tk.END)
        passenger_id_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        flight_id_entry_2.delete(0, tk.END)
        result_text.insert(tk.END, f"Informations du passager {passenger_id} : {passenger}")
    else:
        result_text.delete(1.0, tk.END)
        name_entry.delete(0, tk.END)
        passenger_id_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        flight_id_entry_2.delete(0, tk.END)
        result_text.insert(tk.END, f"Le passager {passenger_id} n'existe pas.")


def add_passenger():
    passenger_data = {
        "id": int(passenger_id_entry.get()),
        "name": str(name_entry.get()),
        "email": str(email_entry.get()),
        "phone": int(phone_entry.get()),
        "flight_id": int(flight_id_entry_2.get())
    }
    response = requests.post('http://localhost:5000/passengers', json=passenger_data)
    if response.status_code == 200:
        passenger = response.json()
        result_text.delete(1.0, tk.END)
        name_entry.delete(0, tk.END)
        passenger_id_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        flight_id_entry_2.delete(0, tk.END)
        result_text.insert(tk.END, "Le passager a été ajouté avec succès. ID du passager : " + str({passenger_data['id']}))
    else:
        result_text.delete(1.0, tk.END)
        name_entry.delete(0, tk.END)
        passenger_id_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        flight_id_entry_2.delete(0, tk.END)
        result_text.insert(tk.END, "Erreur lors de l'ajout du passager.")


def update_passenger():
    passenger_id = int(passenger_id_entry.get())
    passenger_data = {
        "name": str(name_entry.get()),
        "email": str(email_entry.get()),
        "phone": int(phone_entry.get()),
        "flight_id": int(flight_id_entry_2.get())
    }
    response = requests.put(f'http://localhost:5000/passengers/{passenger_id}', json=passenger_data)
    if response.status_code == 200:
        result_text.delete(1.0, tk.END)
        name_entry.delete(0, tk.END)
        passenger_id_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        flight_id_entry_2.delete(0, tk.END)
        result_text.insert(tk.END, f"Les informations du passager {passenger_id} ont été modifiées avec succès.")
    else:
        result_text.delete(1.0, tk.END)
        name_entry.delete(0, tk.END)
        passenger_id_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        flight_id_entry_2.delete(0, tk.END)
        result_text.insert(tk.END, f"Le passager {passenger_id} n'existe pas.")

def delete_passenger():
    passenger_id = int(passenger_id_entry.get())
    response = requests.delete(f'http://localhost:5000/passengers/{passenger_id}')
    if response.status_code == 200:
        result_text.delete(1.0, tk.END)
        name_entry.delete(0, tk.END)
        passenger_id_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        flight_id_entry_2.delete(0, tk.END)
        result_text.insert(tk.END, f"Le passager {passenger_id} a été supprimé avec succès.")
    else:
        result_text.delete(1.0, tk.END)
        name_entry.delete(0, tk.END)
        passenger_id_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        flight_id_entry_2.delete(0, tk.END)
        result_text.insert(tk.END, f"Le passaager {passenger_id} n'existe pas.")


#------------------------------------------------------------------------------------------------------
# Création de la fenêtre principale
window = tk.Tk()
window.title("Gestion de vols et de passagers")


#Personnaliser la fenetre
#window.geometry("1080x720")
#window.minsize(480,360)
window.iconbitmap("g.ico")
window.config(background='#4065A4')

#Création de la frame principale
frame = Frame(window, bg='#4065A4')





# Création des widgets pour la section "Vols"
flights_label = tk.Label(window, text="Vols", font=("Arial", 16), bg='#4065A4', fg='black')
flights_label.grid(row=0, column=0, columnspan=2)

#label_title1 = Label(left_frame, text="Saisir le texte", font=("Helvetica", 18), bg='#4065A4', fg='white')
#label_title1.pack()
flight_id_label = tk.Label(window, text="ID de vol :", fg='black')
flight_id_label.grid(row=1, column=0)

#message11 = Entry(left_frame, font=("Helvetica", 18), bg='#4065A4', fg='black')
flight_id_entry = tk.Entry(window, font=("Helvetica", 11), bg='#4065A4', fg='black')
flight_id_entry.grid(row=1, column=1)

airline_label = tk.Label(window, text="Compagnie aérienne :")
airline_label.grid(row=2, column=0)

airline_entry = tk.Entry(window, font=("Helvetica", 11), bg='#4065A4', fg='black')
airline_entry.grid(row=2, column=1)

departure_label = tk.Label(window, text="Aéroport de départ :")
departure_label.grid(row=3, column=0)

departure_entry = tk.Entry(window, font=("Helvetica", 11), bg='#4065A4', fg='black')
departure_entry.grid(row=3, column=1)

arrival_label = tk.Label(window, text="Aéroport d'arrivée :")
arrival_label.grid(row=4, column=0)

arrival_entry = tk.Entry(window, font=("Helvetica", 11), bg='#4065A4', fg='black')
arrival_entry.grid(row=4, column=1)

get_flights_button = tk.Button(window, text="Liste des vols", bg='#4065A4', fg='black', command= get_flights)
get_flights_button.grid(row=5, column=0)

get_flight_button = tk.Button(window, text="Informations d'un vol", bg='#4065A4', fg='black', command= get_flight)
get_flight_button.grid(row=5, column=1)

add_flight_button = tk.Button(window, text="Ajouter un vol", bg='#4065A4', fg='black', command=add_flight)
add_flight_button.grid(row=6, column=0)

update_flight_button = tk.Button(window, text="Modifier un vol", bg='#4065A4', fg='black', command=update_flight)
update_flight_button.grid(row=6, column=1)

delete_flight_button = tk.Button(window, text="Supprimer un vol", bg='#4065A4', fg='black', command=delete_flight)
delete_flight_button.grid(row=7, column=0)

# Création des widgets pour la section "Passagers"
passengers_label = tk.Label(window, text="Passagers", font=("Arial", 16), bg='#4065A4', fg='black')
passengers_label.grid(row=8, column=0, columnspan=2)

passenger_id_label = tk.Label(window, text="ID de passager :")
passenger_id_label.grid(row=9, column=0)

passenger_id_entry = tk.Entry(window, font=("Helvetica", 11), bg='#4065A4', fg='black')
passenger_id_entry.grid(row=9, column=1)

name_label = tk.Label(window, text="Nom :")
name_label.grid(row=10, column=0)

name_entry = tk.Entry(window, font=("Helvetica", 11), bg='#4065A4', fg='black')
name_entry.grid(row=10, column=1)

email_label = tk.Label(window, text="Email :")
email_label.grid(row=11, column=0)

email_entry = tk.Entry(window, font=("Helvetica", 11), bg='#4065A4', fg='black')
email_entry.grid(row=11, column=1)

phone_label = tk.Label(window, text="Téléphone :")
phone_label.grid(row=12, column=0)

phone_entry = tk.Entry(window, font=("Helvetica", 11), bg='#4065A4', fg='black')
phone_entry.grid(row=12, column=1)

flight_id_label_2 = tk.Label(window, text="ID de vol :")
flight_id_label_2.grid(row=13, column=0)

flight_id_entry_2 = tk.Entry(window, font=("Helvetica", 11), bg='#4065A4', fg='black')
flight_id_entry_2.grid(row=13, column=1)

get_passengers_button = tk.Button(window, text="Liste des passagers", bg='#4065A4', fg='black', command=get_passengers)
get_passengers_button.grid(row=14, column=0)

get_passenger_button = tk.Button(window, text="Informations d'un passager", bg='#4065A4', fg='black', command=get_passenger)
get_passenger_button.grid(row=14, column=1)

add_passenger_button = tk.Button(window, text="Ajouter un passager", bg='#4065A4', fg='black', command=add_passenger)
add_passenger_button.grid(row=15, column=0)

update_passenger_button = tk.Button(window, text="Modifier un passager", bg='#4065A4', fg='black', command=update_passenger)
update_passenger_button.grid(row=15, column=1)

delete_passenger_button = tk.Button(window, text="Supprimer un passager", bg='#4065A4', fg='black', command=delete_passenger)
delete_passenger_button.grid(row=16, column=0)

# Widget pour afficher les résultats
result_text = tk.Text(window, height=10, width=55)
result_text.grid(row=17, column=0, columnspan=2)


