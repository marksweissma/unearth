# Unearth BHP
Problem - Optimize Train Delays
Solution Domain - Wide (100+)

# Approach
## Day 1
Minimum Working Model - We will create a simple model using our environment to find delays associated with each train, with initial sample for a few trains.
.pre-processing/> train.sh [train_id]
output [/data/post_process]: [train_id].csv DATETIME,WEIGHT,LATITUDE,LONGITUDE,PROFILE,SPEEDLIMIT,FIRESPEED,GPSSTATUS

## Day 2
Compute
- Create a Spark Cluster to process train-run data [DONE using Amazon EMR 5.0.0]
- Next step is to open the port and use Zepellin [DONE]
- Upload all the data to s3://unearthbhp [DONE]
- Map S3 to HDFS Cluster [DONE]
- Install Jupyter and Python goodness on the cluster, moving to PySpark [DONE]

Model
- Decorate the Model
- Run solutions and score them [Axed]
Approach we are creating an early warning system with the model. Wireframe for the same is at: https://wireframe.cc/u8qbSr

Application
- React Application

## Day 3
- Interactive capability to do early detection.
-

Presentation
- Powerpoint - (Problem, Demo, Takeaway - S3)
- Background - BHP IROC & Ninglou

# Team
Mark, Logan & Vaibhav
