import pandas as pd

dates = ['2025-06-01', '2025-06-02', '2025-06-03']
timeseries = pd.to_datetime(dates)

print(timeseries)
