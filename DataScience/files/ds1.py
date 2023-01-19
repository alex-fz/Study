import pandas as pd
import json
import os
import datetime
from random import randint
from string import ascii_uppercase
from email.message import EmailMessage
import mimetypes
import smtplib
import getpass


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

    cols = data_frame.columns
    add = 100
    for c in cols:
        data_frame[c] += add

    return data_frame


def turn_into_json(data_frame: pd.DataFrame) -> json:

    json_1 = data_frame.to_json()
    return json_1


def json_to_file(json_file: str, name_file: str) -> str:
    assert type(name_file) == str, "The name should be an string"

    path_to_file = os.path.join(os.path.dirname(__file__), name_file + ".json")

    if os.path.exists(path_to_file):
        raise FileExistsError("This file already exists, input another name")


    new_json = json.loads(json_file)
    with open(file=path_to_file, mode="w") as file:
        json.dump(new_json, file, indent=4)
        print("json file created")

    return path_to_file


def send_email(path_attachment: str, sender_, recipient_) -> bool:

    ### Create message
    message = EmailMessage()

    sender, recipient = sender_, recipient_
    subject, body = "No subject", "No body"  # change this variable for add subject or body

    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    type_m, _ = mimetypes.guess_type(path_attachment)
    type_m, type_s = type_m.split("/", 1)

    with open(file=path_attachment, mode="rb") as file:
        message.add_attachment(file.read(),
                               maintype=type_m,
                               subtype=type_s,
                               filename=os.path.basename(path_attachment))


    ### send email through smtp server

    try:
        email_server = smtplib.SMTP_SSL("smtp.gmail.com", port=465)
        email = input("Type email: ")
        password = getpass.getpass(prompt="Type password: ")
        email_server.login(user=email, password=password)
        email_server.send_message(message)
        email_server.quit()
        return True

    except smtplib.SMTPException:
        print("Error ocurred")
        return False





if __name__ == "__main__":
    test_list = create_dates()

    test_dict = re_decorate_dates(list_of_dates=test_list)

    test_data_frame = empty_data_frame(dict_of_dates=test_dict)

    test_data_frame = add_content_df(data_frame=test_data_frame)

    test_data_frame = edit_data_df(data_frame=test_data_frame)

    json_test = turn_into_json(data_frame=test_data_frame)

    path = json_to_file(json_test, "Test1")

    send_email(path_attachment=path, sender_="", recipient_="") ### BORRAR



