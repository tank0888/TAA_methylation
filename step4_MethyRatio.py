import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# folder_path = "output2"
folder_path = "C:/Users/Shori INOUE/OneDrive/ドキュメント/Python_script/202312LCMS/S3/output2_2"

file_names = os.listdir(folder_path)
# file_names = ["output2_e13.csv", "output2_e14.csv"]

for file_name in file_names: 
    if file_name.split(".")[-1] != "csv":
        continue 

    sample_name = file_name.split("_")[1]
    df2 = pd.read_csv(f"{folder_path}/{file_name}")

    # df2 = df2.iloc[8:] # SPを除く

    labels = df2['Ksite'].to_list()
    labels = [str(i) for i in labels]
    positions = range(len(labels)//2)
    mono_vals = [float(i*100) for i in df2["Kratio_mono"].to_list()]
    di_vals = [float(i*100) for i in df2["Kratio_di"].to_list()]
    tri_vals = [float(i*100) for i in df2["Kratio_tri"].to_list()]
    non_vals = [float(i*100) for i in df2["Kratio_non"].to_list()]

    lab1, lab2 = labels[:len(labels)//2], labels[len(labels)//2:]
    mono1, mono2 = mono_vals[:len(mono_vals)//2], mono_vals[len(mono_vals)//2:]
    di1, di2 = di_vals[:len(di_vals)//2], di_vals[len(di_vals)//2:]
    tri1, tri2 = tri_vals[:len(tri_vals)//2], tri_vals[len(tri_vals)//2:]
    non1, non2 = non_vals[:len(non_vals)//2], non_vals[len(non_vals)//2:]


    bar_width = 0.9
    fig =plt.figure(figsize=(20, 5))
    mpl.rcParams['axes.xmargin'] = 0 # 棒グラフと縦軸の隙間
    mpl.rcParams['axes.ymargin'] = 0 
    # plt.rcParams['figure.subplot.left'] = 0.15 #プロットエリア外の余白(%) 
    plt.subplots_adjust(left=0.25, right=0.75, bottom=0.25, top=0.75)

    ax1 = fig.add_subplot(2, 1, 1)
    ax1.bar(positions, mono1, bar_width, color='blue', label='mono-Methyl')
    ax1.bar(positions, di1, bar_width, bottom=mono1, color='green', label='di-Methyl')
    ax1.bar(positions, tri1, bar_width, bottom=di1, color='red', label='tri-Methyl')
    ax1.bar(positions, non1, bar_width, bottom=np.array(mono1)+np.array(di1)+np.array(tri1), color='sandybrown', label='non-Methyl')

    # ax1.set_title('Methylation status at K_pos')
    ax1.set_xticks(positions)
    ax1.tick_params(labelsize=14)
    ax1.set_xticklabels(lab1, rotation=90, fontsize=10)
    ax1.set_yticks([0, 25, 50, 75, 100])
    ax1.set_ylabel('Methylation (%)', fontsize=16)
    # ax1.set_xlabel('Position')
    # ax1.legend()


    ax2 = fig.add_subplot(2, 1, 2)
    ax2.bar(positions, mono2, bar_width, color='blue', label='mono-Methyl')
    ax2.bar(positions, di2, bar_width, bottom=mono2, color='green', label='di-Methyl')
    ax2.bar(positions, tri2, bar_width, bottom=di2, color='red', label='tri-Methyl')
    ax2.bar(positions, non2, bar_width, bottom=np.array(mono2)+np.array(di2)+np.array(tri2), color='sandybrown', label='non-Methyl')

    # ax2.set_title('Methylation status at K_pos')
    ax2.set_xticks(positions)
    ax2.tick_params(labelsize=14)
    ax2.set_xticklabels(lab2, rotation=90, fontsize=10)
    ax2.set_yticks([0, 25, 50, 75, 100])
    ax2.set_ylabel('Methylation (%)', fontsize=16)
    ax2.set_xlabel('Position of lysine residues in AtaA', fontsize=16)
    # ax2.legend()


    plt.tight_layout()
    fig.savefig(f"C:/Users/Shori INOUE/OneDrive/ドキュメント/Python_script/202312LCMS/S3/output3/output3_{sample_name}.png", bbox_inches='tight')
    # plt.show()
