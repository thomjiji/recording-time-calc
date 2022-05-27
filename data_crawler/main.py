import csv
import json
import pandas as pd
import os
from pathlib import Path


def data_crawl(cam, filetype, url):
    """
    Using pandas to crawling data from https://brains.florianmilz.com/ucdb/,
    create multiple json/csv file, then merge them into one, deleted them in the end.
    """

    # Firstly, get a list containing multiple pandas DataFrame.
    DataFrame_list = pd.read_html(url)

    # Convert multiple DataFrames to multiple json/csv files using pandas to_json method.
    index_to_json_csv = 1
    if filetype == "json":
        for data_frame in DataFrame_list:
            data_frame.to_json(f'data/json/{cam}_database_{index_to_json_csv}.json')
            index_to_json_csv += 1
    elif filetype == "json":
        for data_frame in DataFrame_list:
            data_frame.to_json(f'data/csv/{cam}_database_{index_to_json_csv}.csv')
            index_to_json_csv += 1
    else:
        return None

    # Load individual JSON files from 'data/json' into a single Python list.
    cam_database = []
    if filetype == "json":
        try:
            index_retrieve = 1
            while True:
                with open(f'data/json/{cam}_database_{index_retrieve}.json', 'r') as f:
                    separate_json = json.load(f)
                    cam_database.append(separate_json)
                    index_retrieve += 1
        except FileNotFoundError:
            print(f"{cam} separate JSON file merge successful. (1/3)")
    elif filetype == "csv":
        try:
            index_retrieve = 1
            while True:
                with open(f'data/csv/{cam}_database_{index_retrieve}.csv', 'r') as f:
                    reader = csv.reader(f, delimiter=',')

    # Write that Python list into a master json file.
    with open(f'data/json/{cam}_database.json', 'w') as f:
        json.dump(cam_database, f)
        print(f"{cam} master JSON file created successfully. (2/3)")

    # Remove those individual json files.
    try:
        index_remove = 1
        while True:
            os.remove(f'data/json/{cam}_database_{index_remove}.json')
            index_remove += 1
    except FileNotFoundError:
        print(f"{cam} separate JSON file deleted. (3/3)")


data_crawl('gh5m2', 'https://brains.florianmilz.com/ucdb/panasonic/gh5ii')

# """Get csv file contents."""
# filename = 'data/csv/fx3_table_1.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
# """Get first row - header information."""
# for index, column_header in enumerate(header_row):
#     print(index, column_header)