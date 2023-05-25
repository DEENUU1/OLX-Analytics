from typing import List

import pandas as pd

from base.data.parser import ParseData


def save_to_excel(data: List[ParseData]):
    df = pd.DataFrame(data=data)
    df.to_excel("olx-analytics.xlsx", index=False)
