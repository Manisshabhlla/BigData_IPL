from google.cloud import bigquery
import pandas as pd

client = bigquery.Client()
dataset_id = 'ipl_dataset'
client.create_dataset(dataset_id, exists_ok=True)

files = {
    'matches': 'cleaned_matches.csv',
    'deliveries': 'cleaned_deliveries.csv',
    'teams': 'cleaned_teams.csv',
    'home_away': 'cleaned_teamwise_home_and_away.csv'
}

for table, file in files.items():
    df = pd.read_csv(f'data/{file}')
    table_id = f"{dataset_id}.ipl_{table}"
    client.load_table_from_dataframe(df, table_id).result()
    print(f"Uploaded {file} to {table_id}")
