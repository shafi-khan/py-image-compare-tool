from __future__ import division
from datetime import datetime
import csv
import pandas as pd
import cv2


def parser(input_file):
    # Open the csv file  in read + write mode
    with open(input_file, mode='r+', newline='') as file:
            # Initialize a Dataframe using pandas and get the row count
            data = pd.read_csv(input_file)
            row_count = len(data.index)
            # Initialize empty lists to store values that are being calculated ahead
            sim_index = [None] * row_count
            elapsed_time = [None] * row_count
            elapsed_time_seconds = [None] * row_count

            # Read the input csv file into a variable
            csv_read = csv.DictReader(file)
            wr = csv.writer(file, quoting=csv.QUOTE_ALL)
            for i, row in enumerate(csv_read):
                # Calculate the timestamp before calling the compare function
                start_time = datetime.now()
                # Call the compare function
                sim_index[i] = compare_images(row["image1"],row["image2"])
                # Calculate timestap after calling the compare function
                end_time = datetime.now()
                # Measure the time time difference, in seconds
                elapsed_time[i] =  end_time - start_time
                elapsed_time_seconds[i] = elapsed_time[i].total_seconds()
                # print("Elapsed time: ",elapsed_time_seconds[i])
                #
                # print("Similarity: ",sim_index[i])

            # Add the elapsed time and similarity index columns to the csv  file
            data['Similarity Index'] = sim_index
            data['Elapsed Time'] = elapsed_time_seconds
            data.to_csv(input_file, index=False)

def compare_images(a,b):
    # Read the images
    first = cv2.imread(a)
    second = cv2.imread(b)

    # Get the size of any one image (Assuming both are same size i.e, Height X Width)
    imgsize = first.shape
    height = imgsize[0]
    width = imgsize[1]

    # Get the difference image(This will be in matrix form)
    difference = cv2.subtract(first,second)
    # RGB components of the 'difference image'
    blue = difference[:,:,0]
    green = difference[:,:,1]
    red = difference[:,:,2]
    # Calculate individual color differences
    blue_index = cv2.countNonZero(blue)
    green_index = cv2.countNonZero(green)
    red_index = cv2.countNonZero(red)

    # Calculate the Similarity Index, normalized to result in a value between 0 and 1.
    # 0 = Same image , 1 = Completely dissimilar images
    index = (blue_index + green_index + red_index) / (height*width*3)
    return index

def main():
    # Prompt user for input
    user_csv = input('Please enter the full path of the csv file: ')
    # Call the parser function
    parser(user_csv)

if __name__ == "__main__":
    main()
