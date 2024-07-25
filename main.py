from utils.inventory import Inventory
from utils.guitar_spec import GuitarSpec
from utils.enums import Builder, TypeG, Wood

def initializeInventory(inventory) -> None:
    spec1 = GuitarSpec(
        Builder.FENDER, "stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6
    )

    inventory.add_guitar("V95693", 1499.95, spec1)
    inventory.add_guitar("V99999", 1599.95, spec1)

    spec2 = GuitarSpec(
        Builder.MARTIN, "D-18", TypeG.ACOUSTIC, Wood.MAHOGANY, Wood.ADIRONDACK, 6
    )

    inventory.add_guitar("122784", 5495.95, spec2)

def main() -> None:
    inventory = Inventory()
    initializeInventory(inventory)

    whatErinLikes = GuitarSpec(
        Builder.FENDER, "Stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6
    )

    matching_guitars = inventory.search(whatErinLikes)

    if matching_guitars is None:
        print("Desculpe Erin, não temos nada para você")

        return None

    print("Erin, talvez você goste destas: ")
    for i, guitar in enumerate(matching_guitars):
        guitar_spec = guitar.get_spec

        print(
            f"\n{i+1}. Guitarra: {guitar.get_serial_number()} {guitar_spec.get_builder().value} {guitar_spec.get_model()} {guitar_spec.get_typeg().value} guitar:".title(),
            f"\n   - {guitar_spec.get_back_wood().value.capitalize()} na traseira e laterais",
            f"\n   - {guitar_spec.get_top_wood().value.capitalize()} no tampo, com {guitar_spec.get_num_strings()} cordas",
            f"\n   - Ela pode ser sua por apenas US$ {guitar.get_price():.2f}!",
        )

if __name__ == "__main__":
    main()