from datetime import datetime
import os

import pandas as pd

def _ensure_dir(path: str) -> None:
    '''
    funkcja utworzy ściezke jeśeli nie istnieje
    '''
    now_str = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    os.makedirs(f'{path}\\{now_str}', exist_ok=True)


def save_csv(df: pd.DataFrame, path: str) -> None:
    _ensure_dir(os.path.dirname(path))
    df.to_csv(path, index=False)