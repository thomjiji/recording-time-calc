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

    for count, column in enumerate(range(len(csv_database.columns))):
        """
        Inside the set parentheses, The output of the expression in the
        outer square brackets is the column's name. The output of the
        csv_database DataFrame `csv_database['column's name']` is the whole
        column's value. We use set() function to turn the column's value into
        a non-repeating set data type.
        """
        options = set(csv_database[csv_database.columns[column_index]])
        if 'nan' in options:
            print(f"{csv_database.columns[column_index]} parameter is not available.")
            column_index += 1
            continue

        if len(options) == 1:
            column_index += 1
            for i in options:
                print(f"Automatically selected {i}.")
            continue

        # Let user select the first option. Use this selection create a filterer.
        """这里我们 print 出可选项，把用户的记录选择到 available_options 供下面的筛选使用。"""
        print(f">>> Select {csv_database.columns[column_index]} below: ")
        available_options = {}
        for index, option in enumerate(sorted(options)):
            print(f"{index + 1}. {option}")
            available_options[f"{index + 1}"] = option
        user_selection = input(">>> ")

        """基于用户的输入（数字），找到该数字（key）在 available_options 里对应的 values，assign 到
        filterer 这个 variable 上。"""
        filterer = available_options[user_selection]
        """使用 filterer 作为筛选，过滤掉用户选项之外的 row，由此创建新的 csv_database DataFrame 
        供下一个 loop 使用。"""
        csv_database = csv_database[csv_database[f"{csv_database.columns[column_index]}"] == filterer]

        if len(csv_database.index) == 1:
            print(f"datarate is {csv_database['datarate'].values}.")
            break

        column_index += 1


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