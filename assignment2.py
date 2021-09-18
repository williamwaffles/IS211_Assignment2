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
    linenum = -1
    for data in file_content.split('\n')[:-1]:
        linenum += 1
        if header:
            header = False
            continue
        else:
            parsed_data = data.split(',')
            try:
                stripped_date = datetime.datetime.strptime((parsed_data[2]), '%d/%m/%Y')
                parsed_dict[parsed_data[0]] = (parsed_data[1], stripped_date)
            except ValueError:
                logging.error(f'Error processing line:{linenum} for ID:{parsed_data[0]}')
    return parsed_dict


# takes in an id and a dictionary, checks if the id exists, and prints out the ID, name, and birthday of the associated person
def displayPerson(id, personData):
    #id_str = str(id)
    person = personData.get(id)
    print(personData.get(id))
    if person:
        print(f'Person {id} is {person[0]} with a birthday of {person[1]}')
    else:
        print('No such person exists.')

def main(url):
    print(f"Running main with URL = ...")

    pass

main(user_url)

if __name__ == "__main__":
    """Main entry point"""
    new_dict = processData(downloadData(user_url))
    while True:
        id = input('Please enter an ID number: ')
        id_int = int(id)
        displayPerson(id, new_dict)
        if id_int <= 0:
            break

   # parser = argparse.ArgumentParser()
   # parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
   # args = parser.parse_args()
   # main(args.url)
