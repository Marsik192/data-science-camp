import pandas as pd 
import numpy as np 
  
def answer_one():
    return answer.head(15)

def answer_two():
    Top15 = answer_one()
    Top15.drop(Top15.columns[range(0, 10)], axis = 1, inplace= True)
    answer_two_series = pd.Series()
    answer_two_series = Top15.mean(axis = 1).sort_values(ascending = False)
    return answer_two_series

def answer_three():
    Top15 = answer_one()
    Top15.drop(Top15.columns[range(0, 10)], axis = 1, inplace= True)
    CountryRanked6th = Top15.loc['France']
    answer_number = CountryRanked6th.loc['2021'] - CountryRanked6th['2006']
    return answer_number


file_name = "Energy_Indicators.xls" 
Energy = pd.read_excel(file_name,skiprows = 17,sheet_name= "Energy",skipfooter = 38, 
usecols = (2,3,4,5), names= ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']) 
 
Energy["Energy Supply"] = Energy["Energy Supply"] * 1000000 # переводимо петаджоулі в гігаджоулі 
 
Energy = Energy.replace({'Country':{'Republic of Korea': 'South Korea', 'United States of America': 'United States', 
                            'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom', 
                            'China, Hong Kong Special Administrative Region': 'Hong Kong', 
                            'Bolivia (Plurinational State of)':'Bolivia', 
                            'Switzerland17':'Switzerland'}}) # міняємо назви країн 

CSVfile_name = "world_bank.csv" 
GDP = pd.read_csv(CSVfile_name, skiprows = 4) 
GDP = GDP.replace({'Korea, Rep.': 'South Korea',
'Iran, Islamic Rep.': 'Iran', 
'Hong Kong SAR, China': 'Hong Kong'})
GDP.drop(GDP.columns[range(4,50)], axis = 1, inplace= True)

Scimagojr_file = "Scimagojr Rank.xlsx" 
ScimEn = pd.read_excel(Scimagojr_file)

answer = pd.merge(ScimEn, Energy, how = 'outer', on = 'Country') 
answer = pd.merge(answer, GDP, how = 'outer', on = 'Country')

answer.drop(columns = ["Region", "Country Code", "Indicator Code", "Indicator Name"], axis = 1, inplace = True)
answer = answer.set_index(['Country'])

writer = pd.ExcelWriter("results check.xlsx") 
answer.to_excel(writer, sheet_name = "answer1") 
writer.save() 

answer_one()

answer_two()

answer_three()

