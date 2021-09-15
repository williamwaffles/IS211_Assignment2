import argparse
import urllib.request
import logging
import datetime

#url containing needed data
user_url = urllib.request.Request('http://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')

#function that downloads the needed data
def downloadData(url = 'http://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        return content

#function that
def processData(file_content):
    parsed_dict ={}
    header = True
    for data in file_content.split('\n'):
        if header:
            header = False
            continue
        else:
            parsed_data = data.split(',')
            parsed_dict[parsed_data[0]] = (parsed_data[1], parsed_data[2])
            print(parsed_dict)
            continue
    return parsed_dict

    #format = "%d %m %y"
    #list_data = datetime.datetime.strptime(index, format)
        #print(i)
'''
    with file_content as f:
        reader = list(f)
        print(map(lambda x: dict(zip(reader[0], x)), reader))
 '''

print(downloadData(user_url))

processData(downloadData(user_url))


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
