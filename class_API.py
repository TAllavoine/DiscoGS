import tkinter as tk
from tkinter import ttk
import requests
from requests_oauthlib import OAuth1

class Recherche_Musique:
    def __init__(self, Fenetre):
        self.Fenetre = Fenetre
        self.Fenetre.title("Recherche de Musique")
        self.Fenetre.geometry("400x300")

        # Informations d'authentification OAuth
        self.consumer_key = 'amtStcrgKGmQFzHJvubE'
        self.consumer_secret = 'aaQIgEAcyIXmJKiPzoQCGJJVEuYBfuth'
        self.access_token = 'YOUR_ACCESS_TOKEN'
        self.access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

        # Champ de saisie de texte
        self.entry = tk.Entry(self.Fenetre, width=50)
        self.entry.insert(0, "Entrez un titre ici ...")
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.clear_entry)

        # Bouton de recherche
        self.search_button = ttk.Button(self.Fenetre, text="Rechercher", command=self.search)
        self.search_button.pack(pady=10)

        # Labels pour afficher les résultats
        self.artist_label = tk.Label(self.Fenetre, text="Artiste :")
        self.artist_label.pack(pady=5)

        self.title_label = tk.Label(self.Fenetre, text="Titre :")
        self.title_label.pack(pady=5)

        self.date_label = tk.Label(self.Fenetre, text="Date sortie :")
        self.date_label.pack(pady=5)

    def clear_entry(self, event):
        self.entry.delete(0, tk.END)

    def search(self):
        title = self.entry.get()
        url = f"https://api.discogs.com/database/search?q={title}&type=release"
        auth = OAuth1(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.access_token,
            resource_owner_secret=self.access_token_secret
        )
        headers = {"User-Agent": "Recherche_Musique/1.0"}
        response = requests.get(url, headers=headers, auth=auth)
        data = response.json()

        if 'results' in data and data['results']:
            result = data['results'][0]
            self.artist_label.config(text=f"Artiste : {result.get('artist', 'N/A')}")
            self.title_label.config(text=f"Titre : {result.get('title', 'N/A')}")
            self.date_label.config(text=f"Date sortie : {result.get('year', 'N/A')}")
        else:
            self.artist_label.config(text="Artiste : Aucun résultat")
            self.title_label.config(text="Titre : Aucun résultat")
            self.date_label.config(text="Date sortie : Aucun résultat")

if __name__ == "__main__":
    Fenetre = tk.Tk()
    app = Recherche_Musique(Fenetre)
    Fenetre.mainloop()
