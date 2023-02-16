import pandas as pd
import matplotlib.pyplot as mp
import pandas as pd
import seaborn as sb
import os
# assign directory

# def merge_files(data):
    
#     # data = data.drop(data.columns[[0]],axis =1)
#     # print(data)
    
    
#     data.columns = data.iloc[0]
#     # data =data.drop(data.index[0],axis = 0)
#     # print(data.head())
#     return data
    
   
    
   
# merge_files(pd.read_csv(r'Z:\NASSCOM\AQI\MonthlyAQI2022.csv'))

directory = r'Z:\NASSCOM\weather'





 
# # iterate over files in
# # that directory
final_df = pd.DataFrame()
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    
    # checking if it is a file
    
    if os.path.isfile(f) and f.endswith('.csv'):
        print(f)
        print("")
        data = pd.read_csv(f)
        # print(data['district'].value_counts())
        # break
        col_names = ['district', 'mandal', 'date', 'rain', 'temp_min', 'temp_max',
       'humidity_min', 'humidity_max', 'wind_speed_max', 'wind_speed_min']
        if(len(col_names)!=len(data.columns)):
            print("err.................")
            
            break
            
        data.columns = col_names
        data = data.drop(['mandal'],axis = 1)
        data = data.groupby(['district','date'],as_index=False).mean()
        # print(data['district'])
        data = data[data['district'].isin(['Adilabad','Nizamabad','Karimnagar','Warangal','Khamman'])]
        # print(data['district'])
        

        # data = merge_files(data)
        # print(data.head())
        
        if(final_df.shape == (0,0)):
            final_df = data
        else:
            # final_df = final_df.merge(data, how='outer',on = "district")
            final_df = final_df.append(data, ignore_index = True)
        # print(final_df.head())
        # print("..................................")
        # print("................................................................")
       
dataplot = sb.heatmap(final_df.corr(), cmap="YlGnBu", annot=True)
  
# displaying heatmap
mp.show()
# print(final_df.corr())
final_df.to_csv('finalWeather.csv',index=False)
        











# print(data[data[data.columns[0]] == 1])

