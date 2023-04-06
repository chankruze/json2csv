import json
import os
import pandas as pd

if __name__ == '__main__':
    # ask the user for the file name
    input_file_name = input('Enter the input file name: ')
    # add the file extension
    input_file_name = input_file_name + '.json'

    # ask the user for the output file name
    output_file_name = input('Enter the output file name: ')
    # add the file extension
    output_file_name = output_file_name + '.csv'

    # get the path of the files
    input_file = os.path.join(os.getcwd(), input_file_name)
    output_file = os.path.join(os.getcwd(), output_file_name)

    # read the json file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # convert json array to pandas dataframe
    df = pd.DataFrame(data)

    # save the dataframe as csv file
    df.to_csv(output_file, index=False)
