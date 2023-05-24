from scraper import get_citations_needed_count, get_citations_needed_report
import json

def write_json(file_path, data):

    '''
    This function takes in a file path and data and writes the data to a json file
    '''

    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
count = get_citations_needed_count(url)
report = get_citations_needed_report(url)

data = {
    'number_of_citations_needed': count,
    'citations_needed_report': report
}

file_path = 'citations.json'
write_json(file_path, data)

print("Data has been written to", file_path, "successfully!")