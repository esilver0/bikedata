#!/usr/bin/env python3

import pandas as pd
import operator
from station import Station

#-----------------------------------------------------------------------------#


def __main__():
	'''
	     Gets data file name and readies it for input.
	     Calls function checkstationdata for each row, updating bike 
	     station list.
	     Sorts the list to plot and calls function to create graph 
	     and save to image.
	'''

	datafilename = input('Enter the csv file you would like to analzye: ')
	# So I don't have to type the name of the file
	if datafilename == "///":
		datafilename = 'citibike.csv'
		#datafilename = 'smalldata.csv'  # expected test file name
	print(datafilename)
	df=pd.read_csv(datafilename, sep=',')

	bikestations = [] # This will be a list of Station instances

	print("Input Progress:   ", end="")
	input_percent = 0
	rows = df.shape[0] # rows in file	
	for index, row in df.iterrows():
		checkstationdata(df, row, bikestations, 'start station id',
	        	                                'start station name')
		checkstationdata(df, row, bikestations, 'end station id',
	        	                                'end station name')

		# If a multiple of a hundredth of the rows has past
		if rows > 1000 and (index % (rows // 100) == 0):
			input_percent += 1
			if input_percent < 11:
				print('\b' * 2, end= "")
			elif input_percent < 101:
				print('\b' * 3, end= "")
			if input_percent < 101:
				print(input_percent,"\b%", end= "", flush = True)
	if rows <= 1000:
		print("100%") 
	print("")

	# Sorts bikestations by the increase in bikes
	bikestations.sort(key=lambda x: x.get_increase_in_units(), reverse= True)

	for i in range(len(bikestations) ):
		print("Station:", bikestations[i].get_id(),
		      "\tArrival count:", bikestations[i].get_arrival_count(),
		      "\tDeparture count:", bikestations[i].get_departure_count(),
		      "\tArrivals minus departures:",
		      bikestations[i].get_increase_in_units() ) 
	print('\n'* 3)

	'''
	# Sorts the instances in the list by their station ids
	bikestationsby_id = sorted(bikestations, key=operator.attrgetter('id'))
	for i in range(len(bikestations) ):
		print("Station:", bikestations[i].get_id(),
		  "\tArrival count:", bikestations[i].get_arrival_count(),
		  "\tDeparture count:", bikestations[i].get_departure_count() )	
	'''

	# Saves graph as png
	graph = 'stationgraph.png'
	plot(bikestations, graph) 
	print("A graph has been saved as:", graph)


#-----------------------------------------------------------------------------#


def searchforstation(stations, station_id):
	'''  Searches for station by checking for matching id 
	     and returns position in list '''

	#print("Looking for station id:", station_id) # For debugging

	for i in range(len(stations) ):
		if stations[i].get_id() == station_id:
			#print("Position in searchforstat:", i) # For debugging
			return i 	# Returns the position if found

	return len(stations)	# Returns an index out of range


#-----------------------------------------------------------------------------#


def increase_appropriate_count(station, id_type, amount = 1):
	''' 
	Checks for whether the station is a start station or 
	end station then increases the respective count
	'''

	if id_type == 'start station id':
		station.increase_arrival_count(amount)

	elif id_type == 'end station id':
		station.increase_departure_count(amount)
	'''
	# For debugging
	print("Station:", station.get_id(),
	      "\tArrival count:", station.get_arrival_count(),
	      "\tDeparture count:", station.get_departure_count() )	
	'''

#-----------------------------------------------------------------------------#


def checkstationdata(df, row, stations, station_id, station_name):
	'''  Checks and updates 'stations' with the id, name, and
	     usage of the station.
	'''

	# The positon in stations list
	station_position = searchforstation(stations, row[station_id])
	#print("Position in checkstatdata:", station_position) # For debugging	


	# If the position is within stations' range
	# increase the corresponding count for the station
	if abs(station_position) < len(stations):
		tempstation = stations[station_position]
		increase_appropriate_count(tempstation, station_id)

	else: # Initialize a new station and add it to stations list
		tempstation = Station()
		tempstation.set_id(row[station_id])
		tempstation.set_name(row[station_name])
		increase_appropriate_count(tempstation, station_id)
		stations.append(tempstation)


#-----------------------------------------------------------------------------#


def plot(bikestations, outputfile = 'bikestations.png'):
	'''
	     Creates a bar graph of the increase in bikes in a station
	     in decending order. The greater the magnitude of the bar
	     the more imbalanced the station is.

	     The graph is saved as an image. 
	'''

	import matplotlib as mpl
	mpl.use('Agg')  # So that matplotlib will output to an image
	import numpy as np
	import matplotlib.pyplot as plt

	# Plot data
	n_stations = len(bikestations)
	station_ids = []
	increaseinbikes = []
	for i in range(len(bikestations) ):
		station_ids.append(bikestations[i].get_id() )
		increaseinbikes.append(bikestations[i].get_increase_in_units())

	# Create Plot

	# Creates figure and size of plot
	fig, ax = plt.subplots(1, 1, figsize=(n_stations / 4.0, 10) )
	#fig, ax = plt.subplots()



	index = np.arange(n_stations) # The x locations
	bar_width = 0.5
	opacity = 0.6

	bar = plt.bar(index + 2.5 * bar_width, increaseinbikes, bar_width,
	              alpha = opacity,
	              color = 'b',
	              label = 'Increase in bikes'
	              ) 
	

	plt.xlabel('Bike Stations')                 # Horizontal axis label
	#plt.ylabel()
	plt.title('Increase in Bikes Per Station')  # Title

	# Horizontal label locations
	plt.xticks(index + 3.0 * bar_width, station_ids)
	plt.xticks(rotation= 60)                    # Rotates counterclockwise
	plt.legend()

	plt.tight_layout()

	fig.savefig(outputfile) 

#-----------------------------------------------------------------------------#



# Calls __main__
if __name__ == "__main__":
	__main__()

