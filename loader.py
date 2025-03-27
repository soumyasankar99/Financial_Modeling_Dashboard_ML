import pandas as pd

def load_data(file):
    ext = file.name.split('.')[-1]
    if ext == 'csv':
        return pd.read_csv(file)
    elif ext in ['xls', 'xlsx']:
        return pd.read_excel(file)
    elif ext == 'tsv':
        return pd.read_csv(file, sep='\t')
    else:
        return None
