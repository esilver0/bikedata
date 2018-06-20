# bikedata

#### Instructions:
Obtain a citi bike data csv file \
Run _bikestation.py_ to analyze the data \
You will need _station.py_ as well.




#### The question:
Which stations are the least balanced (more bikes leaving than entering, or vice versa)? 

#### The answer:
Taking data from a csv file, a list of Station class instances _located in station.py_ is made.
The Station class has attributes such as the name, id, and number of bikes that started and ended there.
The list is then sorted by the number of bikes arriving there minus the number of bikes leaving there in decending order.
Next a bar chart is mades such that the increase in bikes is on the vertical axis and the station ids are on the horizontal axis. 


On the chart, the bike stations that had the most arrivals minus departures are furthest left.
The bike stations that had the most bike departures minus arrivals are furthest right. The larger the magnitude of the bar the more inbalanced the station is.




A result using a small data set:


<img src="https://raw.githubusercontent.com/esilver0/bikedata/master/smalldataset.png" width="600">


\
\
\
A result using a larger data set from January 2016. You may want to open the image in a new tab or scroll down to see the image rotated.


![data](https://raw.githubusercontent.com/esilver0/bikedata/master/stationgraph.png)


\
\
\
\
\
Rotated Image:

<img src="https://raw.githubusercontent.com/esilver0/bikedata/master/stationgraph_rotated.png" width="600">

