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
    

    def remove_outliers(self, df, columns):
        for col in columns:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
        return df

