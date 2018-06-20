
#-----------------------------------------------------------------------------#


class Station:
	'''  
	Station class contains the attributes of a station
	such as a name, id, departure count, and arrival count
 

	'''

	# The inital state of a station has neither arrivals nor departures
	def __init__(self):
		self.departure_count = 0
		self.arrival_count = 0

	# Increases the arrival count by additional
	def increase_arrival_count(self, additional = 1):     # To decrease use
		self.arrival_count += additional	      # negative

	# Increases the departure count by addtional
	def increase_departure_count(self, additional = 1):   # To decrease use
		self.departure_count += additional	      # negative

	# Set station name
	def set_name(self, station_name):
		self.name = station_name

	# Returns station name
	def get_name(self):
		return self.name

	# Set station id
	def set_id(self, station_id):
		self.id = station_id

	# Returns station id
	def get_id(self):
		return self.id

	# Returns arrival count
	def get_arrival_count(self):
		return self.arrival_count

	# Returns departure count
	def get_departure_count(self):
		return self.departure_count

	# Returns the increase in units (May be negative)
	def get_increase_in_units(self):
		return self.arrival_count - self.departure_count	
#-----------------------------------------------------------------------------#


