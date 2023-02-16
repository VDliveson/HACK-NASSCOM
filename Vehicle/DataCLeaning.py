import pandas as pd

data = pd.read_csv(r"Z:\NASSCOM\Vehicle\VehicleSales.csv",encoding = 'cp1252')
data.drop(['Model_Desc','Colour','InsuranceCompany','TempRegnNo','Manufacturer_Name','OfficeCd','rowid'],axis = 1,inplace = True)
print(data.dtypes)