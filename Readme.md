# Unearth BHP
Problem - Optimize Train Delays
Solution Domain - Wide (100+)

# Approach
## Day 1
Minimum Working Model - We will create a simple model using our environment to find delays associated with each train, with initial sample for a few trains.
.pre-processing/> train.sh [train_id]
output [/data/post_process]: [train_id].csv DATETIME,WEIGHT,LATITUDE,LONGITUDE,PROFILE,SPEEDLIMIT,FIRESPEED,GPSSTATUS

## Day 2
- Create a Spark Cluster to process train-run data
- Decorate the Model
- Run solutions and score them

## Day 3
- Interactive capability to explore solutions (??)

# Team
Mark, Logan & Vaibhav
