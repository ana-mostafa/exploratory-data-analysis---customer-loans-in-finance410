class DataFrameInfo:

    def __init__(self, df):
        self.df = df

    def check_data_types(self):
        return self.df.dtypes
    
    def statistical_values(self):
        return self.df.describe()
    
    def count_distinct_values(self):
        return self.df.select_dtypes(include=['object']).nunique()
    
    def print_df_shape(self):
        print(f"Shape of DataFrame: {self.df.shape}")

    def null_values(self):
        return self.df.isnull().sum()
    
    def percentage_null_values(self):
        total_cells = self.df.size
        null_count = self.df.isnull().sum()
        return (null_count / total_cells) * 100       