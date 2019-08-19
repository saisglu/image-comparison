### image-comparison
* In this python project we are comparing images using SSIM technique, where it differentiate the images with the value of similarity and we are calculating the elapsed-time.

##Dependencies

* In this project required packages/dependencies are defined in the requirements.txt file.

* To install the required files need to run the following command in terminal. before executing the command we need cd to the file directory.

  *      pip3 install -r requirements.txt

##How to know my code is working?
 * To check my code works properly or not I written a test case.
 * Test case file name is ssim-test.py, In the testcase file need to give comparing images absolute paths. 
 * Run ssim-test.py file by below command.
 
 *       pytest
   
##How to use this program.
 * Initially you need to give the list of images absolute paths in test.csv file.
 * In the run.py file you need to give the path for the test.csv & result.csv file.
 * Run the below command to use this program and generate the result.csv file.
 *       python3 run.py
 * In the result.csv file we can see the image1, image2, similarity, elapsed.
 * To use this application in windows need to follow the above steps.
 
 
 
 
 