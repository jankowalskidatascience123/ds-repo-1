import os

import tyro

from config import settings
from utils.constants import TARGET_COLUMN
from utils.data_loader import DataLoader
from utils.ml.artifacts import save_csv
from utils.ml.split import split_xy, make_train_test_split


def main(data_path: str, artifacts_output_path: str, test_size: float = settings.TEST_SIZE):
    df = DataLoader(data_path).load()
    X, y = split_xy(df, TARGET_COLUMN)
    X_train, X_test, y_train, y_test = make_train_test_split(
        X, y, test_size = test_size, random_state = settings.RANDOM_STATE
    )

    save_csv(X_train, os.path.join(artifacts_output_path, 'X_train.csv'))
    save_csv(X_test, os.path.join(artifacts_output_path, 'X_test.csv'))
    save_csv(y_train, os.path.join(artifacts_output_path, 'y_train.csv'))
    save_csv(y_test, os.path.join(artifacts_output_path, 'y_test.csv'))


if __name__ == "__main__":
    tyro.cli(main)