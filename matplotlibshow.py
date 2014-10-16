import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import operator

def show():
	datingDataMat = array([[ 0.03644456,  0.27849309,  0.11832173,  0.00573102],
       [ 0.88972708,  0.77340296,  0.96107136,  0.47103944],
       [ 0.95485912,  0.92376677,  0.80436754,  0.81541758],
       [ 0.80417579,  0.86723049,  0.79248537,  0.00182596]])
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
	plt.show()



if __name__ == '__main__':
	show()