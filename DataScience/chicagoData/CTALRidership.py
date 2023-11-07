import pandas

#below data is large Chicago 'L' ridership dataset.
# the top row is | station_id | stationname | date | daytype | rides

chicagoData = pandas.read_csv("/Users/aaron/Code/DataScience/Data/CTA_-_Ridership_-__L__Station_Entries_-_Daily_Totals.csv")


print (chicagoData.dtypes)

print (chicagoData.stationname.value_counts())

print (chicagoData.date.value_counts())

sortedByDate = chicagoData.sort_values('date')

print (sortedByDate)

#print (chicagoData.head())
print (chicagoData.describe)


# print (chicagoData.shape)
# print (type(chicagoData))