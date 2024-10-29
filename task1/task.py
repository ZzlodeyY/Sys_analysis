import pandas as pd

def main(csv_path:str,row_index : int, col_index:int):
    df = pd.read_csv(csv_path)
    return df.iloc[row_index].values[col_index]

print(main("Путь к csv"))
