import pandas as pd

def PDdescribe(data):
    '''function which returns descriptive stats about input data'''
    df = pd.DataFrame(data)
    return df.describe()
