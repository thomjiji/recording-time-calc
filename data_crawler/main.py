import csv
import json
import pandas as pd
import os


# def merge_json(cam, url):
#     """
#     Using pandas to crawling data from https://brains.florianmilz.com/ucdb/,
#     create multiple json file, then merge them into one, deleted them in the end.
#     """
#
#     # Firstly, get a list containing multiple pandas DataFrame.
#     DataFrame_list = pd.read_html(url)
#
#     # Convert multiple DataFrames to multiple json/csv files using pandas to_json method.
#     for index, data_frame in enumerate(DataFrame_list):
#         data_frame.to_json(f'data/json/{cam}_database_{index}.json')
#
#     # Load individual JSON files from 'data/json' into a single Python list.
#     cam_database = []
#     try:
#         index_retrieve = 1
#         while True:
#             with open(f'data/json/{cam}_database_{index_retrieve}.json', 'r') as f:
#                 separate_json = json.load(f)
#                 cam_database.append(separate_json)
#                 index_retrieve += 1
#     except FileNotFoundError:
#         print(f"{cam} separate JSON file merge successful. (1/3)")
#
#     # Write that Python list into a master json file.
#     with open(f'data/json/{cam}_database.json', 'w') as f:
#         json.dump(cam_database, f)
#         print(f"{cam} master JSON file created successfully. (2/3)")
#
#     # Remove those individual json files.
#     try:
#         index_remove = 1
#         while True:
#             os.remove(f'data/json/{cam}_database_{index_remove}.json')
#             index_remove += 1
#     except FileNotFoundError:
#         print(f"{cam} separate JSON file deleted. (3/3)")


def generate_database(cam, url, type):
    """
    Using pandas to crawling data from https://brains.florianmilz.com/ucdb/,
    """

    df_all = pd.read_html(url)

    df_list = []
    for i in df_all:
        df_list.append(i)

    if type == 'json':
        with open(f'data/json/{cam}_database.json', 'w') as f:
            pd.concat(df_list, axis=0, ignore_index=True).to_json(f)
    elif type == 'csv':
        with open(f'data/csv/{cam}_database.csv', 'w') as f:
            pd.concat(df_list, axis=0, ignore_index=True).to_csv(f)


generate_database('fx3', 'https://brains.florianmilz.com/ucdb/sony/fx3', 'csv')