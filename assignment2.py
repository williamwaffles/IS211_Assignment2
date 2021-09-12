import argparse
import urllib.request
import logging
import datetime

user_url = urllib.request.Request('http://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')


def downloadData(url = 'http://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')
        return data

print(downloadData(user_url))

def processData(file_content):
    #format = "%d %m %y"
    for i in file_content:
        #list_data = datetime.datetime.strptime(index, format)
        print(i)
'''
    with file_content as f:
        reader = list(f)
        print(map(lambda x: dict(zip(reader[0], x)), reader))
 '''

print(processData(downloadData(user_url)))


def displayPerson(id, personData):
    pass

def main(url):
    print(f"Running main with URL = {url}...")
    pass

if __name__ == "__main__":
    """Main entry point"""
   # parser = argparse.ArgumentParser()
   # parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
   # args = parser.parse_args()
   # main(args.url)
