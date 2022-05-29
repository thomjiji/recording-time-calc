import pandas as pd


def generate_database(cam, url, type):
    """
    Using pandas to crawling data from https://brains.florianmilz.com/ucdb/,
    then output to json or csv files.
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