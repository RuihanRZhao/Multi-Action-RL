# python standard
from typing import Dict, Union              # type control
from datetime import datetime, timedelta    # time calculate

# components of the project
from object import Material, Producer


class Factory:
    def __init__(self, target: str | None = None):
        """
        Initialize the factory from the target directory, otherwise use the default settings


        """
        # get the link of the factory environment data
        self.source = target if target is not None else "data/"

        # the material and producer objects
        self.materials: list[Material] = []
        self.producers: list[Producer] = []
        self.price_standard: Dict[datetime, Union[float]] = {}
        self.raw = {
            "materials": list[Material],
            "producers": list[Producer],
        }

        self.date_start: datetime = datetime(2022, 2, 1)
