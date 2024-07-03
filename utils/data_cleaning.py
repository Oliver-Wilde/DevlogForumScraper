import pandas as pd

def clean_data(df):
    # Example cleaning steps
    df['content'] = df['content'].str.replace('\n', ' ').str.strip()
    df['author'] = df['author'].str.strip()
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # Drop rows with missing or invalid dates
    df = df.dropna(subset=['date'])
    
    return df
