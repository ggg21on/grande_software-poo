from utils.enums import Builder, TypeG, Wood

class GuitarSpec:
    def __init__(self, builder, model, typeg, back_wood, top_wood, num_strings):
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood
        self.num_strings = num_strings

    def get_builder(self) -> Builder:
        return self.builder

    def get_model(self) -> str:
        return self.model

    def get_typeg(self) -> TypeG:
        return self.typeg

    def get_back_wood(self) -> Wood:
        return self.back_wood

    def get_top_wood(self) -> Wood:
        return self.top_wood

    def get_num_strings(self) -> str:
        return self.num_strings

    def matches(self, other_spec) -> bool:
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
        if self.num_strings != other_spec.get_num_strings():
            return False

        return True