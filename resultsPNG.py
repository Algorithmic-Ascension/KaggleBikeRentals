import csv
import statistics as s
import matplotlib.pyplot as plt

results = [row for row in csv.reader(open('results.csv'    , 'r'))]
truth   = [row for row in csv.reader(open('groundTruth.csv', 'r'))]
if len(truth) != len(results):
	print "length of truth %s != length of results %s", len(truth), len(results) 
else:
	plt.plot(range(truth), [float(  truth[i][0]) for i in range(truth)])
	plt.plot(range(truth), [float(results[i][0]) for i in range(truth)])
	plt.xlabel('Time')
	plt.show()
