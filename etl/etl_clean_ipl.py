import pandas as pd

def clean_and_save(name):
    df = pd.read_csv(f'data/{name}.csv')
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.to_csv(f'data/cleaned_{name}.csv', index=False)
    print(f"{name} cleaned and saved.")

for file in ['matches', 'deliveries', 'teams', 'teamwise_home_and_away']:
    clean_and_save(file)
