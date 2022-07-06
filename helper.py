import re

# get rid of specific character in user name
def getRidOfSpaceAndSpecialChar(userName):
    return re.sub('\W+','',userName)
