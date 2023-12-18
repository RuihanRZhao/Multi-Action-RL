# python standard
from typing import Dict, Union              # type control
from datetime import datetime, timedelta    # time calculate

# components of the project
from object import Material, Producer


class Factory:
    def __init__(self, process_for_factory: int = 1):
        """
        Initialize the factory from the target directory, otherwise use the default settings
        """
        # multi-process settings
        self.process = process_for_factory

        # the material and producer objects
        self.material_list = []

        self.date_start: int = 0

    def load_data(self):
        source = "./data"

    def initialize_material_list(self):


