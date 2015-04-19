import csv
import datetime as dt

percentageTrainingDataToBeUsedAsTest = 0.1
trainKaggle = [row for row in csv.reader(open('trainRaw.csv', 'r'))]
trainDataRobot = trainKaggle[:-int(len(trainKaggle)* percentageTrainingDataToBeUsedAsTest)]
with open('trainKaggle.csv', 'wb') as f:
	csvwriter = csv.writer(f)
	# exclude the 2 columns not in test, convert datetime to date and seconds for easier learning
	# cyclic pattern is explicit in that representation
	for t in trainKaggle:
		timeSince2011 = (dt.datetime.strptime(t[0], "%Y-%m-%d %X") - dt.datetime(2011,1,1))
		csvwriter.writerow([t[-1]] + [ timeSince2011.days , timeSince2011.seconds/3600 ] + t[1:-3])
with open('trainDataRobot.csv', 'wb') as f:
	csvwriter = csv.writer(f)
	# exclude the 2 columns not in test, convert datetime to date and seconds for easier learning
	# cyclic pattern is explicit in that representation
	# split training data so we can analyze residuals
	for t in trainDataRobot:
		timeSince2011 = (dt.datetime.strptime(t[0], "%Y-%m-%d %X") - dt.datetime(2011,1,1))
		csvwriter.writerow([t[-1]] + [ timeSince2011.days , timeSince2011.seconds/3600 ] + t[1:-3])


testKaggle = [row for row in csv.reader(open('testRaw.csv', 'r'))]
testDataRobot = trainKaggle[-int(len(trainKaggle) * percentageTrainingDataToBeUsedAsTest):]
with open('testKaggle.csv', 'wb') as f:
	csvwriter = csv.writer(f)
	# exclude the 2 columns not in test, convert datetime to date and seconds for easier learning
	# cyclic pattern is explicit in that representation
	for t in testKaggle:
		timeSince2011 = (dt.datetime.strptime(t[0], "%Y-%m-%d %X") - dt.datetime(2011,1,1))
		csvwriter.writerow([t[-1]] + [ timeSince2011.days , timeSince2011.seconds/3600 ]  + t[1:-1])
with open('testDataRobot.csv', 'wb') as f:
	csvwriter = csv.writer(f)
	# exclude the 2 columns not in test, convert datetime to date and seconds for easier learning
	# cyclic pattern is explicit in that representation
	# split training data so we can analyze residuals
	for t in testDataRobot:
		timeSince2011 = (dt.datetime.strptime(t[0], "%Y-%m-%d %X") - dt.datetime(2011,1,1))
		csvwriter.writerow([ timeSince2011.days , timeSince2011.seconds/3600 ] + t[1:-3])
		
