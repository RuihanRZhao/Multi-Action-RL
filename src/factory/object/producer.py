import string
from typing import Dict, Union

from .material import Material


class Producer:
    def __init__(self,
                 name: string,
                 id: string,
                 produce_range: tuple[int, int],
                 material_list: Dict[string, float],
                 lowest_cost: float = 0,
                 unit_consumption: float = 0
                 ):
        self.ID = id
        self.name = name
        self.produce_range = (produce_range[0], produce_range[1])
        self.material_list: dict = material_list
        self.lowest_period_cost = lowest_cost
        self.unit_consumption = unit_consumption

    def produce(self, amount: float, material_track: list[Material], mode: str):
        if self.produce_range[0] <= amount <= self.produce_range[1]:
            for material in material_track:
                if material in self.material_list:
                    if material.inventory + self.material_list[material.ID] > 0:
                        pass
                    else:
                        raise ValueError(f"Illegal amount produce by using {material.name} in Producer {self.name}")
                else:
                    pass

            if mode is "produce":
                for material in material_track:
                    if material in self.material_list:
                        material.inventory += self.material_list[material.ID]
                return True
            elif mode is "mock":
                return True
            else:
                return False
        else:
            raise ValueError(f"Illegal amount produce by Producer {self.name}")
