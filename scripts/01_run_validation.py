import tyro

from utils.constants import REQUIRED_COLUMNS, TARGET_COLUMN
from utils.data_loader import DataLoader
from utils.ml.validate import check_if_columns_exist, check_target_col_not_empty, printout_basic_report


def main(data_path: str):
    df = DataLoader(data_path).load()
    check_if_columns_exist(df, REQUIRED_COLUMNS)
    check_target_col_not_empty(df, TARGET_COLUMN)
    printout_basic_report(df, TARGET_COLUMN)

if __name__ == "__main__":
    tyro.cli(main)