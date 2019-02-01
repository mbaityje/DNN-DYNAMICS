from functions import *  # functions.py contains useful functions
import argparse
import numpy as np
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--log_dir", type=str, nargs='+', required=True)
parser.add_argument("--X", type=float, required=False, default=0.7)

args = parser.parse_args()

def find_tx(X, times, accuracy):
	'''Returns the time at which the accuracy becomes larger than X'''
	if accuracy[-1]<X:
		return np.infty
	if accuracy[0]>X:
		return 0
	itx=np.where(accuracy>X)[0][0]
	return times[itx]


for directory in args.log_dir:
	runs = list(load_dir2(directory))

	for irun in range(len(runs)):
		run = runs[irun]  # pick the first one
		dynamics = run['dynamics']  # list containing many measures during the training
		model_init, model_last, trainset, testset = load_run(runs[0])


		times    = np.array([dynamics[it]['step'] for it in range(len(dynamics))])
		loss     = np.array([dynamics[it]['train'][1] for it in range(len(dynamics))])
		error    = np.array([dynamics[it]['train'][3] for it in range(len(dynamics))])/ run['desc']['p']
		accuracy = 1-error

		tx=find_tx(args.X, times,accuracy)
		print(args.X, tx)
		# ax=plt.subplot(111)
		# ax.plot(times,accuracy, label='Accuracy')
		# ax.plot(times,X*np.ones(len(times)), label='0.8')
		# ax.set_ylabel('Train Accuracy')
		# ax.set_xlabel('time')
		# plt.show()











#Plot loss
from matplotlib import pyplot as plt
times    = np.array([dynamics[it]['step'] for it in range(len(dynamics))])
loss     = np.array([dynamics[it]['train'][1] for it in range(len(dynamics))])
error    = np.array([dynamics[it]['train'][3] for it in range(len(dynamics))])/len(trainset[1])
accuracy = 1-error


ax=plt.subplot(211)
ax.plot(times,loss)
ax.set_ylabel('Train Loss')
ax.set_xlabel('time')
# plt.show()



