import pandas as pd
from typing import List
from base.data.parser import ParseData


def save_to_excel(data: List[ParseData], file_path: str):
    df = pd.DataFrame(data=data)
    df.to_excel(file_path, index=False)
