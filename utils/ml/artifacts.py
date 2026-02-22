import os

import pandas as pd

def _ensure_dir(path: str) -> None:
    '''
    funkcja utworzy ściezke jeśeli nie istnieje
    '''
    os.makedirs(path, exists_ok=True)


def save_csv(df: pd.DataFrame, path: str) -> None:
    _ensure_dir(os.path.dirname(path))
    df.to_csv(path, index=False)