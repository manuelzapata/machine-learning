#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#Get dataset size
print "Enron dataset size: {0}".format(len(enron_data))

#Get number of features per person
people = enron_data.keys()
features = enron_data[people[0]]
print "Features per person: {0}".format(len(features))

#Get the POI (person of interest) count from dataset
poiCount = 0
for key, value in enron_data.iteritems():
    if(enron_data[key]["poi"] == 1):
        poiCount += 1

print "POI count from dataset: {0}".format(poiCount)

#Get POI count from text file
poiCount = 0
with open("../final_project/poi_names.txt") as file:
    for line in file:
        if(line.startswith("(y)") or line.startswith("(n)")):
            poiCount += 1

print "POI count from text file: {0}".format(poiCount)

#James Prentice total stock value
totalStockValue = enron_data["PRENTICE JAMES"]["total_stock_value"]
print "James Prentice total stock value: {0}".format(totalStockValue)

#Wesley Colwell to POI email count
emailCount = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Wesley Colwell emails sent to POIs: {0}".format(emailCount)

#Jeffrey K Skilling value of exercised stock options
exercisedStockValue = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print "Jeffrey K Skilling value of exercised stock options: {0}".format(exercisedStockValue)

#Who took most of the money?
totalPaymentsSKilling = enron_data["SKILLING JEFFREY K"]["total_payments"]
totalPaymentsLay = enron_data["LAY KENNETH L"]["total_payments"]
totalPaymentsFastow = enron_data["FASTOW ANDREW S"]["total_payments"]

maxValue = max(totalPaymentsFastow, totalPaymentsLay, totalPaymentsSKilling)
maxValueOwner = ""
if(maxValue == totalPaymentsFastow):
    maxValueOwner = "FASTOW ANDREW S"
elif maxValue == totalPaymentsLay:
    maxValueOwner = "LAY KENNETH L"
else:
    maxValueOwner = "FASTOW ANDREW S"


print "{0} took the most: $ {1}".format(maxValueOwner, maxValue)

#How many people with a quantified salary and how many people with email address
peopleWithSalary = 0
peopleWithEmailAddress = 0
for key, value in enron_data.iteritems():
    if(enron_data[key]["salary"] != "NaN"):
        peopleWithSalary += 1
    if(enron_data[key]["email_address"] != "NaN"):
        peopleWithEmailAddress += 1

print "People with a quantified salary: {0}".format(peopleWithSalary)
print "People with a known email address: {0}".format(peopleWithEmailAddress)

#percentage of people without total payments info
peopleWithoutTotalPayments = 0.0
for key, value in enron_data.iteritems():
    if(enron_data[key]["total_payments"] == "NaN"):
        peopleWithoutTotalPayments += 1
percentage = peopleWithoutTotalPayments / len(enron_data) * 100
print "Percentage of people without total payments info: {0}%".format(percentage)

#percentage of POIs without total payments info
peopleWithoutTotalPayments = 0.0
for key, value in enron_data.iteritems():
    person = enron_data[key]
    if(person["total_payments"] == "NaN" and person["poi"] == 1):
        peopleWithoutTotalPayments += 1
percentage = peopleWithoutTotalPayments / len(enron_data) * 100
print "Percentage of POIs without total payments info: {0}%".format(percentage)
