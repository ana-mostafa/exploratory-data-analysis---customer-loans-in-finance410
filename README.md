# explanatory data analysis
steps for the project:
1-db_utils.py: contains the code that dowloads the dataset from thw AWS.
2-Plotter.py: handles the code for different stages of visualizations.
3-DataFrameTransform.py: contains the class for for handling null values by either imputing or droping columns, also handles the skewed data, but the file freezes whever i use it, so some operations done outsid the class using the pandas directly.
4-DataFrameInfo.py: contains the class that retreives info about the dataset.
5-DataTransform.py: contains the class that transform the variables to the correct datatypes.