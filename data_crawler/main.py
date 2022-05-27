import csv
import json
import pandas as pd
import os
from pathlib import Path


"""Data crawling using pandas. Get a list containing multiple pandas DataFrame."""
DataFrame_list = pd.read_html(r'https://brains.florianmilz.com/ucdb/sony/fx3')

"""Convert multiple DataFrames to json/csv."""
file_index = 1
for data_frame in DataFrame_list:
    data_frame.to_json(f'data/json/fx3_database_{file_index}.json')
    file_index += 1


def json_merge(cam):
    """Merge multiple json files together, then delete those individual json files."""

    # Load individual json files into one list.
    cam_database = []
    try:
        index = 1
        while True:
            with open(f'data/json/{cam}_database_{index}.json', 'r') as f:
                separate_json = json.load(f)
                cam_database.append(separate_json)
                index += 1
    except FileNotFoundError:
        print(f"{cam} separate JSON file merge successful.")

    # Write that list into a master json file.
    with open(f'data/json/{cam}_database.json', 'w') as f:
        json.dump(cam_database, f)
        print(f"{cam} master JSON file created successfully.")

    # Remove those individual json files.
    try:
        index_remove = 1
        while True:
            os.remove(f'data/json/{cam}_database_{index_remove}.json')
            index_remove += 1
    except FileNotFoundError:
        print(f"{cam} separate JSON file deleted.")


json_merge('fx3')

# """Get csv file contents."""
# filename = 'data/csv/fx3_table_1.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
# """Get first row - header information."""
# for index, column_header in enumerate(header_row):
#     print(index, column_header)