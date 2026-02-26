import sys
import pandas as pd

month = int(sys.argv[1])

pd = pd.DataFrame({"day": [1, 2], "num_passangers": [3, 4]})
pd["month"] = month
print(pd.head())
pd.to_parquet(f"day_{month}.parquet")

print(f"Hello World, month={month}")