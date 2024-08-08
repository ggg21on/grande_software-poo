from utils.enums import Builder, Style, TypeG, Wood
from utils.instrument_spec import InstrumentSpec

class MandolinSpec(InstrumentSpec):
    def __init__(
        self,
        builder: Builder,
        model: str,
        typeg: TypeG,
        back_wood: Wood,
        top_wood: Wood,
        style: Style,
    ):
        super().__init__(builder, model, typeg, back_wood, top_wood)
        self.style = style

    def get_style(self) -> Style:
        return self.style

    def matches(self, other_spec) -> bool:
        if not isinstance(other_spec, MandolinSpec):
            return False

        if self.builder != other_spec.get_builder():
            return False
        if self.model and self.model.lower() != other_spec.get_model().lower():
            return False
        if self.typeg != other_spec.get_typeg():
            return False
        if self.back_wood != other_spec.get_back_wood():
            return False
        if self.top_wood != other_spec.get_top_wood():
            return False
        if self.style != other_spec.get_style():
            return False

        return True