import csv
import statistics as s
import matplotlib.pyplot as plt

results = [row for row in csv.reader(open('results.csv'    , 'r'))]
truth   = [row for row in csv.reader(open('groundTruth.csv', 'r'))]
if len(truth) != len(results):
	print "length of truth " ,len(truth), " != length of results ", len(results) 
else:
	n = len(results)
	plt.plot(range(n), [float(  truth[i][0]) for i in range(n)])
	plt.plot(range(n), [float(results[i][0]) for i in range(n)])
	plt.xlabel('Time')
	plt.show()
