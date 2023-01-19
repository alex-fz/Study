import numpy as np
import pandas as pd
import datetime

### Trabajar con fechas, datos nulos operaciones e indexacion
# etc...


def create_range_dates() -> pd.DatetimeIndex:

    #date in 5 days
    base_date = datetime.datetime.now().date() + datetime.timedelta(days=5)
    end_date = base_date + datetime.timedelta(days=60)

    ## create start dates step 2 days
    all_dates = pd.date_range(start=base_date, end=end_date, freq="48H", )

    # return a list of all dates (DatetimeIndex)
    return all_dates


def create_basic_df(dates: pd.DatetimeIndex, num_cols: int) -> pd.DataFrame:

    # Create random data for the data frame
    data = {
        "Col"+str(n): np.random.randint(low=1,high=100,size=5) for n in range(num_cols)
    }

    # create data frame with the dates as index, it will only pick from index 0 to num of columns
    df = pd.DataFrame(data=data,
                      index=dates[:num_cols])


    return df


def insert_null_values(data_frame: pd.DataFrame) -> pd.DataFrame:
    """Insert  null values into the data frame at respective col, index"""


    indexs = data_frame.index
    cols = data_frame.columns

    for (i, c) in zip(indexs, cols):
        data_frame.loc[i, c] = None

    return data_frame


def edit_null_values(data_frame: pd.DataFrame, filler=0) -> dict:
    """Change the null value, return the new data frame, old data frame but values are boolean of detected null values
    """

    bool_df = data_frame.isnull()
    new_df = data_frame.fillna(filler)

    data_frames = {
        "boolean df":bool_df,
        "new_df":new_df
    }

    return data_frames


def add_columns(data_frame: pd.DataFrame) -> pd.DataFrame:
    """Add some columns related to index DATES,
    add weekday name, and days remaining to new year"""

    indexs_dates = data_frame.index

    data = []
    data_year = []
    # crete a weekday ref because the method weekday
    # return the weekday number not the name
    week_ref = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]


    for date in indexs_dates:
        data.append(week_ref[date.weekday()])

        next_year = datetime.date(date.year + 1, 1, 1)

        remaining_days = next_year - date.date()
        data_year.append(remaining_days.days)


    data_frame["Weekday"] = data
    data_frame["Days to next year"] = data_year

    return data_frame


def delete_columns(data_frame: pd.DataFrame) -> dict:
    """Return a dict,
    1-A dataframe without some columns
    2-A dataframe of the deleted columns"""

    data_df = data_frame
    columns_delete = ["Col3", "Col4"]

    del_df = data_df[columns_delete]
    data_df.drop(labels=columns_delete, axis=1, inplace=True)


    dct_frames = {"df1":data_df, "df2":del_df}

    return dct_frames


if __name__ == "__main__":
    dates = create_range_dates()

    df = create_basic_df(dates=dates, num_cols=5)

    df = insert_null_values(data_frame=df)

    # Two data frames: a boolean an a new with no null values
    dict_df = edit_null_values(data_frame=df, filler=0)

    df = dict_df["new_df"]

    df = add_columns(data_frame=df)

    dict_df = delete_columns(data_frame=df)

    print(dict_df["df1"])