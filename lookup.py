import pandas as pd
import numpy as np


class Lookup(object):
    """
    """
    def __init__(self, column, values):
        """
        """
        self.column = column
        self.values = values

        self.downtime = pd.read_csv('downtime_events.csv')
        self.busLocoMap = pd.read_csv('busLocoMap.csv')
        self.trainBusinessMap = pd.read_csv('trainBusinessLookup.csv')

    def get_loco_downtime_id(self, loaded=True):
        """
        """
        self.trainIDs = self.downtime.TRAIN_ID[self.downtime[self.column] == self.values]
        self.businessIDs = self.trainBusinessMap.BUSINESS_TRAIN_ID[np.in1d(self.trainBusinessMap.TRAIN_ID, self.trainIDs)]
        self.loco_tuples = self.busLocoMap.loco[np.in1d(self.busLocoMap.bus, self.businessIDs)].apply(lambda x: eval(x))
        self.loco_ids = [j for i in self.loco_tuples for j in i]
