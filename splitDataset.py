import csv
import datetime as dt
#import random as r

#r.seed(1337)
percentageOfDataToBeUsedAsTest = 0.1
data = [row for row in csv.reader(open('trainRaw.csv', 'r'))]
# the application is forecasting, so sampling independently makes less sense here
# r.sample( data, len(data) * percentageOfDataToBeUsedAsTest )
train = data[:-int(len(data)* percentageOfDataToBeUsedAsTest)] 
with open('dataset.csv', 'wb') as f:
	csvwriter = csv.writer(f)
	# exclude the 2 columns not in test, convert datetime to date and seconds for easier learning
	# cyclic pattern is explicit in that representation
	for t in data:
		timeSince2011 = (dt.datetime.strptime(t[0], "%Y-%m-%d %X") - dt.datetime(2011,1,1))
		csvwriter.writerow([t[-1]] + [ timeSince2011.days , timeSince2011.seconds/3600 ] + t[1:-3])
with open('train.csv', 'wb') as f:
	csvwriter = csv.writer(f)
	# split training data so we can analyze residuals
	for t in train:
		timeSince2011 = (dt.datetime.strptime(t[0], "%Y-%m-%d %X") - dt.datetime(2011,1,1))
		csvwriter.writerow([t[-1]] + [ timeSince2011.days , timeSince2011.seconds/3600 ] + t[1:-3])

labeledTestSet = [x  for x in data if x not in train]
with open('test.csv', 'wb') as f:
	# save ground truth into similar file for easy comparison
	with open('groundTruth.csv', 'wb') as g:
		labeledWriter = csv.writer(f)
		truthWriter = csv.writer(g)
		for t in labeledTestSet:
			timeSince2011 = (dt.datetime.strptime(t[0], "%Y-%m-%d %X") - dt.datetime(2011,1,1))
			labeledWriter.writerow([ timeSince2011.days , timeSince2011.seconds/3600 ] + t[1:-3])
			truthWriter.writerow( [t[-1]] )
		
