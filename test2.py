
import pandas as pd
import pandasql as pdsql
from datetime import datetime

excel_file = r"C:\Users\Ram_DFID\Desktop\PaperWritingTraining\FocusGroupData.xlsx"

df_civil_society = pd.read_excel(excel_file, "Civil Society")
df_community_consultation = pd.read_excel(excel_file, "Community Consultation")
df_local_government = pd.read_excel(excel_file, "Local Government")

df_list = [
    {"df": df_civil_society, "survey_type":"Civil Society"},
    {"df": df_community_consultation, "survey_type":"Community Consultation"},
    {"df": df_local_government, "survey_type":"Local Government"}
    ]
df_name_list = ["Civil Society", "Community Consultation", "Local Government"]
cols = [
    "Response ID","Edit Links",
    #"Name of the enumerator",
    "2. Partner Organization",
    "3. National Coordinating Organisation (NCO)",
    "4. Country",
    "5&9.  Risk Area / Community",
    "6. Urban or Rural",
    "10. Survey Date - Please enter in format dd/mm/yyyy",
    "11. Survey reference number",
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
    "1:T3B","2:T3B","3:T3B",
    "1:Forecasting", "2:Forecasting", "3:Forecasting"
    ]


cols_age_group = [
    "14-17:14. Informant Age (how many participants per age group)",
    "18-24:14. Informant Age (how many participants per age group)",
    "25-34:14. Informant Age (how many participants per age group)",
    "35-44:14. Informant Age (how many participants per age group)",
    "45-64:14. Informant Age (how many participants per age group)",
    "65 plus:14. Informant Age (how many participants per age group)",
    ]

extra_cols_civil_society = ["14. Gender", "13. Informant’s Age"]
extra_cols_community_consultations=["13. Number of Participants in Group",
                                    "14 and below:14. Informant Age (how many participants per age group)",
                                    "14-17:14. Informant Age (how many participants per age group)",
                                    "18-24:14. Informant Age (how many participants per age group)",
                                    "25-34:14. Informant Age (how many participants per age group)",
                                    "35-44:14. Informant Age (how many participants per age group)",
                                    "45-64:14. Informant Age (how many participants per age group)",
                                    "65 plus:14. Informant Age (how many participants per age group)",
                                    "12. Consultation Group of"

                                    ]
                                    
                                    
extra_cols_local_gov = ["14. Gender", "13. Informant’s Age", "12. Name of Local Government Institution"]
                                    

print ("Civil Society")
cols_civil_society = df_civil_society.columns
for col in cols:
    if col not in cols_civil_society:
        print ("<< %s >> colum not found" %(col))

    else:
        pass
        #print ("<< %s >> OK" %(col))
        

print ("Community Consultation")
cols_community_consultation = df_community_consultation.columns
for col in cols:
    if col not in cols_community_consultation:
        print ("<< %s >> colum not found" %(col))

    else:
        pass
        #print ("<< %s >> OK" %(col))

print ("Local Government")
cols_local_government = df_local_government.columns
for col in cols:
    if col not in cols_local_government:
        print ("<< %s >> colum not found" %(col))
    else:
        pass
        #print ("<< %s >> OK" %(col))




def combine_data(df_list, df_name_list, filename):
    cols_dfObj = cols+["14. Gender","13. Number of Participants in Group"]+cols_age_group+["Male","Female"]+["Urban","Rural", "Urban_Participants","Rural_Participants"]+["Survey Type"]
    #+["Civil Society"+"Community Consultation"+"Local Government"]
    dfObj = pd.DataFrame([], columns=cols_dfObj)
    for item in df_list:    
        df = item["df"]
        survey_type = item["survey_type"]
        for index, row  in df.iterrows():
            dfObj_row = {}
            for col in cols:
                dfObj_row[col] =row[col]
                
            dfObj_row['Survey Type'] = survey_type
            if row["6. Urban or Rural"] == 'Rural':
                dfObj_row["Rural"]='YES'
            if row["6. Urban or Rural"] == 'Urban':
                dfObj_row["Urban"]='YES'
                
            if dfObj_row['Survey Type'] =="Civil Society":
                #dfObj_row["Civil Society"] = 1
                if row["13. Informant’s Age"] == "18-24":
                    dfObj_row["18-24:14. Informant Age (how many participants per age group)"] =1
                if row["13. Informant’s Age"] == "25-34":
                    dfObj_row["25-34:14. Informant Age (how many participants per age group)"] =1
                if row["13. Informant’s Age"] == "35-44":
                    dfObj_row["35-44:14. Informant Age (how many participants per age group)"] =1
                if row["13. Informant’s Age"] == "45-64":
                    dfObj_row["45-64:14. Informant Age (how many participants per age group)"] =1
                if row["13. Informant’s Age"] == "65 plus":
                    dfObj_row["65 plus:14. Informant Age (how many participants per age group)"] =1

                dfObj_row["13. Number of Participants in Group"] = 1
                if row["6. Urban or Rural"] == 'Rural':
                    dfObj_row["Rural_Participants"]=1
                if row["6. Urban or Rural"] == 'Urban':
                    dfObj_row["Urban_Participants"]=1

                
                dfObj_row["14. Gender"] = row["14. Gender"]
                if row["14. Gender"] == "Male":
                    dfObj_row["Male"]=1
                if row["14. Gender"] == "Female":
                    dfObj_row["Female"]=1
    


            if dfObj_row['Survey Type'] =="Community Consultation":
                #dfObj_row["Community Consultation"] = 1
                """
                if row["12. Consultation Group of"] == "Children & Youth":
                    dfObj_row["14 and below:14. Informant Age (how many participants per age group)"]
                """
                dfObj_row["18-24:14. Informant Age (how many participants per age group)"]=row["18-24:14. Informant Age (how many participants per age group)"]
                dfObj_row["25-34:14. Informant Age (how many participants per age group)"]=row["25-34:14. Informant Age (how many participants per age group)"]
                dfObj_row["35-44:14. Informant Age (how many participants per age group)"]=row["35-44:14. Informant Age (how many participants per age group)"]
                dfObj_row["45-64:14. Informant Age (how many participants per age group)"]=row["45-64:14. Informant Age (how many participants per age group)"]
                dfObj_row["65 plus:14. Informant Age (how many participants per age group)"]=row["65 plus:14. Informant Age (how many participants per age group)"]

                
                dfObj_row["13. Number of Participants in Group"] = row["13. Number of Participants in Group"]
                if row["6. Urban or Rural"] == 'Rural':
                    dfObj_row["Rural_Participants"]=row["13. Number of Participants in Group"]
                if row["6. Urban or Rural"] == 'Urban':
                    dfObj_row["Urban_Participants"]=row["13. Number of Participants in Group"]
                
                if row["12. Consultation Group of"] == "Women":
                    dfObj_row["14. Gender"] = "Female"
                    dfObj_row["Female"]=row["13. Number of Participants in Group"]

                   
                            
                    
                if row["12. Consultation Group of"] == "Men":
                    dfObj_row["14. Gender"] = "Male"
                    dfObj_row["Male"]=row["13. Number of Participants in Group"]
                
                
            if dfObj_row['Survey Type'] =="Local Government":
                #dfObj_row["Local Government"] = 1
                if row["13. Informant’s Age"] == "18-24":
                    dfObj_row["18-24:14. Informant Age (how many participants per age group)"] =1
                if row["13. Informant’s Age"] == "25-34":
                    dfObj_row["25-34:14. Informant Age (how many participants per age group)"] =1
                if row["13. Informant’s Age"] == "35-44":
                    dfObj_row["35-44:14. Informant Age (how many participants per age group)"] =1
                if row["13. Informant’s Age"] == "45-64":
                    dfObj_row["45-64:14. Informant Age (how many participants per age group)"] =1
                if row["13. Informant’s Age"] == "65 plus":
                    dfObj_row["65 plus:14. Informant Age (how many participants per age group)"] =1

                dfObj_row["13. Number of Participants in Group"] = 1
                if row["6. Urban or Rural"] == 'Rural':
                    dfObj_row["Rural_Participants"]=1
                if row["6. Urban or Rural"] == 'Urban':
                    dfObj_row["Urban_Participants"]=1
                    
                dfObj_row["14. Gender"] = row["14. Gender"]    
                if row["14. Gender"] == "Male":
                    dfObj_row["Male"]=1
                if row["14. Gender"] == "Female":
                    dfObj_row["Female"]=1
            
            dfObj = dfObj.append(dfObj_row, ignore_index=True)
        
        dfObj.to_excel(filename)

filename = r'FocusGroupData_Combined_test2.xlsx'
combine_data(df_list, df_name_list, filename)
