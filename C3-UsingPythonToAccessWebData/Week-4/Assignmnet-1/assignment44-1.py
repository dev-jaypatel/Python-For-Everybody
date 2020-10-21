#Welcome Jay Nareshbhai Patel from Using Python to Access Web Data
#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write
# a Python program similar to http://www.py4e.com/code3/urllink2.py. The program
# will use urllib to read the HTML from the data files below, and parse the data,
# extracting numbers and compute the sum of the numbers in the file.
#We provide two files for this assignment. One is a sample file where we give
# you the sum for your testing and the other is the actual data you need to
# process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_913540.html (Sum ends with 4)
#You do not need to save these files to your folder since your program will read
# the data directly from the URL. Note: Each student will have a distinct data
# url for the assignment - so only use your own data url for analysis.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

total_sum = 0
# Retrieve all of the anchor tags
tags = soup('tr')
for tag in tags:
   # Look at the Contents of a tag
   y = tag.contents[1]
   #Find the number after decoding the tag
   raw = re.findall('[0-9]+', y.decode())
   #goes throught the list of raw
   for numb in raw:
       #converts raw to integer numbers
       inumb = int(numb)
       #Sum
       total_sum = total_sum + inumb

print(total_sum)
