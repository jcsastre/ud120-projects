#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL', 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

# for key, value in data_dict.iteritems():
#     bonus = value['bonus']
#     salary = value['salary']
#     if bonus != 'NaN' and bonus >= 5000000 and salary != 'NaN' and salary >= 1000000:
#         print key
# exit()


# maxBonus = 0
# name = ""
# for key, value in data_dict.iteritems():
#     bonus = value['bonus']
#     salary = value['salary']
#     if bonus != 'NaN' and bonus > maxBonus and salary < 400000 and bonus < 8000000:
#         maxBonus = bonus
#         name = key
# print name
# print maxBonus
# exit()

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()