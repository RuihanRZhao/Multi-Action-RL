import csv


def load_data(position: str):
    try:
        # Open the file in read mode
        with open(position, 'r', newline="") as file:
            cursor = csv.reader(file, delimiter=",")
            header = next(cursor)
            data = []
            for row in cursor:
                row_dict = []
                for i, col in enumerate(header):
                    row_dict.append(row[i])
                data.append(row_dict)
            return header, data

    except FileNotFoundError:
        print(f"The file in '{position}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    print(load_data("../data/material.csv"))
