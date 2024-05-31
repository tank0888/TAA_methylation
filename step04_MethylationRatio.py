import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def create_png(file_path, output_path):
    # Load and prepare data
    df = pd.read_csv(file_path)
    labels = df['Position of residues in AtaA'].apply(str).tolist()
    half_len = len(labels) // 2
    positions = range(half_len)
    ratios = [
        'Ratio of monomethylated residue',
        'Ratio of dimethylated residue', 
        'Ratio of trimethylated residue',
        'Ratio of unmethylated residue'
        ]
    values = {ratio: (df[ratio] * 100).tolist() for ratio in ratios}

    # Setup figure and axes
    mpl.rcParams['axes.xmargin'] = 0 
    mpl.rcParams['axes.ymargin'] = 0 
    fig, axes = plt.subplots(2, 1, figsize=(20, 5))
    plt.subplots_adjust(left=0.05, right=0.95, bottom=0.25, top=0.75)
    colors = ['blue', 'green', 'red', 'sandybrown']

    # Plot data
    for i, ax in enumerate(axes):
        bottoms = np.zeros(half_len)
        for ratio, color in zip(ratios, colors):
            current_values = np.array(values[ratio][i * half_len:(i + 1) * half_len])
            ax.bar(positions, current_values, label=ratio.split(' ')[2], color=color, bottom=bottoms)
            bottoms += current_values

        ax.set_xticks(positions)
        ax.tick_params(labelsize=14)
        ax.set_xticklabels(labels[:half_len] if i == 0 else labels[half_len:], rotation=90, fontsize=10)
        ax.set_ylabel('Methylation (%)', fontsize=16)
        ax.set_yticks([0, 25, 50, 75, 100])

    axes[1].set_xlabel('Position of lysine residues in AtaA', fontsize=16)
    
    plt.tight_layout()
    fig.savefig(output_path, bbox_inches='tight')

def main():
    input_folder = "output3"   
    output_folder = "output4"
    
    for file_name in os.listdir(input_folder): 
        if file_name.endswith(".csv"):
            output_path = f"{output_folder}/{file_name.split(".")[0]}.png"
            create_png(os.path.join(input_folder, file_name), output_path)

    
if __name__ == "__main__":
    main()
