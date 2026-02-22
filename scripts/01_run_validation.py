from utils.data_loader import DataLoader

from config import settings
from utils.ml.validate import check_if_columns_exist, check_target_col_not_empty, printout_basic_report
from utils.constants import REQUIRED_COLUMNS, TARGET_COLUMN

df = DataLoader(settings.DATA_PATH).load()

check_if_columns_exist(df, REQUIRED_COLUMNS)
check_target_col_not_empty(df, TARGET_COLUMN)
printout_basic_report(df, TARGET_COLUMN)