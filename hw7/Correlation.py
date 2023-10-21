import numpy as np
import csv


dataset_tw = []
dataset_mediatek = []
dataset_largen = []
dataset_tsmc = []

shares = ["tw", "tsmc", "largen", "mediatek"]

for share in shares :
    with open(f"./{share}910.csv", newline='') as csvfile:
        rows = csv.reader(csvfile)
        if share == "tw":
            for row in rows:
                dataset_tw.append(float(row[1]))
        elif share == "tsmc":
            for row in rows:
                dataset_tsmc.append(float(row[1]))
        elif share == "largen":
            for row in rows:
                dataset_largen.append(float(row[1]))
        elif share == "mediatek":
            for row in rows:
                dataset_mediatek.append(float(row[1]))


corr_tt = 0
corr_tm = 0
corr_tl = 0


print("Dataset length correct!")
corr_tt = np.corrcoef(dataset_tw, dataset_tsmc)
corr_tm = np.corrcoef(dataset_tw, dataset_mediatek)
corr_tl = np.corrcoef(dataset_tw, dataset_largen)
print(f"Correlation for 0050 & 2330/2454/3008 is: {corr_tt[0]}, {corr_tm[0]}, {corr_tl[0]}")





