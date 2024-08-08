from enum import Enum

from utils.enums import Builder, InstrumentType, Style, Type, Wood
from utils.instrument import Instrument
from utils.instrument_spec import InstrumentSpec
from utils.inventory import Inventory

DIVIDER = f"{'-' * 32}"

def show_instruments(matching_instruments: list[Instrument] | None) -> None:
    if matching_instruments is None:
        print("...\nDesculpe, não temos nada para você\n```")

        return None

    print(DIVIDER)
    print("Talvez você goste desses instrumentos:")
    for i, instrument in enumerate(matching_instruments, 1):
        spec = instrument.get_spec
        instrument_name = spec.get_property("instrument_type").value

        properties = [
            f"   - {property_name.replace('_', ' ').title()}: {property_value.value.capitalize() if isinstance(property_value, Enum) else property_value}"
            for property_name, property_value in spec.get_properties.items()
            if property_name != "instrument_type"
        ]

        print(
            f"\n{i}. {instrument_name}: '{instrument.get_serial_number()}' {spec.get_property('builder').value} {spec.get_property('model')} {spec.get_property('type').value} {instrument_name}:\n".title()
            + "\n".join(properties),
            f"\n   - Ela pode ser sua por apenas R$ {instrument.get_price():.2f}",
        )
    print(DIVIDER)


def initialize_inventory(inventory: Inventory) -> None:
    properties = {
        "instrument_type": InstrumentType.GUITAR,
        "builder": Builder.FENDER,
        "model": "stratocastor",
        "type": Type.ELECTRIC,
        "top_wood": Wood.ALDER,
        "back_wood": Wood.ALDER,
        "num_strings": 6,
    }

    inventory.save("V95693", 1499.97, InstrumentSpec(properties))
    inventory.save("V99999", 2174.49, InstrumentSpec(properties))

    properties = {
        "instrument_type": InstrumentType.GUITAR,
        "builder": Builder.MARTIN,
        "model": "Les Paul",
        "type": Type.ELECTRIC,
        "top_wood": Wood.MAHOGANY,
        "back_wood": Wood.ADIRONDACK,
        "num_strings": 6,
    }

    inventory.save("V22784", 5495.27, InstrumentSpec(properties))

    properties = {
        "instrument_type": InstrumentType.MANDOLIN,
        "builder": Builder.GIBSON,
        "model": "F5-G",
        "type": Type.ACOUSTIC,
        "top_wood": Wood.MAPLE,
        "back_wood": Wood.MAPLE,
        "style": Style.A,
    }

    inventory.save("V73832", 3459.99, InstrumentSpec(properties))

    properties = {
        "instrument_type": InstrumentType.BANJO,
        "builder": Builder.GIBSON,
        "model": "RB-3",
        "type": Type.ACOUSTIC,
        "num_strings": 5,
        "back_wood": Wood.MAPLE,
    }

    inventory.save("V46257", 674.49, InstrumentSpec(properties))
    inventory.save("V85121", 1597.95, InstrumentSpec(properties))


def main() -> None:
    inventory = Inventory()
    initialize_inventory(inventory)

    properties = {
        "builder": Builder.GIBSON,
        "type": Type.ACOUSTIC,
        "back_wood": Wood.MAPLE,
    }
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)

    show_instruments(matching_instruments)

    properties = {
        "builder": Builder.RYAN,
        "model": "Stratocastor",
        "type": Type.ACOUSTIC,
        "top_wood": Wood.CEDAR,
        "back_wood": Wood.SITKA,
    }
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)

    show_instruments(matching_instruments)

    properties = {
        "builder": Builder.MARTIN,
        "type": Type.ELECTRIC,
        "top_wood": Wood.MAHOGANY,
        "back_wood": Wood.ADIRONDACK,
    }
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)

    show_instruments(matching_instruments)

    properties = {
        "type": Type.ELECTRIC,
        "top_wood": Wood.ALDER,
        "num_strings": 6,
    }
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)

    show_instruments(matching_instruments)

    properties = {
        "builder": Builder.OLSON,
        "back_wood": Wood.ADIRONDACK,
        "style": Style.F,
    }
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)

    show_instruments(matching_instruments)

if __name__ == "__main__":
    main()