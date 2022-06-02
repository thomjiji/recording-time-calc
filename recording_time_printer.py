import json
import sys

import pandas as pd


def recording_time(bitrate, capacity):
    """
    Calculate how long the camera can record based on a certain bit rate
    and card capacity.
    """
    time = round(capacity * 1000 * 8 / bitrate / 60)
    print(f"Can record up to {time} minutes (theoretically).")


def get_bitrate(
    camera,  # this
    sensor_mode,
    resolution,  # this
    codec,
    chroma_subsampling,
    bit_depth,
    frame_rate,  # this
    file_format,
):
    """Get bitrate from database and return."""
    filename = f"data/{camera}_database.json"
    with open(filename, 'r') as f:
        cam_para = json.load(f)
        for i in cam_para:
            para_array = [
                sensor_mode,
                resolution,
                codec,
                chroma_subsampling,
                bit_depth,
                frame_rate,
                file_format,
            ]
            index = 0
            for value in i.values():
                if index > 6:
                    return value
                elif value == para_array[index]:
                    index += 1
                    continue
                else:
                    break
        return None


def print_selection(cam):
    csv_database = pd.read_csv(f'data_crawler/data/csv/{cam}_database.csv')

    if 'sensor mode' not in csv_database.columns:
        csv_database = pd.read_csv(f'data_crawler/data/csv/{cam}_database.csv', usecols=[1, 2, 3, 4, 6, 7, 9, 8])
    else:
        csv_database = pd.read_csv(f'data_crawler/data/csv/{cam}_database.csv', usecols=[1, 2, 3, 4, 5, 6, 7, 10, 8])

    csv_database.fillna(0, inplace=True)

    column_index = 0

    for count, column in enumerate(csv_database.columns):

        options = set(csv_database[csv_database.columns[column_index]])

        if len(options) == 1:
            column_index += 1
            for i in options:
                print(f"Automatically selected {i}.")
            continue

        print(f">>> Select {csv_database.columns[column_index]} below: ")
        available_options = {}
        for index, option in enumerate(sorted(options)):
            print(f"{index + 1}. {option}")
            available_options[f"{index + 1}"] = option
        user_selection = input(">>> ")

        filterer = available_options[user_selection]
        csv_database = csv_database[csv_database[f"{csv_database.columns[column_index]}"] == filterer]

        if csv_database['datarate'].eq(0).all():
            print(f"datarate is not available in {available_options[user_selection]} format.")
            break

        if len(csv_database.index) == 1:
            print(f"datarate is {csv_database['datarate'].values}.")
            break

        column_index += 1


print_selection('gh5s')