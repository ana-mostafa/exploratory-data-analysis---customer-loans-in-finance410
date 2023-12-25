import pandas as pd

class DataFrameTransform:

    def __init__(self, df):
        self.df = df   

    def drop_column(self, columns):
        self.df.drop(columns, axis = 1, inplace = True)
        return self.df
    
    def impute_column(self, column_name, strategy='median'):
        if strategy == 'median':
            self.df[column_name].fillna(self.df[column_name].median(), inplace=True)
        elif strategy == 'mean':
            self.df[column_name].fillna(self.df[column_name].mean(), inplace=True)
        elif strategy == 'mode':
            self.df[column_name].fillna(self.df[column_name].mode(), inplace=True)            
        else:
            print("Invalid imputation strategy!")
        return self.df
