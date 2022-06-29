import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from src.data import intersc

def lo_siento():
  print(" sirves ? ")
  df = intersc()

  crr = df[['calle_id', 'start_lat', 'start_log', 'end_lat', 'end_log', 'distancia', 'velocidad', 'costo']].copy()
  crr['start'] = crr[['start_lat', 'start_log']].apply(lambda x: (x[0], x[1]), axis=1)
  crr['end'] = crr[['end_lat', 'end_log']].apply(lambda x: (x[0], x[1]), axis=1)

  a = crr.groupby(["calle_id"])['start'].apply(set)
  b = crr.groupby(["calle_id"])['end'].apply(set)
  c = crr.groupby(["calle_id"])['distancia'].sum()
  d = crr.groupby(["calle_id"])['velocidad'].mean()
  e = crr.groupby(["calle_id"])['costo'].mean()

  inter = pd.DataFrame(a).join(b, on='calle_id').join(c, on='calle_id').join(d, on='calle_id').join(e, on='calle_id')
  inter['id'] = [x[0] for x in inter.iterrows()]

  cols = ['start', 'end']

  def add_set(start, end):
    for i in end:
      start.add(i)
    return start

  inter['combined'] = inter[cols].apply(
      lambda row: add_set(row.values[0], row.values[1]), axis=1)

  inter.to_csv('data/inter.csv', index=False)


  new_df = inter[['id', 'distancia', 'velocidad', 'costo']].copy()
  start = []
  end = []

  for row in inter.itertuples():
      start.append([ id
                for x, id in zip(inter['combined'], inter['id'])  
                if len(x.intersection(row.combined)) > 0 and id != row.id])
      

  new_df['paths'] = start
  #new_df['end'] = end
  new_df
  new_df.head()

  cars_per_km = [50, 200, 100, 250, 150]
  crr_time = 0 #number between 0 - 23 => 12am - 11pm

  new_df['factor_trafico'] = (cars_per_km[crr_time] * new_df['distancia'])  /  (cars_per_km[crr_time] * new_df['distancia'] * new_df['velocidad'] * 0.75 * new_df['costo'])
  new_df['factor_trafico'] = new_df['factor_trafico'].astype(int)

  scaler = MinMaxScaler()

  new_df['factor_trafico'] =(scaler.fit_transform(new_df['factor_trafico'].values.reshape(-1,1)) * 100).astype(int)
  new_df.describe()


  new_df.to_csv('data/Lima-calles-trafico.csv', sep=";", index=False)
  
  return (new_df, inter)
