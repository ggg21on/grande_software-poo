from utils.guitar import Guitar

class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number, price, guitar_spec) -> None:
        guitar = Guitar(serial_number, price, guitar_spec)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number) -> Guitar | None:
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar

        return None

    def search(self, search_guitar) -> Guitar | None:
        matching_guitars = []

        for guitar in self.guitars:
            if guitar.get_spec.matches(search_guitar):
                matching_guitars.append(guitar)

        return matching_guitars or None