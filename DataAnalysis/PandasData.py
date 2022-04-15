import pandas as pd
import datetime

def GenerateData(month):
    monthString = str(month)
    lengthMonthString = len(monthString)
    if(lengthMonthString == 1):
        monthString = '0' + monthString
    inputFile = INPUT_PREFIX + monthString + OUTPUT_EXTENSION
    outputFile = OUTPUT_PREFIX + monthString + OUTPUT_EXTENSION
    print("Input : ", inputFile, "  Output : ", outputFile)
    data = pd.read_csv(inputFile, sep=",", encoding="euc-kr")
    data_clean = data.drop(["Unnamed: 6"], axis='columns')
    data_clean = data_clean[data_clean["통행시간"] > 0]
    dataFrame_data = pd.DataFrame(data_clean, columns=["집계일자", "집계시", "출발영업소코드", "도착영업소코드", "통행시간"])
    staart_from_101 = dataFrame_data[dataFrame_data["출발영업소코드"] == 101]
    staart_from_101_to_140 =staart_from_101[staart_from_101["도착영업소코드"].isin([105,110,115,120,125,130,135,140])]
    staart_from_101_to_140 = staart_from_101_to_140.assign(요일=pd.to_datetime(staart_from_101_to_140["집계일자"], format="%Y%m%d").dt.dayofweek)    
    staart_from_101_to_140.sort_values(by=["집계일자", "집계시"])
    staart_from_101_to_140.to_csv(outputFile, index=None, header=True, encoding="euc-kr")
    output_dataframes.append(staart_from_101_to_140)

INPUT_PREFIX = './CSV/TCS_영업소간통행시간_1시간_1개월_2021'
OUTPUT_PREFIX = './CSV/data_2021'
OUTPUT_EXTENSION = '.csv'

output_dataframes = []
for month in range(1,13):
    GenerateData(month)
    
output_data = pd.concat(output_dataframes, ignore_index=True, sort=False)
final = OUTPUT_PREFIX + OUTPUT_EXTENSION
output_data.to_csv(final, index=None, header=True)



    

