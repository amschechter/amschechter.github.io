import pandas as pd
import datetime
import matplotlib.pyplot as plt


transit_ridership_file = pd.read_csv(r'C:\Users\aaron\Downloads\Daily_Transit_Ridership.csv')


transit_ridership_file.columns = [c.replace(' ', '_') for c in transit_ridership_file.columns] #replaces column names with underscores


#print(transit_ridership_file)


#only_mass = transit_ridership_file['Agency'].str.contains('WMATA').any()

#print(len(transit_ridership_file))

mass_rows = [];


for index, row in transit_ridership_file.iterrows():
    #only_mass = row['Agency'].str.contains('WMATA').any()
    only_mass = row

    #print(only_mass.Agency.find('WMATA'))
    if(only_mass.Agency.find('WMATA') == 0):
        #print("yes mata")
        #print(row)
        mass_rows.append(row)
    


for row in mass_rows:
    
    #   current_date = datetime(row.Date)
    #print('current_date - ', current_date)
    
    month = row.Date[0:2]
    day = row.Date[3:5]
    year = row.Date[6:10]

    current_date = datetime.datetime(int(year),int(month),int(day))

    row.Date = current_date

    Current_Ridership_Int = int(row.Current_Ridership)

    row.Current_Ridership = Current_Ridership_Int

    #print(month,day,year)
    ##date_as_datetime = date
    #print (row.Current_Ridership, current_date)
    #print(row)

data_frame = pd.DataFrame(mass_rows)

    
    #if(row['Agency'].str.contains('WMATA').any()):
     #   print('masshole')




print(type(data_frame.iloc[1].Current_Ridership))
print((data_frame.iloc[1].Current_Ridership))


### inplace = true modifies the existing DF, otherwise you need to make a new one.
data_frame.sort_values('Current_Ridership', inplace = True)

print(data_frame.head(2))
print(data_frame.info())

print (data_frame)

#   data_frame.plot()

data_frame["Current_Ridership"].plot(kind = 'hist')

#file path "C:\Users\aaron\Downloads\Daily_Transit_Ridership.csv"