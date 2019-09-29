# py-image-compare-tool
A python function to compare images and calculate a similarity index

## Overview
<p>This repository consists of a Python program that
- Takes a CSV file as input
- Parses the CSV file which consists of paths to the images to be compared
- Calculates the difference or "similarity index", a number between 0 and 1 , 0 being identical images and 1 being completely dissimilar images </p>

## Prerequisites/ Assumptions
 <p>
 (1) Python 3 : You need to have  Python 3 installed on your system
 </p>
 (2) pip: You need to have pip (for Python3) installed. It usually comes installed with Python. Alternatively, you can get it from https://pip.pypa.io/en/stable/installing/ .
 </p>
 <p>
  (3) pipenv: Although not absolutely necessary, it is highly recommended that you use pipenv to utilize this repository as that will ensure that it functions on most Operating systems.
  </p>
 <p>
 (4) The images that are being compared are of equal size (i.e, Height  and Width). If they are not, logic can be added to the code to first resize both images to a fixed size before performing the  comparison, using opencv's <strong>resize<strong> module.
 </p>

## Usage
</p>  - Clone this repository</p>
</p>  - Change to the root directory of the repository</p>
 </p> - If using pipenv(recommended), activate pipenv using: <strong>pipenv shell</strong>, and install the required packages by running: <strong>pipenv -r install requirements.txt</strong> </p>
 </p> - Run python py-compare.py, which should prompt you to input the path to a CSV file (which contains a list of images, separated into two rows)</p>

## Assumptions:
<p> (1)You have Python 3 installed
</p>
<p>
(2) You have pip (for Python3) installed. It usually comes installed with Python. Alternatively, you can get it from https://pip.pypa.io/en/stable/installing/ .
</p>
<p>
(3) The images that are being compared are of equal size (i.e, Height  and Width). If they are not, logic can be added to the code to first resize both images to a fixed size before performing the  comparison, using OPENCV's <strong>resize</strong> module.
</p>
 ## How it works:
 <p> When you first invoke the program, it prompts you to enter the path to a CSV file. It is assumed that the file is structured into two columns titled image1 and image2 and each row gives the paths to a pair of images that are desired to be compared.</p>
 <p> The program then utilizes modules from <strong>csv</strong> and </strong>pandas</strong> libraries to parse the file and extract the images and pass them as arguments to a separate function. This function utilizes the <strong>opencv</strong> to perform the comparison if the images using the subtract methods.
 </p>
