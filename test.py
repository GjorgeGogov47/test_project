from Boat_Rental import Boat_Rental
from Boat import Boat
from Customer import Customer

brod1 = Boat("Baja Marine", True)
brod2 = Boat("Belzona Marine", True)

pero = Customer(1000, "CAD", brod1, True)
pero.konverzija()

mile = Customer(100, "BAM", brod2, False)
mile.konverzija()

lista_brodovi = [brod1, brod2]

boat_rental = Boat_Rental(lista_brodovi)
boat_rental.checkout(pero, 'h', 10)
boat_rental.checkout(mile, 'w', 100)
boat_rental.dostapni()


