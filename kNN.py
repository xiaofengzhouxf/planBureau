# k-NearestNeighbor classify
#
# @auther jason.zhou
from numpy import *
import operator

# test data
def createDataSet():
	group = array([  [1.0,1.1],[1.0,1.0],[0,0],[0,0.1]   ])
	labels = ['A','A','B', 'B']
	return group,labels


#  classify the inX
#
# @param inX : input data
# @param dataSet  : sample data set
# @param labels classify  : labels
# @param k : num of nearest Neighbor
def classify_Knn(inX, dataSet, labels, k):
	#caculate distance , shape arrry
	##  == 4
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize,1)) - dataSet ## distance between two group
	sqDiffMat = diffMat**2  #power
	sqDistances = sqDiffMat.sum(axis=1)   ##Euclidean distance
	
	distances = sqDistances**0.5
	
	#print distances

	sortedDistIndicies = distances.argsort() #sort by row, return array index

	#print sortedDistIndicies

	classCount={}
	#To obtain K point recently
	for i in range(k):
		votellabel = labels[sortedDistIndicies[i]]
		classCount[votellabel] = classCount.get(votellabel,0) + 1 
	
	#sort
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1), reverse=True)
	
	return sortedClassCount[0][0]

# norm
def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals, (m, 1) )
	normDataSet = normDataSet/tile(ranges, (m,1)) 
	return normDataSet, ranges, minVals


# main
if __name__ == '__main__':
	group,labels = createDataSet()
	
	print classify_Knn([0,0], group,labels,2)