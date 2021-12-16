import pandas as pd

def process_group(group):
    group = group.set_index("Date")
    group = group.drop(["District Name"], axis="columns")
    return group

def main():
    ts = pd.read_csv("../data/timeseries.csv", sep=',', index_col="2")
    ts.drop("A", axis="columns", inplace=True)
    tst = ts.transpose()
    groups = tst.groupby("District Name")
    for name, group in groups:
        processed = process_group(group)
        processed.to_csv(f"../data/timeseries_{name}.csv")

if __name__ == "__main__":
    main()
