import os
import pandas as pd

def merge_files(input_folder, file_names):
    dataframes = []
    for file_name in file_names:
        file_path = os.path.join(input_folder, file_name)
        df = pd.read_csv(file_path)
        dataframes.append(df)

    df_concat = pd.concat(dataframes)
    df_mean = df_concat.groupby('Position of residues in AtaA').mean().reset_index()

    df_mean["Abundance of unmethylated residue"] = df_mean["Total abundance"] - df_mean["Abundance of monomethylated residue"] - df_mean["Abundance of dimethylated residue"] - df_mean["Abundance of trimethylated residue"]
    df_mean['Ratio of monomethylated residue'] = df_mean['Abundance of monomethylated residue'] / df_mean['Total abundance']
    df_mean['Ratio of dimethylated residue'] = df_mean['Abundance of dimethylated residue'] / df_mean['Total abundance']
    df_mean['Ratio of trimethylated residue'] = df_mean['Abundance of trimethylated residue'] / df_mean['Total abundance']
    df_mean['Ratio of unmethylated residue'] = df_mean['Abundance of unmethylated residue'] / df_mean['Total abundance']

    df_mean.fillna(0, inplace=True)
    
    return df_mean

def main():
    input_folder = "output2"
    output_folder = "output3"
    file_names = ["e3.csv", "e4.csv"] # file names to merge
    data_name = "WT" # names of merged data 
    
    df_out = merge_files(input_folder, file_names)
    df_out.to_csv(f"{output_folder}/{data_name}.csv")   
    

if __name__ == "__main__":
    main()

