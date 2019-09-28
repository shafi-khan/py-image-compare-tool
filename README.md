# py-image-compare-tool
A python function to compare images and calculate a similarity index

## Overview
<p>This repository consists of a Python program that
- Takes a csv file as input
- Parses the CSV file which consists of paths to the images to be compared
- Calculates the difference or "similarity index", a number between 0 and 1 , 0 being identical images and 1 being completely dissimilar images </p>

## Prerequisites
<p>
  - Python 3 : You need to have  Python 3 installed on your system
  - Pipenv: Although not absolutely necessary, it is highly recommended that you use pipenv to utilize this repository as that will ensure that it functions on most Operating systems .
</p>
## Usage
<p> 
  - Clone this repository
  - Change to the root directory of the repository
  - If using pipenv(recommended), activate pipenv using: **pipenv shell**
  - Run python py-compare.py, which should prompt you to input the path to a CSV file (which contains a list of images, separated into two rows)
  

