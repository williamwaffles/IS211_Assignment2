import argparse
import urllib.request
import logging
import datetime

#url containing needed data
user_url = urllib.request.Request('http://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')

#function that downloads the needed data
def downloadData(url):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        return content

#function that parses the data into a dictionary with a tuple as a value
def processData(file_content):
    parsed_dict ={}
    header = True
    for data in file_content.split('\n')[:-1]:
        if header:
            header = False
            continue
        else:
            parsed_data = data.split(',')
            #stripped_date = datetime.datetime.strptime((parsed_data[2]), '%d/%m/%Y')
            #logger.error('Error processing line <linenum> for ID <id>”,')
            #print(stripped_date)
            parsed_dict[parsed_data[0]] = (parsed_data[1], parsed_data[2])
            #print(parsed_dict)
    return parsed_dict

    #format = "%d %m %y"
    #list_data = datetime.datetime.strptime(index, format)
        #print(i)

#print(downloadData(user_url))

#print(processData(downloadData(user_url)))

new_dict = processData(downloadData(user_url))

def displayPerson(id, personData):
    new_id = personData[str(id)]
    name = new_id[0]
    birthday = new_id[1]
    print(id)
    print(new_id)
    print(name)
    print(birthday)
    '''if personData.get(new_id):
        print('hi!')
    else:
        print('No user with that ID.')
'''
    for id in personData:
        print(id)
        print(personData[id])
        print(id, 'hi')
        if str(id) == new_id:
            print("Data was found")
            break
        else:
            print("Data was not found")
            break




    '''if id == personData[id]:
        return personData[id]
    else:
        

        if id == personData[id]:
            print('Person ', id, 'is ', pes)'''

displayPerson(3, new_dict)

def main(url):
    print(f"Running main with URL = {url}...")
    pass

if __name__ == "__main__":
    """Main entry point"""
   # parser = argparse.ArgumentParser()
   # parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
   # args = parser.parse_args()
   # main(args.url)
