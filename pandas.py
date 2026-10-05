import pandas

# Series: 1 dimensional data

data = [100, 200, 300]

series = pandas.Series(data, index=["a","b","c"])

print(series)