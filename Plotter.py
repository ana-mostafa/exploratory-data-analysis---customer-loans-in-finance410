import pandas as pd
import matplotlib.pyplot as plt

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
