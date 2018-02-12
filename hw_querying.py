# Homework Querying Template Code
#
# This initial helper code will contact the server to request a random address in the United States. 
#
# Your goal is to determine most recent bill sponsored by the state senator who represents this address.
# To achieve this goal, you should:
#  - First parse the state's two-letter abbreviation from the address string using regular expressions;
#  - Then use the Census.gov Geocoding API onelineaddress geographies search to find the Upper State Legislative District.
#  - Next use the OpenStates.org API legislator method to determine the full name of the senator in this district.
#  - Finally use the OpenStates.org API bills method to find the title of the last bill sponsored by this senator. (If none, then return 'nothing'.)
#
# Pass your answers to the variables named stateAbbrev, districtNumber, senatorFullName, and sponsoredBillTitle resposectively.
# 
# When you have a final answer, you can submit your assignment to the autograde by running the submit.py script 

##################################################################
### HELPER CODE TO REQUEST RANDOM ADDRESS FROM SERVER
##################################################################
import requests
address=requests.get("https://goo.gl/dyW5Wy").text
print(address)

##################################################################
### YOUR CODE SHOULD GO BELOW HERE
##################################################################
import re
# import anything else you might need here 

email= "YOUR_EMAIL_GOES_HERE@brown.edu" #REPLACE THIS







stateAbbrev='???' # UPDATE THIS LINE TO INCLUDE YOU ANSWER
districtNumber='???' # UPDATE THIS LINE TO INCLUDE YOU ANSWER
senatorFullName='???' # UPDATE THIS LINE TO INCLUDE YOU ANSWER
sponsoredBillTitle='???' # UPDATE THIS LINE TO INCLUDE YOU ANSWER

print(stateAbbrev)
print(districtNumber)
print(senatorFullName)
print(sponsoredBillTitle)

##################################################################
### DO NOT CHANGE THE FOLLOWING - Used in submission process
##################################################################
def yourSubmission():
	return {'email':email,'hw':'querying','input':address,'state':stateAbbrev,'district':districtNumber,'senator':senatorFullName,'bill':sponsoredBillTitle}