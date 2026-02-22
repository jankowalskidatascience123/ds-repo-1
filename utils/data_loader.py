import os
import pandas as pd

class DataLoader:
    '''
    twozymy klasę która w zalezności od rozszerzenia pliku
    uzyje odpowiedniej funkcji z pandasa do zaczytania pliku do df
    '''

    def __init__(self, path: str) -> None:
        self.path = path

    def load(self) -> pd.DataFrame | None:
        extension = os.path.split(self.path)[-1].split('.')[-1]

        load_func_dict = {
            'csv': self._load_csv,
            'xlsx': self._load_excel,
            'parquet': self._load_parquet,
        }
        load_func = load_func_dict.get(extension)
        if load_func is None:
            raise Exception(f"Following extension {extension} is not supported")
        return load_func()

    def _load_csv(self):
        return pd.read_csv(self.path)

    def _load_excel(self):
        return pd.read_excel(self.path)

    def _load_parquet(self):
        return pd.read_parquet(self.path)

