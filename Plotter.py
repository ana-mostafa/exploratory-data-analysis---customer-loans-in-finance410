import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Plotter:
    def visualize_nulls(self, df):
        # Calculate null count before and after removal
        null_count_before = df.isnull().sum()
        df_cleaned = df.dropna()
        null_count_after = df_cleaned.isnull().sum()
        
        # Plotting
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        null_count_before.plot(kind='bar', title='NULL Counts Before Cleaning', ax=axes[0])
        null_count_after.plot(kind='bar', title='NULL Counts After Cleaning', ax=axes[1])
        
        plt.tight_layout()
        plt.show()

    def visualize_skew(self, df):
        numerical_cols = df.select_dtypes(include=['number'])
        skewness = numerical_cols.skew()
        
        plt.figure(figsize=(8, 6))
        skewness.plot(kind='bar', color='skyblue')
        plt.title('Skewness of Numerical Columns')
        plt.xlabel('Columns')
        plt.ylabel('Skewness')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.show()

    def visualize_skew_sns(self, df, columns):
        numeric_features = [col for col in df.columns if df[col].dtype in ['int64', 'float64']]

        sns.set(font_scale=0.7)
        f = pd.melt(df[numeric_features].reset_index(), id_vars="index", value_vars=numeric_features)
        g = sns.FacetGrid(f, col="variable", col_wrap=3, sharex=False, sharey=False)
        g = g.map(sns.histplot, "value", kde=True)

        plt.show()
    
    def visualize_outliers(self, df, columns):
        plt.figure(figsize=(12, 6))
        for col in columns:
            sns.boxplot(x=df[col])
            plt.title(f'Boxplot of {col}')
            plt.show()