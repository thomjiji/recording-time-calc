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
    column_index = 1

    for column in range(len(csv_database.columns)):
        options = set(csv_database[csv_database.columns[column_index]])
        if len(options) == 1:
            continue

        # Let user select the first option. Use this selection create a filterer.
        print(f">>> Select {csv_database.columns[column_index]} below: ")
        available_options = {}
        for index, opt in enumerate(sorted(options)):
            print(f"{index + 1}. {opt}")
            available_options[f"{index + 1}"] = opt
        user_selection = input(">>> ")
        filterer = available_options[user_selection]
        csv_database = csv_database[csv_database[f"{csv_database.columns[column_index]}"] == filterer]
        column_index += 1

        # if len(options) == 1:


print_selection('fx6')

"""pandas"""
"""1"""
# Use read_csv function to create a initial DataFrame including all parameter.
# csv_database = pd.read_csv('data_crawler/data/csv/gh5m2_database.csv')

# Create a Python set to display available options in current column.
# x = csv_database.columns[1]
# resolution_options = set(csv_database[csv_database.columns[1]])
# print(resolution_options)

# # Let user to select first parameter: resolution.
# print(">>> Select resolution below: ")
# available_options = {}
# for index, res in enumerate(sorted(resolution_options)):
#     print(f"{index + 1}. {res}")
#     available_options[f'{index + 1}'] = res
# user_selection = input(">>> ")
# filterer = available_options[user_selection]
#
# """2"""
# # Use user entered selection to filter out a part of DataFrame row, yielding a new DataFrame.
# after_first_selection = csv_database[csv_database['resolution'] == filterer]
#
# # Create a Python set to display available options in current column.
# codec_options = set(after_first_selection['codec'])
#
# print(">>> Select codec below: ")
# available_options = {}
# for index, cdc in enumerate(sorted(codec_options)):
#     print(f"{index + 1}. {cdc}")
#     available_options[f'{index + 1}'] = cdc
# user_selection = input(">>> ")
# filterer = available_options[user_selection]
#
# """3"""
# after_second_selection = after_first_selection[after_first_selection['codec'] == filterer]
# print(after_second_selection)