from enum import Enum

class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELETRIC = "eletric"

class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "cocobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"

class Guitar:
    def __init__(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        self.serial_number = serial_number
        self.price = price
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_builder(self):
        return self.builder

    def get_typeg(self):
        return self.typeg

    def get_model(self):
        return self.model

    def get_back_wood(self):
        return self.back_wood

    def get_top_wood(self):
        return self.top_wood
    
class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serialNumber, price, builder, model, typeG, backWood, topWood):
        guitar = Guitar(serialNumber, price, builder, model, typeG, backWood, topWood)
        self.guitars.append(guitar)

    def get_guitar(self, serialNumber):
        for guitar in self.guitars:
            if guitar.getSerialNumber() == serialNumber:
                return guitar
        return None

    def search_guitar(self, searchGuitar):
        matching_guitars = []
        for guitar in self.guitars:
            builder = searchGuitar.get_builder()
            if builder is not None and builder != "" and builder != guitar.get_builder():
                continue
            model = searchGuitar.get_model()
            if model is not None and model != "" and model != guitar.get_model():
                continue
            typeG = searchGuitar.get_typeg()
            if typeG is not None and typeG != "" and typeG != guitar.get_typeg():
                continue
            backWood = searchGuitar.get_back_wood()
            if backWood is not None and backWood != "" and backWood != guitar.get_back_wood():
                continue
            topWood = searchGuitar.get_top_wood()
            if topWood is not None and topWood != "" and topWood != guitar.get_top_wood():
                continue
            matching_guitars.append(guitar)

        return matching_guitars

inventory = Inventory()

inventory.add_guitar("V95693", 1499.95, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
inventory.add_guitar("V956TRRTETRER", 3000.00, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)
inventory.add_guitar("11277", 3999.95, Builder.COLLINGS.value, "Stratocastor", TypeG.ACOUSTIC.value, Wood.INDIAN_ROSEWOOD.value, Wood.INDIAN_ROSEWOOD.value)

whatErinLikes = Guitar(" ", 0, Builder.FENDER.value, "Stratocastor", TypeG.ELETRIC.value, Wood.ALDER.value, Wood.ALDER.value)

found_guitars = inventory.search_guitar(whatErinLikes)
if found_guitars:
    print("Erin, talvez você goste dessas guitarras:")
    for guitar in found_guitars:
        print(f"\n{guitar.get_builder()} {guitar.get_model()} {guitar.get_typeg()} guitar, ela tem:\n{guitar.get_back_wood()} na traseira e laterais e {guitar.get_top_wood()} no tampo.\nEla pode ser sua por apenas US${guitar.get_price()}!")
else:
  print("Desculpe Erin, não temos nada para você")