import pandas as pd


def get_file_csv(path_data: str):
    result = pd.read_csv(path_data, delimiter=";")
    return result
