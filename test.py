import pandas as pd
    # Sample data
df = pd.read_csv("transport.csv")

Bus_route = "Sankarankovil Mukku"

filtered_df = df[df['Bus Stop'] == Bus_route]

Bus_stop = filtered_df['Time (AM)'].unique()

busno = filtered_df['BUS NO'].unique()

print(Bus_stop,busno)


