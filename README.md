The machine learning task has two parts - symbol classification and determination of the optimal classifier parameter.

Data provided by Eyedea Recognition, some data are from public resources.

Problem
The task is to design a classifier / character recognition program. The input is a small grayscale image of one handwritten character - a letter or number - the output is a class decision, i.e. the recognition of the character in the image.

You are given training data, a set of images with the information on the correct classification. This is usually all that the customer provides. After you prepare the code, the customer, in this case represented by the instructor, will use different test data on which to evaluate your work. We recommend dividing the provided data into a training and test set.

Your resulting code will be tested on the new data within the AE system.

Data
The images are in the png format in one folder, where we also provide the file truth.dsv (dsv format). The file names are not related to the file content. The file truth.dsv has on each line file_name.png:character, e.g. img_3124.png:A. The separator character is :, which is never in the name of the file. The names of the files contain only characters, numbers or underscores (_).

train_1000_10.zip images 10×10, 20 classes, 50 exemplars for each.
train_1000_28.zip images 28×28, 10 classes, 100 exemplars for each
train_700_28.zip images 28×28, 10 classes, varying number of exemplars
Interface specification
Implement k-NN and Naive Bayes classifiers. The main code will be in classifier.py

>> python3.8 classifier.py -h
usage: classifier.py [-h] [-k K] [-b] train_path test_path

Learn and Classify image data

positional arguments:
  train_path  Path to the training data
  test_path   Path to the testing data

optional arguments:
  -h, --help  show this help message and exit
  -k K        run K-NN classifier
  -b          run Naive Bayes classifier
  -o name     name (with path) of the output dsv file with the results
Example
python3 classifier.py -k 3 -o classification.dsv ./train_data ./test_data 
runs 3-NN training and testing (classification) classifier and saves the data as classification.dsv. The saved data must be of the same format as truth.dsv.



Selection of optimal classifier
Very often, there are many classifiers that can be used for a ML task, and we have to make a decision about which is the best classifier for the task. In the zip archive classif_result_tables.zip, there are all files that will be used for the task. The task shall be solved in Python. What is asked to be uploaded are a pdf report and one function related to the part Safety first.

We have 5 different learned binary classifiers. The result of the classification of each classifier depends on the value of the 
α
 parameter. Thus, the result of the classification of a given classifier can be expressed as a function 
C(x,α)∈{0,1}, where x is a vector which belongs to the sample we want to classify.

We tested all classifiers on a test set 
X={x0,x1,…,x99}. At the same time, we tried all possible values of 
α∈{α0,α1,…,α49}. For a classifier i∈{1,2,…,5} we obtain a table with values Ci(xj,αk)∈{0,1}, where j∈{0,1,..,99},k∈{0,1,..,49} (see C1, C2, C3, C4, C5 in classif_result_tables.zip). The real labels of the samples x0,x1,…,x99 from the test set are available (see GT in classif_result_tables.zip).

Selection of appropriate parameter
In this section, suppose that the classifiers are used for binary classification of images (e.g. whether a dog is on the picture or not). For the classifier 1 (table C1), determine the best value for parameter 
{α0,α1,…,α49}. Be aware that you don’t know the concrete task for which the classifier will be used. Therefore, it is necessary to use a sufficiently general approach. In other words, the classifier should not be one that is optimal for a particular task but globaly inefficient for most other tasks.

In a short (definitely shorter than one A4 page) pdf report explain the choice of the parameter (use terms such as sensitivity, false positive, ROC curve etc.). Inside the report, put the figure of a ROC curve with a marked point on the curve which correspond to the optimal value of the parameter.

Top secret!
Imagine, that you are an agent 00111 and you want to use your fingerprint to secure some top secret documents. The data are very sensitive, so it is better to delete them than secure them poorly. You also know that you will always have enough time to unlock the data. Five trained classifiers (with different 
α values) are available. The input of the classifier is a fingerprint scan. For your fingerprint, desired output of the classifier is 1 (data will be unlocked), 0 otherwise (if it is not your fingerprint). All classifiers were tested using the test set 
X for all possible values of the parameter 
α. Results of the test for the classifiers are saved in tables C1, C2, C3, C4, C5 (see above). Ground truth values (real fingerprint affiliation) of the different scans are also available (see GT)

Select the most suitable classifier and its α parameter.

In the pdf report write your choice and explain the criterias you used for the choice.

Safety first
This part is a continuation of the previous part Top secret!. A colleague, also an agent, will send you his classifier which also depends on the parameter 
α. However, you are not sure about his loyalty, as he may be a double agent. Thus, it will be necessary to find if his classifier is better than the classifier you selected in the previous section.

For security reasons, you will have to make the decision about his classifier using a function that will be created in advance. Input of the function will be table C6 with the results of the classification on the set for different 
α parameters (same format as C1, C2, etc.) and eventually other input parameters of your choice. The output of the function should be the decision if the new classifier is better than the one that you selected yourself (true if the obtained classifier is better than the previous one, false otherwise). In the pdf report explain the criterias that the function use. Submit also the function.

References
Christopher M. Bishop. Pattern Recognition and Machine Learning. Springer Science+Bussiness Media, New York, NY, 2006.

T.M. Cover and P.E. Hart. Nearest neighbor pattern classification. IEEE Transactions on Information Theory, 13(1):21–27, January 1967.

Richard O. Duda, Peter E. Hart, and David G. Stork. Pattern classification. Wiley Interscience Publication. John Wiley, New York, 2nd edition, 2001.

Vojtěch Franc and Václav Hlaváč. Statistical pattern recognition toolbox for Matlab. Research Report CTU–CMP–2004–08, Center for Machine Perception, K13133 FEE. Czech Technical University, Prague, Czech Republic, June 2004. http://cmp.felk.cvut.cz/cmp/software/stprtool/index.html.

Michail I. Schlesinger and Václav Hlaváč. Ten Lectures on Statistical and Structural Pattern Recognition. Kluwer Academic Publishers, Dordrecht, The Netherlands, 2002.

 
