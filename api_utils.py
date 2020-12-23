import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile




def parse_excel(path):
    df = pd.read_excel(
            open(path, 'rb'),
              sheet_name='Page 1',
              engine="openpyxl")
    return df


def get_count(df):
    out = []
    try:
        buffer = df['Codigo_Producto'].value_counts()
        buffer2 = buffer.index
        buffer = buffer.to_list()
        for i in buffer:
            ind = buffer.index(i)
            tuplee = []
            tuplee.append(i)
            tuplee.append(buffer2[ind])
            out.append(tuplee)
        print(out)
        return out
    except KeyError:
        out="error de excel, columna Codigo_Producto no encontrada"
        return out
    finally:
        del out 
        pass