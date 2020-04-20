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
