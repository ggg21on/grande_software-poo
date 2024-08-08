from utils.guitar_spec import GuitarSpec
from utils.instrument import Instrument

class Guitar(Instrument):
    def __init__(self, serial_number: str, price: float, spec: GuitarSpec):
        super().__init__(serial_number, price, spec)