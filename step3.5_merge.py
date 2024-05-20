import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

folder_path = "output2"
folder_path_out = "output2_1"

# file_names = ["output2_e13.csv", "output2_e14.csv"]
# sample_name = "WT2"

# file_names = ["output2_e15.csv", "output2_e16.csv"]
# sample_name = "KO2"

file_names = ["output2_e17.csv", "output2_e18.csv"]
sample_name = "Comp2"

# file_names = ["output2_e3.csv", "output2_e4.csv"]
# sample_name = "WT"

# file_names = ["output2_e5.csv", "output2_e6.csv"]
# sample_name = "KO"

# file_names = ["output2_e7.csv", "output2_e8.csv"]
# sample_name = "Comp"




rep1_name = file_names.pop(0)
rep2_name = file_names.pop(0)
df1 = pd.read_csv(f"{folder_path}/{rep1_name}")
df2 = pd.read_csv(f"{folder_path}/{rep2_name}")

dfm = pd.DataFrame()
dfm["Ksite"] = df1["Ksite"]
dfm["Kabc_mono"] = (df1["Kabc_mono"] + df2["Kabc_mono"]) / 2
dfm["Kabc_di"] = (df1["Kabc_di"] + df2["Kabc_di"]) / 2
dfm["Kabc_tri"] = (df1["Kabc_tri"] + df2["Kabc_tri"]) / 2
dfm["Kabc_total"] = (df1["Kabc_total"] + df2["Kabc_total"]) / 2

dfm["Kabc_non"] = dfm["Kabc_total"] - dfm["Kabc_mono"] - dfm["Kabc_di"] - dfm["Kabc_tri"]
dfm['Kratio_mono'] = float(0)
dfm['Kratio_di'] = float(0)
dfm['Kratio_tri'] = float(0)
dfm['Kratio_non'] = float(0)
for i in range(len(dfm)):
    total = float(dfm.iloc[i]["Kabc_total"])
    if total > 0:
        dfm.at[i, "Kratio_mono"]  = dfm.iloc[i]["Kabc_mono"] / total
        dfm.at[i, "Kratio_di"]  = dfm.iloc[i]["Kabc_di"] / total
        dfm.at[i, "Kratio_tri"]  = dfm.iloc[i]["Kabc_tri"] / total
        dfm.at[i, "Kratio_non"]  = dfm.iloc[i]["Kabc_non"] / total

dfm.to_csv(f"{folder_path_out}/output2_{sample_name}.csv")