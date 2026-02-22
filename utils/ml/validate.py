from typing import Iterable
import pandas as pd


def check_if_columns_exist(df: pd.DataFrame, required_columns: Iterable[str]) -> None:
    '''
    funkcja, która sprawdza czy wszystkie wymagane kolumny sa w danych
    jeśli nie, to podnosi błąd
    '''
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f'Missing columns: {",".join(missing)}')


def check_target_col_not_empty(df: pd.DataFrame, target_column: str) -> None:
    '''
    funkcja sprawdzająca czy kolumna z y jest w pełni pusta,
    jeśli tak - to podnosi błąd
    '''
    if df[target_column].isna().all():
        raise ValueError(f'Target column {target_column} is empty')


def printout_basic_report(df: pd.DataFrame, target_column: str) -> None:
    '''
    funkcja wyświetlająca podstawowe statystyki na temat danych
    '''
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"Missing values per column: {df.isna().sum()}")
    print(f"Target distribution\n: {df[target_column].value_counts(dropna=False, normalize=True)}")
