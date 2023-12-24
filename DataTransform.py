import pandas as pd

class DataTransform:
    @staticmethod
    def convert_to_numeric(df, columns):
        df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
        return df

    @staticmethod
    def convert_to_categorical(df, columns):
        df[columns] = df[columns].astype('category')
        return df
    
    @staticmethod
    def convert_to_datetime(df, columns):
        for col in columns:
            df[col] = pd.to_datetime(df[col], errors='coerce', format='%b-%Y')
        return df
    
    @staticmethod
    def remove_symbols(df, columns, symbols):
        for col in columns:
            for symbol in symbols:
                df[col] = df[col].str.replace(symbol, '')
        return df

