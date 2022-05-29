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


"""pandas"""
"""1"""
# Use read_csv function to create a initial DataFrame including all parameter.
csv_database = pd.read_csv('data_crawler/data/csv/gh5m2_database.csv')

# Create a Python set to display available options in current column.
resolution_options = set(csv_database['resolution'])

# Let user to select first parameter: resolution.
print(">>> Select resolution below: ")
available_options = {}
for index, res in enumerate(sorted(resolution_options)):
    print(f"{index + 1}. {res}")
    available_options[f'{index + 1}'] = res
user_selection = input(">>> ")
filterer = available_options[user_selection]

"""2"""
# Use user entered selection to filter out a part of DataFrame row, yielding a new DataFrame.
after_first_selection = csv_database[csv_database['resolution'] == filterer]

# Create a Python set to display available options in current column.
codec_options = set(after_first_selection['codec'])

print(">>> Select codec below: ")
available_options = {}
for index, cdc in enumerate(sorted(codec_options)):
    print(f"{index + 1}. {cdc}")
    available_options[f'{index + 1}'] = cdc
user_selection = input(">>> ")
filterer = available_options[user_selection]

"""3"""
after_second_selection = after_first_selection[after_first_selection['codec'] == filterer]
print(after_second_selection)