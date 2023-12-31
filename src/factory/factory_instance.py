# python standard
import string
from typing import Dict, Union  # type control
from datetime import datetime, timedelta  # time calculate

# components of the project
from object import Material, Producer
from utillity.u_csv import load_data


class Factory:
    def __init__(self, process_for_factory: int = 1):
        """
        Initialize the factory from the target directory, otherwise use the default settings
        """
        # multi-process settings
        self.process = process_for_factory

        # the material and producer objects
        self.material_list = []
        self.producer_list = []
        self.produce_detail = []
        self.price_detail = []

        self.date_start: int = 0

    def load_data(self, source: string = "./data"):
        material = source + "/material.csv"
        price = source + "/material_price.csv"
        producer = source + "/producer.csv"
        produce = source + "/produce.csv"

        def create_list(instance_type, location, extra_infos: list[list] = None) -> list:
            temp_list = []
            header, instances = load_data(location)


            for line in instances:

                print(line)
                element_additional_list_info = []
                if extra_infos is not None:
                    for extra_info in extra_infos:
                        if extra_info[0] == line[0]:
                            element_additional_list_info.append(extra_info)

                if instance_type is not None:
                    # test usage print
                    # print(*line, element_additional_list_info)
                    temp_list.append(instance_type(*line, element_additional_list_info))
                else:
                    temp_list.append(line)
            return temp_list

        self.material_list = create_list(Material, material, create_list(None, price))
        self.producer_list = create_list(Producer, producer, create_list(None, produce))

    def initialize_material_list(self):
        pass


if __name__ == "__main__":
    f = Factory(1)
    f.load_data()
    print(f.producer_list)
