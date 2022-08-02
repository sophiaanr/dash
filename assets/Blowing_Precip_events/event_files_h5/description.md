Event files created using aggregated_snow_events_400_3.csv. The aggregation of 
snow events was done using DBScan, with an epsilon value of 400 and 3 min_samples. 
These resulting clusters were then aggregated using aggregate.py, which loops 
through events and groups based on events' duration and gap. The parameters were 
a gap of 1.5 hours between events and a minimum event duration of 30 minutes. 
The events contain flag data from mrr, cl61, and pip, pip precip rain and nonrain
rates, and pip psd N0 fitted and lambda fitted reprocessed data. All data is 
processed on a time interval of 10 seconds, starting from the first available time
and ending with the last available time (both from cl61 instrument). 