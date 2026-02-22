import pandas as pd
from sklearn.model_selection import train_test_split


def split_xy(df: pd.DataFrame, target_column: str) -> tuple[pd.DataFrame, pd.Series]:
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y


def make_train_test_split(X: pd.DataFrame, y: pd.Series, test_size: float, random_state: int) -> list[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    return train_test_split(X, y, test_size = test_size, random_state = test_size, stratify = y)