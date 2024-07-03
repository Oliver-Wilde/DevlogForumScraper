import pandas as pd
from utils.data_cleaning import clean_data

def process_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df = clean_data(df)
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    input_file = 'data/raw/forum_data_raw.csv'
    output_file = 'data/processed/forum_data_processed.csv'
    process_data(input_file, output_file)
