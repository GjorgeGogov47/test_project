import requests
import json

class Customer:
    def __init__(self, funds, valuta, boat_choice, diskont):
        if boat_choice.is_available():
            self.funds = funds
            self.valuta = valuta
            self.boat_choice = boat_choice
            self.diskont = diskont
            self.konvertiran = False
            print("Boat model: " + boat_choice.model + " is taken.")
        else:
            print("Boat model: " + boat_choice.model + " is unavailable.")
            return None
        
    # Disclaimer: 
    # Мислам дека поефикасно ќе беше конверзијата да се вршеше директно 
    # во конструкторот, ама мислам дека има повеќе смисла да е во функција. 
    def konverzija(self):
        if self.valuta=='EUR':
            self.konvertiran=True
            return
        else:
            key = {"api_key": "98292b403986363abec14c39dc2889e0"} 
            endpoint="https://api.currencyscoop.com/v1/convert?from=" + self.valuta + "&to=EUR&amount=" + str(self.funds)
            konverz = json.loads(requests.get(endpoint,key).text)
            evra = konverz["response"]["value"]
            self.funds=evra
            self.konvertiran=True
    
    def rent_h(self, casovi):
        self.boat_choice.availability=False
        cena = casovi * 10
        if self.diskont:
            cena = cena - (cena * .30)
        
        if self.funds < cena:
            print("Insufficient funds.")
        elif not(self.konvertiran):
            print("Unconverted currency.")
        elif self.funds >= cena and self.konvertiran:
            self.funds = self.funds - cena
            print("Boat successfully rented.")
    
    def rent_d(self, denovi):
        self.boat_choice.availability=False
        cena = denovi * 150
        if self.diskont:
            cena = cena - (cena * .30)
        
        if self.funds < cena:
            print("Insufficient funds.")
        elif not(self.konvertiran):
            print("Unconverted currency.")
        elif self.funds >= cena and self.konvertiran:
            self.funds = self.funds - cena
            print("Boat successfully rented.")
    
    def rent_w(self, nedeli):
        self.boat_choice.availability=False
        cena = nedeli * 500
        if self.diskont:
            cena = cena - (cena * .30)
        
        if self.funds < cena:
            print("Insufficient funds.")
        elif not(self.konvertiran):
            print("Unconverted currency.")
        elif self.funds >= cena and self.konvertiran:
            self.funds = self.funds - cena
            print("Boat successfully rented.")
