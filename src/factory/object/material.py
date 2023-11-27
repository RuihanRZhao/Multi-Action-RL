from typing import Dict, Union
import string


from attributes.permit import Permit


class Material:
    def __init__(self,
                 id: int,
                 name: string = "",
                 inventory: float = 0,
                 inventory_cap: float = 0,
                 pur_permit: bool = False,
                 sal_permit: bool = False,
                 price_source: list | None = None):

        self.raw_data = {
            "ID": id,
            "name": name,
            "inventory": inventory,
            "inventory capability": inventory_cap,
            "permit": Permit(pur_permit, sal_permit),
            "price_check_dict": price_source,
        }
        self.ID = None
        self.name = None
        self.inventory = None
        self.inventory_capability = None
        self.permit = None
        self.price = None

        self.initialize()
        self.get_price(0)

    def __repr__(self) -> Dict[string, Union[string, Permit]]:
        return {
            "Name":    self.name,
            "Inventory": f"{self.inventory}/{self.inventory_capability}",
            "Permit":  self.permit
        }

    def initialize(self):
        self.ID = self.raw_data["ID"]
        self.name = self.raw_data["name"]
        self.inventory = self.raw_data["inventory"]
        self.inventory_capability = self.raw_data["inventory capability"]
        self.permit = self.raw_data["permit"]

    def reset(self):
        self.initialize()
        if self.inventory == self.raw_data["inventory"]:
            print(f"Material {self.name}:{self.ID} is reset.")
            return True
        else:
            raise ValueError(f"Material {self.name}:{self.ID} cannot be reset.")

    def get_price(self, date: int = 0) -> float:
        result = self.raw_data["price_check-dict"][date]
        if result is not None:
            return result
        else:
            return 0

    def inventory_change(self, mode: str, amount: float = 0) -> bool:
        if mode not in ["mock", "trade", "produce"]:
            raise ValueError(f"material {self.name}: inventory_change do not take a mode.")

        def check_space(space_required) -> bool:
            space_have = self.inventory_capability - self.inventory
            if space_required > space_have:
                return False
            else:
                return True

        def check_storage(inventory_required) -> bool:
            if inventory_required > self.inventory:
                return False
            else:
                return True

        def check_change(function, _amount) -> bool:
            if not function(_amount):
                return False
            else:
                if mode != "mock":
                    self.inventory += _amount
                return True

        if amount > 0:
            return check_change(check_space, amount)
        elif amount == 0:
            return True
        elif amount < 0:
            return check_change(check_storage, amount)
        else:
            raise ValueError(f"Illegal amount change for Material {self.name}: {amount}")

    def trade(self, date: int, mode: str, amount: float = 0) -> (bool, float):
        _earn = 0
        _result = False

        if amount > 0:
            if self.permit.purchase:
                if self.inventory_change(mode, amount):
                    _result = True
            else:
                pass
        elif amount == 0:
            return True
        elif amount < 0:
            if self.permit.sale:
                if self.inventory_change(mode, amount):
                    _result = True
            else:
                pass
        else:
            raise ValueError(f"Illegal amount change for Material {self.name}: {amount}")

        _result = amount * self.price
        return {_result, _earn}


