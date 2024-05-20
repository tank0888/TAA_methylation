## 2024/2/5 
## リピートの帰属先の数を考慮

import pandas as pd
import os
import re

prot_name = "AtaA"
prot_seq = "MNKIYKVIWNATLLAWVAVSELAKGKTKSTTSKSKAKSLSSSVIVGGIILTTPLSLIAATVQVGGGTNSGTTATASTNCADLYNYQNPENSGSGAAGNYNAGNPSVCSIAIGENAQGGTSGTGGSPGIAIGGNSKATGGLSVAIGGYAQATNVGSIALGTAALSSGFNSLAISRQAAATNNYSIAIGTTSVSKGVGSIAMGHSTNASGDQSIAIGSSDAVNSATATTTYDGTTNTQASGSKSIAIGASAKASTNNSIALGAGSVTSAQSGNSYLTGVGASATNGVVSVGTSTATRRIQNVADGSAASDAVTVAQLDKAYDDTNGRLAAALGTGSGAAYNAANNTYTAPTNIGGTGKNTIDDAIKATQRSVVAGSNIVVTPTTASDGSISYSVATSATPTFTSITVNNAPTAGTDATNKTYVDSKAAASRTEVAAGSNVSGVVKTTGANGQDVYTVNANGTTASAGSSAVTVTPGTKDANNVTDYKVDLSATTKTDIQKGVDAKNAVDTAGLKFKGDTATTSNTKKLGDTVSITGDTNISTVATTDGVQVKLNPNLDLGATGSVKTGNTTINNAGVTADQVTVGGVVINNTSGINAGGKAITNVAAPTNNTDAANKKYVDDAGTALTNLGFGLKAQDGTTVNKKLGEAVDIVGSNSNISTKVNAGKVEVALSNTLDLGTTGSVTTGSTVINNAGVTATQVTANKVTINNAPTAGTDATNKTYVDSKAAASRTEVAAGSNVSGVVKTTGANGQDIYAVNANGTTASAGSSAVTVTPGTKDANNVTDYKVDLSATTKTDIQKGVDAKNAVDTAGLKFKGDTATTSNTKKLGDTVSITGDTNISTVATTDGVQVKLNPNLDLGATGSVKTGNTTINNAGVTADQVTVGGVVINNTSGINAGGKAITNVAAPTNNTDAANKKYVDDAGTALTNLGFGLKAQDGTTVNKKLGEAVDIVGSNSNISTKVNAGKVEVALSNTLDLGTTGSVTTGSTVINNAGVTATQVTANKVTVNNAPTAGTDATNKTYVDSKAAASRTEVAAGSNVSGVVKTTGANGQDVYTVNANGTTASAGSSAVTVTPGTKDANNVTDYKVDLSATTKTDIQKGVDAKNAVDTAGLKFKGDTATTSNTKKLGDTVSITGDTNISTVATTDGVQVKLNPNLDLGATGSVKTGNTTINNAGVTADQVTVGGVVINNTSGINAGGKAITNVAAPTNNTDAANKKYVDDAGTALTNLGFGLKAQDGTTVNKKLGEAVEVVGADSNITTKVAGGQVAIELNKNLNNLTGITVNDGTNGTNGSTVIGKDGISVKDGSGNTIAGVDNTALTVKDGSGNTETSINQAINTLNAAQGETDKFAVKYDKNADGSVNYNNITLAGTTASSTQDATTGKITTTGGTSLNNVASAGDYKDVANASKGVNAGDLNNAVVDATNAATSKGFALQAADGAKVQKNLGEAVEVVGADSNITTKVAGGQVAIELNKNLNNLTGITVNDGTNGTNGSTVIGKDGISVKDGSGNTIAGVDNTALTVKDGSGNTETSINQAINTLNAAQGETDKFAVKYDKNTDGSTNYNSITAGNGNGTAATIGTDTAGNSVVTSGGTKISNVANGVNASDAVNKGQLDSLSTGLTNTGFGLKAADGNTVNKKLGEAVDVVGADSNITTKVAGGQVAIELNKNLNNLTGITVNDGTNGTNGSTVIGKDGISIKDGSGNTIAGVDNTALTVKDGSGNTETSINQAINTLNAAQGETDKFAVKYDKNADGSANYNNITLAGTTASSTQDATTGKITTTGGTSLNNVASAGDYKDVANASKGVNAGDLNNAVVDATNAATSKGFALQAADGAKVQKNLGEAVEVVGADSNITTKVVGGQVAIELNKNLNNLTGITVNDGTNGTNGSTVIGKDGISVKDGSGNTIAGVDNTALTVKDGSGNTETSINQAINTLNAAQGETDKFAVKYDKNADGSVNYNNITLAGTTASSTQDATTGKITTTGGTSLNNVASAGDYKDVANASKGVNAGDLNNAVVDATNAATSKGFALQAADGAKVQKNLGEAVEVVGADSNITTKVAGGQVAIELNKNLNNLTGITVNDGTNGTNGSTVIGKDGISVKDGSGNTIAGVDNTALTVKDGSGNTETSINQAINTLNAAQGETDKFAVKYDKNADGSVNYNNITLAGTTASSTQDATTGKITTTGGTSLNNVASAGDYKDVANASKGVNAGDLNNAVVDATNAATSKGFALQAADGAKVQKNLGEAVEVVGADSNITTKVAGGQVAIELNKNLNNLTGITVNDGTNGTNGSTVIGKDGISVKDGSGNTIAGVDNTALTVKDGSGNTETSINQAINTLNAAQGETDKFAVKYDKNADGSANYNNVTLAGTNGTIISNVKAGAVTSTSTDAINGSQLYGVANSVKNAIGGSTTIDATTGAITTTNIGGTGSNTIDGAISSIKDSATKAKTTVSAGDNVVVTSGTNADGSTNYEVATAKDVNFDKVTVGSVVVDKSSNTIKGLSNTTWNGTAVSGQAATEDQLKTVSDAQGETDKFAVKYDKNADGSANYNSITAGNGNGTAATIGTDTAGNSVVTSGGTKISNVANGVNASDAVNKGQLDSLSTGLTNTGFGLKAADGNTVNKKLGEAVDVVGADSNITTKVAGGQVAIELNKNLNNLTGITVNDGTNGTNGSTVIGKDGISIKDGSGNTIAGVDNTALTVKDSSGNTETSINQAINTLNAAQGETDKFAVKYDKNADGSVNYNNVTLAGTNGTIIRNVKAGAVTSTSTDAINGSQLYDIANSVKNAIGGSTTRDVTTGAITTTNIGGTGSNTIDGAISSIKDSATKAKTTISAGDNVVVTSGTNADGSTNYEVATAKDVNFDKVTVGNVVVDKANDTIQGLSNKDLNSTDFATKGRAATEEQLKAVITSNITEVVDGNGNKVNIIDQVVNTKPDNKNQDSLFLTYDKQGQETTDRLTIGQTVQKMNTDGIKFFHTNADTSKGDLGTTNDSSAGGLNSTAIGVNAIVANGADSSVALGHNTKVNGKQSIAIGSGAEALGNQSISIGTGNKVTGDHSGAIGDPTIVNGANSYSVGNNNQVLTDDTFVLGNNVTKTIAGSVVLGNGSAATTGAGEAGYALSVATNADKAAITKTTSSTGAVAVGDASSGIYRQITGVAAGSVDSDAVNVAQLKAVGNQVVTTQTTLVNSLGGNAKVNADGTITGPTYNVAQGNQTNVGDALTALDNAINTAATTSKSTVSNGQNIVVSKSKNADGSDNYEVSTAKDLTVDSVKAGDTVLNNAGITIGNNAVVLNNTGLTISGGPSVTLAGIDAGNKTIQNVANAVNATDAVNKGQLDSAINNVNNNVNELANNAVKYDDASKDKITLGGGATGTTITNVKDGTVAQGSKDAVNGGQLWNVQQQVDQNTTDISNIKNDINNGTVGLVQQAGKDAPVTVAKDTGGTTVNVAGTDGNRVVTGVKEGAVNATSKDAVNGSQLNTTNQAVVNYLGGGAGYDNITGSFTAPSYTVGDSKYNNVGGAIDALNQADQALNSKIDNVSNKLDNAFRITNNRIDDVEKKANAGIAAAMALESAPYVPGKYTYAAGAAYHGGENAVGVTLRKTADNGRWSITGGVAAASQGDASVRIGISGVID" 
folder_path = "C:\Users\Shori INOUE\OneDrive\ドキュメント\Python_script\202312LCMS\S3\output1"


file_names = os.listdir(folder_path)
for file_name in file_names: 
    if len(file_name.split("_")) < 3:
        continue
    if file_name.split("_")[2] == "opt.csv":
        sample_name = file_name.split("_")[1]
        df1 = pd.read_csv(f"{folder_path}/{file_name}")
        
        Ksite = [i + 1 for i, char in enumerate(prot_seq) if char == "K"]
        data = {'Ksite': Ksite}
        df2 = pd.DataFrame(data)
        df2['Kabc_total'] = float(0)
        df2['Kabc_mono'] = float(0)
        df2['Kabc_di'] = float(0)
        df2['Kabc_tri'] = float(0)

        # 
        for i in range(len(df1["Sequence"])):
            abundance = float(df1.iloc[i]["Abundance"])

            pept_pos = df1.iloc[i]["Positions"].split("[")
            pept_pos.pop(0)
            pept_pos = [int(i.split('-')[0]) for i in pept_pos]
            abundance = abundance/len(pept_pos) ## 2024/2/5追加
 
            # 検出された全リシン残基の計算
            pept_seq = df1.iloc[i]["Sequence"].split(".")[1]
            resi_pos = [i + 1 for i, char in enumerate(pept_seq) if char == 'K'] 
            for h in resi_pos:
                for j in pept_pos:
                    position = h + j -1
                    df2.loc[df2['Ksite'] == int(position), 'Kabc_total'] += abundance
        
            # 修飾残基の計算
            Modi = str(df1.iloc[i]["Modifications"])
            if "Trimethyl" in Modi:
                ModiT = Modi.split("Trimethyl [")
                ModiT_l = re.findall(r'K(\d+)\((\d+)\)', ModiT[1])
                for pos, rate in ModiT_l:
                    for j in pept_pos:
                        position = int(pos) + j -1
                        df2.loc[df2['Ksite'] == int(position), 'Kabc_tri'] += abundance * int(rate)/100
                Modi = ModiT[0]
                
            if "Dimethyl" in Modi:
                ModiT= Modi.split("Dimethyl [")
                ModiT_l = re.findall(r'K(\d+)\((\d+)\)', ModiT[1])
                for pos, rate in ModiT_l:
                    for j in pept_pos:
                        position = int(pos) + j -1
                        df2.loc[df2['Ksite'] == int(position), 'Kabc_di'] += abundance * int(rate)/100
                Modi = ModiT[0]
                
            if "Methyl" in Modi:
                ModiT = Modi.split("Methyl [")
                ModiT_l = re.findall(r'K(\d+)\((\d+)\)', ModiT[1])
                for pos, rate in ModiT_l:
                    for j in pept_pos:
                        # print(f"{int(pos)} + {j} - 1")
                        position = int(pos) + j -1
                        if int(position) in df2['Ksite'].values:
                            df2.loc[df2['Ksite'] == int(position), 'Kabc_mono'] += abundance * int(rate)/100
                        else:
                            print(f"{position} is not in AtaA")
                Modi = ModiT[0]
                        



                    # # manual操作の際のpositionのミスの検出
                    # if position in df2['Ksite'].values:
                    #     df2.loc[df2['Ksite'] == int(position), 'Kabc_total'] += abundance
                    # else:
                    #      print(f"{position} is not in AtaA")
        



        df2["Kabc_non"] = df2["Kabc_total"] - df2["Kabc_mono"] - df2["Kabc_di"] - df2["Kabc_tri"]
        df2['Kratio_mono'] = float(0)
        df2['Kratio_di'] = float(0)
        df2['Kratio_tri'] = float(0)
        df2['Kratio_non'] = float(0)
        for i in range(len(df2)):
            total = float(df2.iloc[i]["Kabc_total"])
            if total > 0:
                df2.at[i, "Kratio_mono"]  = df2.iloc[i]["Kabc_mono"] / total
                df2.at[i, "Kratio_di"]  = df2.iloc[i]["Kabc_di"] / total
                df2.at[i, "Kratio_tri"]  = df2.iloc[i]["Kabc_tri"] / total
                df2.at[i, "Kratio_non"]  = df2.iloc[i]["Kabc_non"] / total



        df2.to_csv(f"output2_24005/output2_{sample_name}.csv")




