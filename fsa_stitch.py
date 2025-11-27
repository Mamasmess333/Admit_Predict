import pandas as pd
from pathlib import Path
base = Path('College_Scorecard_Most_Recent_Institutional_Data/Data_Assets/external/fsa')
files = [
    ('dl-dashboard-ay2022-2023-q1.xls', 'Q1'),
    ('dl-dashboard-ay2022-2023-q2.xls', 'Q2'),
    ('dl-dashboard-ay2022-2023-q3.xls', 'Q3'),
    ('dl-dashboard-ay2022-2023-q4.xls', 'Q4')
]
frames = []
for fname, quarter in files:
    path = base / fname
    df = pd.read_excel(path, header=[5,6])
    df.columns = ['{}__{}'.format(str(a).strip(), str(b).strip()) if a.strip() else b.strip()
                  for a,b in df.columns]
    df = df.rename(columns={'OPE ID':'OPEID', 'School':'School', 'State':'State', 'Zip Code':'ZipCode', 'School Type':'SchoolType'})
    df = df[df['OPEID'].notna()]
    df = df[df['OPEID'] != 'Grand Total']
    df['Quarter'] = quarter
    frames.append(df)

combined = pd.concat(frames, ignore_index=True)
print('Combined shape (with headers):', combined.shape)
print('Columns:', list(combined.columns))
print('\nSample rows:')
print(combined.head())

id_cols = ['OPEID','School','State','ZipCode','SchoolType']
numeric_cols = [c for c in combined.columns if c not in id_cols + ['Quarter']]
combined[numeric_cols] = combined[numeric_cols].replace('-', 0)
combined[numeric_cols] = combined[numeric_cols].apply(pd.to_numeric, errors='coerce')
combined['OPEID'] = combined['OPEID'].astype(str).str.zfill(8)

agg_sum = combined.groupby('OPEID', as_index=False)[numeric_cols].sum(min_count=1)
agg_sum = agg_sum.merge(
    combined.groupby('OPEID')['Quarter'].nunique().reset_index(name='quarters_reporting'),
    on='OPEID', how='left'
)
# keep reference columns
ref_cols = combined.groupby('OPEID').agg({'School':'first','State':'first','ZipCode':'first','SchoolType':'first'}).reset_index()
agg_sum = ref_cols.merge(agg_sum, on='OPEID', how='right')

out_path = base / 'dl_dashboard_ay2022_2023_fullyear.csv'
agg_sum.to_csv(out_path, index=False)
print('\nAggregated shape:', agg_sum.shape)
print('Saved aggregated file to', out_path)
