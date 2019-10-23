# py-image-compare-tool
A python function to compare images and calculate a similarity index

## Overview
<p>This repository consists of a Python program that
- Takes a CSV file as input
- Parses the CSV file which consists of paths to the images to be compared
- Calculates the difference or "similarity index", a number between 0 and 1 , 0 being identical images and 1 being completely dissimilar images </p>

## Prerequisites/ Assumptions
 <p>
 [1] Python 3 : You need to have  Python 3 installed on your system
 </p>
 [2] pip: You need to have pip (for Python3) installed. It usually comes installed with Python. Alternatively, you can get it from https://pip.pypa.io/en/stable/installing/ .
 </p>
 <p>
  [3] pipenv: Although not absolutely necessary, it is highly recommended that you use pipenv to utilize this repository as this will ensure that it functions on most operating systems.
  </p>
 <p>
 [4] The images that are being compared are of equal size (i.e, Height  and Width). If they are not, logic can be added to the code to first resize both images to a fixed size before performing the  comparison, using opencv's <strong>resize</strong> module.
 </p>
 [5] the images are R, G, B images i.e, they consist of three individual pixel components, Red, Green and Blue.

## Usage
</p>  - Clone this repository</p>
</p>  - Change to the root directory of the repository</p>
 </p> - If using pipenv(recommended), activate pipenv using: <strong>pipenv shell</strong>, and install the required packages by running: <strong>pipenv -r install /path/to/requirements.txt</strong> </p>
 </p> - Run python py-compare.py, which should prompt you to input the path to a CSV file (which contains a list of images, separated into two rows)</p>
 <p> - The result is stored in the same CSV file.</p>


 ## How it works:
 <p> When you first invoke the program, it prompts you to enter the path to a CSV file. It is assumed that the file is structured into two columns titled image1 and image2 and each row gives the paths to a pair of images that are desired to be compared.</p>
 <p> The program then utilizes modules from <strong>csv</strong> and <strong>pandas</strong> libraries to parse the file and extract the images and pass them as arguments to a separate function. This function utilizes the <strong>opencv</strong> to perform the comparison if the images using the subtract methods.
 </p>
 <p> The image pair is compared using OPENCV's subtract method which will result in a 'difference image' consisting of '0' or '1' values for the individual R,G,B components. These components are extracted into three different variables and we use the 'countNonZero' method   to count the number of Non-zero pixels, where 0 results from identical pixels overlapping and 1 results from dissimilar pixels.
The total count is then normalized to result in a value between 0 and 1 where 0 = identical images and 1 = completely dissimilar images.
 
## References:
[i] pipenv: https://github.com/pypa/pipenv

[ii] Python CSV: https://docs.python.org/3/library/csv.html

[iii] OpenCV: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=2ahUKEwj68-CsvvfkAhUhVt8KHXKzC8gQFjABegQIARAC&url=https%3A%2F%2Freadthedocs.org%2Fprojects%2Fopencv-python-tutroals%2Fdownloads%2Fpdf%2Flatest%2F&usg=AOvVaw3zyOCJCjMjJ7F7syrUISIu

