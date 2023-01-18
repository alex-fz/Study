import pandas as pd
import numpy as np
import sqlite3
import os
import datetime
from string import ascii_uppercase
from random import randint
import json


### Setup connection to db
cnx = sqlite3.connect("test_data_base.db")
cursor = cnx.cursor()


class WorkPandas():

    @classmethod
    def create_random_data(cls, cols: int, rows: int):
        assert type(cols) == int, "arg cols not integer"
        assert type(rows) == int, "arg cols not integer"

        dictionary = {ascii_uppercase[n]:[randint(a=1, b=10)]*rows for n in range(cols)}
        data = pd.DataFrame(data=dictionary)

        return data


    def __init__(self):
        self.random_df = self.create_random_data(cols=7,rows=3)


    def operations_of_columns(self, data_frame: pd.DataFrame) -> any:

        all_operations = {}

        for col in data_frame.columns:

            if data_frame[col].dtype == pd.Int64Dtype.type:

                ### Operations
                all_operations[data_frame[col].name] = ["SumValues: " + str(data_frame[col].sum()),
                                                        "MeanColumn: " + str(data_frame[col].mean()),
                                                        "MinValue: " + str(data_frame[col].min()),
                                                        "MaxValue: " + str(data_frame[col].max()),
                                                        ]



            else:
                continue

        info_oper_json = json.dumps(all_operations, indent=2)
        return info_oper_json


    def change_index_dates(self, data_frame: pd.DataFrame) -> pd.DataFrame:

        date = "2020-06-11"
        converted_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        dates_list = [converted_date]

        for index in data_frame.index:
            converted_date = converted_date + datetime.timedelta(days=10)
            dates_list.append(converted_date)

        data_frame.index = dates_list[0:len(data_frame.index)]
        return data_frame


    def to_data_base(self, data_frame: pd.DataFrame):
        data_frame.to_sql("data frame", con=cnx)
        cnx.commit()
        cnx.close()


def normal_arange():
    numpy_array: np.array = np.arange(1, 101).reshape(10, 10)
    rows, cols = numpy_array.shape
    test_data_frame = pd.DataFrame(data=numpy_array, index=[n for n in range(rows )],
                                   columns=[ascii_uppercase[n] for n in range(cols )])

    return test_data_frame


def file_json(json_data):

    file_path = os.path.join(os.path.dirname(__file__), "df1.json")

    if type(json_data) == str:
        data_convert = json.loads(json_data)

        with open(file=file_path, mode="w") as file:
            json.dump(obj=data_convert,fp=file, indent=2)
        file.close()

    else:
        with open(file=file_path, mode="w") as file:
            json.dump(obj=json_data,fp=file, indent=2)
        file.close()




if __name__ == "__main__":
    df = normal_arange()
    pd_worker = WorkPandas()
    j = pd_worker.operations_of_columns(data_frame=df)
    new_df = pd_worker.change_index_dates(data_frame=df)
    pd_worker.to_data_base(data_frame=new_df)