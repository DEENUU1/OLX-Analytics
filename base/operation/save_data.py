import pandas as pd
from typing import List
from base.data.parser import ParseData


def save_to_excel(data: List[ParseData]):
    df = pd.DataFrame(data=data)
    df.to_excel('olx-analytics.xlsx',index=False)
