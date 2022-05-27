import csv

import pandas as pd

# DataFrame_list = pd.read_html(r'https://brains.florianmilz.com/ucdb/panasonic/gh5ii')
#
# # Convert DataFrame to csv file.
# index = 1
# for data_frame in DataFrame_list:
#     data_frame.to_csv(f'test_csv_writer_reader_{index}.csv')
#     index += 1


# Use pandas to read csv.
csv_reading_1 = pd.read_csv('test_csv_writer_reader_1.csv')
csv_reading_2 = pd.read_csv('test_csv_writer_reader_2.csv')
csv_reading_3 = pd.read_csv('test_csv_writer_reader_3.csv')
csv_reading_4 = pd.read_csv('test_csv_writer_reader_4.csv')
csv_reading_5 = pd.read_csv('test_csv_writer_reader_5.csv')

final_csv = pd.concat([csv_reading_1, csv_reading_2, csv_reading_3, csv_reading_4, csv_reading_5], ignore_index=True)
final_csv.drop('<anonymous>', 1).to_csv('test_csv_final.csv')