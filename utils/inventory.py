from utils.instrument import Instrument
from utils.instrument_spec import InstrumentSpec

class Inventory:
    def __init__(self):
        self.stock = []

    def save(self, serial_number: str, price: float, spec: InstrumentSpec) -> None:
        instrument = Instrument(serial_number, price, spec)
        self.stock.append(instrument)

    def get(self, serial_number: str) -> Instrument | None:
        for instrument in self.stock:
            if instrument.get_serial_number() == serial_number:
                return instrument

        return None

    def search(self, search_spec: InstrumentSpec) -> list[Instrument] | None:
        results = []

        for instrument in self.stock:
            if instrument.get_spec.matches(search_spec):
                results.append(instrument)

        return results or None