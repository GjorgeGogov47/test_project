from Boat import Boat
from Customer import Customer

class Boat_Rental:
    def __init__(self, brodovi):
        self.brodovi = brodovi
    
    def dostapni(self):
        for brod in self.brodovi:
            if brod.is_available():
                print("Modelot " + brod.model + " e dostapen.")
    
    def checkout(self, customer, izbor, vreme):
        if izbor=='h':
            customer.rent_h(vreme)

            for brod in self.brodovi:
                if brod.model==customer.boat_model.model:
                    brod.availability = True
            
        elif izbor=='d':
            customer.rent_d(vreme)

            for brod in self.brodovi:
                if brod.model==customer.boat_model.model:
                    brod.availability = True
            
        elif izbor=='w':
            customer.rent_w(vreme)

            for brod in self.brodovi:
                if brod.model==customer.boat_model.model:
                    brod.availability = True
            
        else:
            print("Invalid input.")
