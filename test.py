
import pandas as pd
import pandasql as pdsql
from datetime import datetime

excel_file = r"C:\Users\Ram_DFID\Desktop\PaperWritingTraining\FocusGroupData.xlsx"

df_civil_society = pd.read_excel(excel_file, "Civil Society")
df_community_consultation = pd.read_excel(excel_file, "Community Consultation")
df_local_government = pd.read_excel(excel_file, "Local Government")

df_list = [
    {"df": df_civil_society, "focus_group_name":"Civil Society"},
    {"df": df_community_consultation, "focus_group_name":"Community Consultation"},
    {"df": df_local_government, "focus_group_name":"Local Government"}
    ]
df_name_list = ["Civil Society", "Community Consultation", "Local Government"]
cols = [
    "Response ID",
    "5&9.  Risk Area / Community",
    "6. Urban or Rural",
    "T1",
    "1:T1C","2:T1C","3:T1C",
    "1:T1A","2:T1A","3:T1A",
    "1:T1B","2:T1B","3:T1B",
    "T2",
    "1:T2C","2:T2C","3:T2C",
    "1:T2A","2:T2A","3:T2A",
    "1:T2B","2:T2B","3:T2B",
    "T3",
    "1:T3C","2:T3C","3:T3C",
    "1:T3A","2:T3A","3:T3A",
    "1:T3B","2:T3B","3:T3B"
    ]



print ("Civil Society")
cols_civil_society = df_civil_society.columns
for col in cols:
    if col not in cols_civil_society:
        print ("<< %s >> colum not found" %(col))

    else:
        print ("<< %s >> OK" %(col))
        

print ("Community Consultation")
cols_community_consultation = df_community_consultation.columns
for col in cols:
    if col not in cols_community_consultation:
        print ("<< %s >> colum not found" %(col))

    else:
        print ("<< %s >> OK" %(col))

print ("Local Government")
cols_local_government = df_local_government.columns
for col in cols:
    if col not in cols_local_government:
        print ("<< %s >> colum not found" %(col))

    else:
        print ("<< %s >> OK" %(col))




def combine_data(df_list, df_name_list, filename):
    cols_dfObj = cols+['Focused Group']
    #+["Civil Society"+"Community Consultation"+"Local Government"]
    dfObj = pd.DataFrame([], columns=cols_dfObj)
    for item in df_list:    
        df = item["df"]
        focus_group_name = item["focus_group_name"]
        for index, row  in df.iterrows():
            dfObj_row = {}
            for col in cols:
                dfObj_row[col] =row[col]
                
            dfObj_row['Focused Group'] = focus_group_name

            
            if dfObj_row['Focused Group'] =="Civil Society":
                dfObj_row["Civil Society"] = 1

            if dfObj_row['Focused Group'] =="Community Consultation":
                dfObj_row["Community Consultation"] = 1

            if dfObj_row['Focused Group'] =="Local Government":
                dfObj_row["Local Government"] = 1

            
            
            dfObj = dfObj.append(dfObj_row, ignore_index=True)
        
        dfObj.to_excel(filename)

filename = r'FocusGroupData_Combined.xlsx'
combine_data(df_list, df_name_list, filename)
