import csv
import datetime as dt

testSize = 24 * 7 # hours in a week
data = [ row for row in csv.reader(open('trainRaw.csv', 'r')) ]

train = data[:-testSize]
csvwriter = csv.writer( open('train.csv', 'wb') )
# exclude the 2 columns not in test, convert datetime to date and seconds for easier learning
# putting into dayhours since 2011 highlights that days are continuous
for i in range(len(train)):
	csvwriter.writerow( [train[i][-1]] + preprocess(train, i) )

truth = train[testSize*70:testSize*71] # fitted model for testing purposes # for realzies [x for x in data if x not in train]
# save ground truth into similar file for easy comparison
unlabeledWriter = csv.writer( open('test.csv', 'wb') )
truthWriter = csv.writer( open('groundTruth.csv', 'wb') )
for i in range(len(truth)):
	unlabeledWriter.writerow( preprocess(truth, i) )
	truthWriter.writerow( [truth[i][-1]] )

# enforces column ordering 
def preprocess(data, rowNumber):
	row = data[rowNumber]
	hourlyComponent, weeklyComponent = encodeTimeAsDifferenceFromPreviousTime(data, rowNumber)
	return [hourlyComponent, weeklyComponent] + decodeCategories(row) + row[5:-3]

# Autoregressive model
def encodeTimeAsDifferenceFromPreviousTime(data, i):	
	hourlyComponent = float(data[i-1   ][-1]) - float(data[i][-1])
	weeklyComponent = float(data[i-24*7][-1]) - float(data[i][-1])
	return hourlyComponent, weeklyComponent
	
def decodeCategories(row):
	seasons = ['', 'spring', 'summer', 'fall', 'winter']
	holiday = ['noliday', 'holiday']
	workingDay = ['leisure', 'work'] 
	return [ int(seasons[row[1]]) , int(holiday[row[2]]) , int(workingDay[row[3]]) ]
	
def timeSince2011(row):
	return (dt.datetime.strptime(t[0], "%Y-%m-%d %X") - dt.datetime(2011,1,1))

