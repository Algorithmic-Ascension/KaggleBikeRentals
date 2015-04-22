import csv
import datetime as dt

testSize = 168
data = [row for row in csv.reader(open('trainRaw.csv', 'r'))]

train = data[:-testSize]
csvwriter = csv.writer(open('train.csv', 'wb'))
# exclude the 2 columns not in test, convert datetime to date and seconds for easier learning
# putting into dayhours since 2011 highlights that days are continuous
for t in train:
	timeSince2011 = (dt.datetime.strptime(t[0], "%Y-%m-%d %X") - dt.datetime(2011,1,1))
	csvwriter.writerow([t[-1], timeSince2011.days + float(timeSince2011.seconds)/3600/24 ] + t[1:-3])

truth = train[:testSize]#[x for x in data if x not in train]
# save ground truth into similar file for easy comparison
unlabeledWriter = csv.writer(open('test.csv', 'wb'))
truthWriter = csv.writer(open('groundTruth.csv', 'wb'))
for t in truth:
	timeSince2011 = (dt.datetime.strptime(t[0], "%Y-%m-%d %X") - dt.datetime(2011,1,1))
	unlabeledWriter.writerow([ timeSince2011.days + float(timeSince2011.seconds)/3600/24 ] + t[1:-3])
	truthWriter.writerow( [t[-1]] )
		
