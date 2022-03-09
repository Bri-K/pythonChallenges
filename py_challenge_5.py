import urllib.request
import pickle

# 'peak hill' sounds like 'pickle';
# another clue: google 'banner.p', .p is an extension for a pickle file

url_request = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

# url_request.read() is a binary string that needs to be unpickled

data = pickle.loads(url_request.read())

# data is a list of lists. Each list is a tuple of characters and counts,
# the counts adding up to 95 for each list

for list in data:
    line_string = ''
    for tuple in list:
        line_string += tuple[0]*tuple[1]
    print(line_string)
