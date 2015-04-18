import csv

train = [row for row in csv.reader(open('trainRaw.csv', 'r'))]
[ [train[i][-1]] + train[i][:-3] for i in range(len(train)) ]

with open('train.csv', 'wb') as f:
	csvwriter = csv.writer(f)
	for i in range(len(train)):
		csvwriter.writerow([train[i][-1]] + train[i][:-3])
