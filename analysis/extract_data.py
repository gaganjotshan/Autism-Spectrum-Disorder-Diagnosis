import pandas as pd
import numpy as np
from matplotlib import pyplot

df_pheno = pd.read_csv("ABIDEII/ABIDEII_Composite_Phenotypic.csv", encoding='unicode_escape')
#Total Coulmns
columns_pheno = df_pheno.columns
print("total", df_pheno.size)


#Total Males
males = df_pheno[df_pheno['SEX'] == 1]
print("males", len(males))
## Autistic Males
males_autistic = males[males['DX_GROUP'] == 1]
print("males_autistic", len(males_autistic))
## Control Males
males_control = males[males['DX_GROUP'] == 2]
print("males_control", len(males_control))

#Total Females
females = df_pheno[df_pheno['SEX'] == 2]
print("females", len(females))
## Autistic Females
females_autistic = females[females['DX_GROUP'] == 1]
print("females_autistic", len(females_autistic))
## Control Females
females_controls = females[females['DX_GROUP'] == 2]
print("females_controls", len(females_controls))


#Filters
## Age Filter 
over_40 = df_pheno[df_pheno['AGE_AT_SCAN '] > 40]
below_40 = df_pheno[df_pheno['AGE_AT_SCAN '] <= 40]
print("over_40", len(over_40))
print("below_40", len(below_40))
print("f_over_40", len(females[females['AGE_AT_SCAN '] > 40]))
print("f_below_40", len(females[females['AGE_AT_SCAN '] <= 40]))
print("m_over_40", len(males[males['AGE_AT_SCAN '] > 40]))
print("m_below_40", len(males[males['AGE_AT_SCAN '] <= 40]))
## IQ Filter
normal_iq = df_pheno[df_pheno['FIQ'] > 80]
below_avg_iq = df_pheno[df_pheno['FIQ'] <= 80]
print("normal_iq", len(normal_iq))
print("below_avg_iq", len(below_avg_iq))
print("f_normal_iq", len(normal_iq[normal_iq['SEX'] == 2]))
print("f_below_avg_iq", len(below_avg_iq[below_avg_iq['SEX'] == 2]))


#Filterd Data Set
Females_below40 = females[females['AGE_AT_SCAN '] <= 40]
Females_IQ_40 = Females_below40[Females_below40['FIQ'] > 80]
print('filtered females', len(Females_IQ_40))
Females_IQ_40 = males[males['AGE_AT_SCAN '] <= 40]
Males_IQ_40 = Males_below40[Males_below40['FIQ'] > 80]
print('filtered males', len(Males_IQ_40))
## vertical concatinate
filter_data = pd.concat([Females_IQ_40, Males_IQ_40], axis=0)
print('filter_data size', len(filter_data))
display(filter_data)

# SubIDs (These are not performed on filtered data, i,e filter_data)
## Males
subid = df_pheno.SUB_ID
print("subid", len(subid))
subid_male = df_pheno.SUB_ID[df_pheno['SEX'] == 1]
print("subid_male", len(subid_male))
## Females
subid_female = df_pheno.SUB_ID[df_pheno['SEX'] == 2]
print("subid_female", len(subid_female))
print(subid_female)
#print("subid male and female", len(subid_male+subid_female))


fautism_data = females.SUB_ID[females['DX_GROUP'] == 1]
print('fautism_data',len(fautism_data))
print(fautism_data)

#Pick Male Autistic samples = Length(Female Autistic).  ?? filters not applied
import random
mdata = males.SUB_ID[males['DX_GROUP'] == 1]
mautism_data = mdata.sample(len(fautism_data))
print('mautism_data',len(mautism_data))
print(mautism_data)
