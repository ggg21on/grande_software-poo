from enum import Enum

class InstrumentSpec:
    def __init__(self, properties=None):
        if properties is None:
            self.properties = {}
        else:
            self.properties = properties.copy()

    def get_property(self, property_name: str) -> str | int | Enum:
        return self.properties.get(property_name)

    @property
    def get_properties(self) -> dict[str, str | int | Enum]:
        return self.properties

    def matches(self, other_spec) -> bool:
        for property_name in other_spec.get_properties:
            if self.properties.get(property_name) != other_spec.get_property(
                property_name
            ):
                return False

        return True