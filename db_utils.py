import yaml
import sqlalchemy as db
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

file_path = '/Users/moustafarashed/EDA_Projects/exploratory-data-analysis---customer-loans-in-finance410/credentials.yaml'
def load_credentials(file_path):
    with open(file_path, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials


class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = self._create_engine()
    
    def _create_engine(self):
        credentials = self.credentials
        HOST = credentials['RDS_HOST']
        PORT = credentials['RDS_PORT']
        PASS = credentials['RDS_PASSWORD']
        USERNAME = credentials['RDS_USER']
        DB_NAME = credentials['RDS_DATABASE']
        #engine = db.create_engine(f"{self.db_api}+psycpg2://{USERNAME}:{PASS}@{HOST}:{PORT}/{DB_NAME}")
        connection_str = f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        engine = db.create_engine(connection_str)
        return engine
    
    def extract_data(self):
        query = "SELECT * FROM loan_payments;"
        df = pd.read_sql(query, self.engine)
        return df
    def save_to_csv(self, data, csv_path):
        data.to_csv(csv_path, index=False)
            
creds = load_credentials(file_path)
connector = RDSDatabaseConnector(creds)
#connector._create_engine()
data_frame = connector.extract_data()
csv_path = '/Users/moustafarashed/EDA_Projects/exploratory-data-analysis---customer-loans-in-finance410/loan_payments.csv'
connector.save_to_csv(data_frame, csv_path)

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    return df
if __name__ == "__main__":
    creds = load_credentials(file_path)
    connector = RDSDatabaseConnector(creds)
    
    data_frame = connector.extract_data()
    csv_path = '/Users/moustafarashed/EDA_Projects/exploratory-data-analysis---customer-loans-in-finance410/loan_payments.csv'
    connector.save_to_csv(data_frame, csv_path)
    
    loaded_data = load_data(csv_path)
    print(loaded_data.head())