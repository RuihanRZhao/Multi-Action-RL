import string
from typing import Dict, Union

from .material import Material


class Producer:
    def __init__(self,
                 id: string,
                 produce_min: float,
                 produce_max: float,
                 lowest_cost: float,
                 unit_consumption: float,
                 material_list: list
                 ):
        self.ID = id
        self.produce_range = (produce_min, produce_max)

        self.material_list: list = [ i[1:] for i in material_list ]
        self.lowest_period_cost = lowest_cost
        self.unit_consumption = unit_consumption

    def __repr__(self):
        material_exchange = ""
        for element, cost in self.material_list:
            material_exchange += "\t\t"
            cost = int(cost)
            if cost > 0:
                material_exchange += f"Produce {cost} of {element}"
            elif cost < 0:
                material_exchange += f"Cost {cost} of {element}"
            else:
                raise ValueError(f"Value [{cost}] Not a Number!")

            material_exchange += "\n"

        return f"\nName: [{self.ID}]\n" \
               f"\tProduce range: [{self.produce_range[0]},{self.produce_range[1]}]\n" \
               f"\tLowest cost: {self.lowest_period_cost}  | Unit consumption: {self.unit_consumption}\n\"" \
               f"\tMaterial exchange: \n" \
               f"{material_exchange}"

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

            if mode == "produce":
                for material in material_track:
                    if material in self.material_list:
                        material.inventory += self.material_list[material.ID]
                return True
            elif mode == "mock":
                return True
            else:
                return False
        else:
            raise ValueError(f"Illegal amount produce by Producer {self.name}")
