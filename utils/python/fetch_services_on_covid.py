from io import BytesIO

import requests
import pandas as pd

class Data(object):
    def __init__(self, url, output_path):
        self.url = url
        self.output_path = output_path

    def store_gsheet_as_json(self):
        r = requests.get(self.url)
        data = r.content
        data = pd.read_csv(BytesIO(data), index_col=0)
        data.to_json(self.output_path, orient='records')


if __name__ == "__main__":
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRiCZwST61wijeBPIX8IM82k2ix_BEH3UtNOSCqEDWYhnOzX7Pv_fDUlCYj-RQKxJAgZrK9JgHiU5vb/pub?gid=1551943992&single=true&output=csv'
    output_path = './../src/assets/data/services_list.json'
    data = Data(url, output_path)
    data.store_gsheet_as_json()

    url_2 = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSKjJRzdDiq6j5BwnFW6Djs83I6S9GmC9O11igdE9zGFZALJIKb-qt5eMnjiImivIgb6zdpzopbzcv-/pub?gid=1142068857&single=true&output=csv'
    output_path_2 = './../src/assets/data/libraries_list.json'
    data_2 = Data(url_2, output_path_2)
    data_2.store_gsheet_as_json()
