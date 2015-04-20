"""
Simple command-line sample for the Google Prediction API
judiciously borrowed from https://github.com/google/google-api-python-client/blob/master/samples/prediction/prediction.py


Command-line application that trains on your input data. This sample does
the same thing as the Hello Prediction! example. You might want to run
the setup.sh script to load the sample data to Google Storage.

Usage:
	$ python prediction.py "bucket/object" "model_id" "project_id"

You can also get help on all the command-line flags the program understands
by running:

	$ python prediction.py --help

To get detailed log output run:

	$ python prediction.py --logging_level=DEBUG
"""
from __future__ import print_function

import argparse
import os
import pprint
import sys
import time
import csv
import matplotlib.pyplot as plt

from apiclient import discovery
from apiclient import sample_tools
from oauth2client import client

# Time to wait (in seconds) between successive checks of training status.
SLEEP_TIME = 30


# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('object_name',
		help='Full Google Storage path of csv data (ex bucket/object)')
argparser.add_argument('model_id',
		help='Model Id of your choosing to name trained model')
argparser.add_argument('project_id',
		help='Model Id of your choosing to name trained model')


def print_header(line):
	'''Format and print header block sized to length of line'''
	header_str = '='
	header_line = header_str * len(line)
	print('\n' + header_line)
	print(line)
	print(header_line)
	

def main(argv):
	# If you previously ran this app with an earlier version of the API
	# or if you change the list of scopes below, revoke your app's permission
	# here: https://accounts.google.com/IssuedAuthSubTokens
	# Then re-run the app to re-authorize it.
	service, flags = sample_tools.init(
			argv, 'prediction', 'v1.6', __doc__, __file__, parents=[argparser],
			scope=(
					'https://www.googleapis.com/auth/prediction',
					'https://www.googleapis.com/auth/devstorage.read_only'))

	try:
		# Get access to the Prediction API.
		papi = service.trainedmodels()
	
		# List models.
		print_header('Fetching list of first ten models')
		result = papi.list(maxResults=10, project=flags.project_id).execute()
		print('List results:')
		pprint.pprint(result)

		# Start training request on a data set.
		print_header('Submitting model training request')
		body = {'id': flags.model_id, 'storageDataLocation': flags.object_name}
		print(body)
		start = papi.insert(body=body, project=flags.project_id).execute()
		print('Training results:')
		pprint.pprint(start)

		# Wait for the training to complete.
		print_header('Waiting for training to complete')
		while True:
			status = papi.get(id=flags.model_id, project=flags.project_id).execute()
			state = status['trainingStatus']
			print('Training state: ' + state)
			if state == 'DONE':
				break
			elif state == 'RUNNING':
				time.sleep(SLEEP_TIME)
				continue
			else:
				raise Exception('Training Error: ' + state)

			# Job has completed.
			print('Training completed:')
			pprint.pprint(status)
			break

		# Describe model.
		print_header('Fetching model description')
		result = papi.analyze(id=flags.model_id, project=flags.project_id).execute()
		print('Analyze results:')
		pprint.pprint(result)

		# Make some predictions using the newly trained model.
		print_header('Making some predictions')
		csvwriter = csv.writer(open('results.csv', 'wb'))
		#rateLimit = 1;
		for row in csv.reader(open('labeledTestSet.csv','r')):
			body = {'input': {'csvInstance': row}}
			result = papi.predict(
				body=body, id=flags.model_id, project=flags.project_id).execute()
			print('Prediction results for "%s"...' % row)
			pprint.pprint(result)
			csvwriter.writerow([result['outputValue']])
			#if rateLimit >1 :
			#	rateLimit -= 1
			#else:
			#	break

		# Delete model.
		print_header('Deleting model')
		result = papi.delete(id=flags.model_id, project=flags.project_id).execute()
		print('Model deleted.\n')
		
		

	except client.AccessTokenRefreshError:
		print ('The credentials have been revoked or expired, please re-run '
			'the application to re-authorize.')


if __name__ == '__main__':
	main(sys.argv)

