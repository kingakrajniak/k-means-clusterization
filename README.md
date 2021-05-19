# k-means-clusterization
Script using k-means algorithm to split the data into two groups.

## General info
Short Python script for spliting dataset of black and red cats (45 photos: 40 training and 5 testing) into two groups using k-means clusterization. Each photo is descripted by its histogram.

## Technologies
- Python 3.7
### Libraries
- OpenCV
- glob
- NumPY
- scikit-learn

## Setup
In command window put (?):
$ python -m pip install https://github.com/kingakrajniak/k-means-clusterization.git
## Problems
- 0 and 1 for 'red cat' and 'black cat' aren't universal. Sometimes the clusters are switched and photos don't match the descriptions.

## Sources
Photos from google.