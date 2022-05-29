import pandas as pd

DataFrame_all = pd.read_html(r'https://brains.florianmilz.com/ucdb/panasonic/gh5ii')

DataFrame_list = []
for i in DataFrame_all:
    DataFrame_list.append(i)

with open('test-reading-csv-and-merge/test_csv_final.csv', 'w') as f:
    pd.concat(DataFrame_list, axis=0).to_csv(f)