import pandas as pd
import numpy as np
import json
import os
import datetime
from random import randint
from string import ascii_uppercase


def create_dates() -> list:

    list_of_dates = []

    while len(list_of_dates) < 5:

        random_year, random_month, random_day = randint(a=1900,b=2023), randint(a=1,b=12), randint(a=1,b=30)
        list_of_dates.append(datetime.date(year=random_year, month=random_month, day=random_day))


    return list_of_dates


def re_decorate_dates(list_of_dates: list) -> dict:

    new_dict = {}
    for (num, date) in zip(range(len(list_of_dates)), list_of_dates):

        new_dict[ascii_uppercase[num]] = date.strftime("%d %B, %Y")

    return new_dict


def empty_data_frame(dict_of_dates: dict) -> pd.DataFrame:
    """Create a dataframe with the keys as indexs
    and the values as columns, the dataframe content is None"""

    df = pd.DataFrame(index=dict_of_dates.keys(), columns=dict_of_dates.values())
    return df


def add_content_df(data_frame: pd.DataFrame) -> pd.DataFrame:
    """Random numbers to all df"""


    cols, rows = data_frame.columns, data_frame.index

    for c in cols:
        for r in rows:
            new_data = randint(a=1, b=100)

            data_frame.loc[r, c] = new_data

    return data_frame


def edit_data_df(data_frame: pd.DataFrame) -> pd.DataFrame:
    pass


if __name__ == "__main__":
    test_list = create_dates()

    test_dict = re_decorate_dates(list_of_dates=test_list)

    test_data_frame = empty_data_frame(dict_of_dates=test_dict)

    print(add_content_df(data_frame=test_data_frame))





