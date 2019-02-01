from functions import *  # functions.py contains useful functions
from matplotlib import pyplot as plt
import argparse
from os import path

def find_tx(X, times, accuracy):
	'''Returns the time at which the accuracy becomes larger than X'''
	if accuracy[-1]<X:
		return np.infty
	if accuracy[0]>X:
		return 0
	itx=np.where(accuracy>X)[0][0]
	return times[itx]

def find_N(h, L, d):
	assert L >= 1
	if d is None: 
		return h*h*L+h
	if L == 1:
		return h*(d-1)
	return h*( (d+1) + h * (L-1) )


parser = argparse.ArgumentParser()
parser.add_argument('--log_dir', default="output/R40d60p100N3L")
parser.add_argument("--X", type=float, required=False, default=0.7)
parser.add_argument("--showplots", action='store_true')
args=parser.parse_args()


runs = list(load_dir2(args.log_dir))
nrep=len(runs)
nt=len(runs[0]['dynamics'])
p  =runs[0]['desc']['p']
L  =runs[0]['desc']['depth']
h  =runs[0]['desc']['width']
dim=runs[0]['desc']['dim']
assert(all( [len(runs[i]['dynamics'])==nt for i in range(nrep)] ) ) #All runs need to have the same length
assert(all( [runs[i]['desc']['p']==p for i in range(nrep)] ) )      #All runs need to have the same number of data
assert(all( [runs[i]['desc']['depth']==L for i in range(nrep)] ) )      #All runs need to have the same depth
assert(all( [runs[i]['desc']['width']==h for i in range(nrep)] ) )      #All runs need to have the same width
assert(all( [runs[i]['desc']['dim']==dim for i in range(nrep)] ) )      #All runs need to have the same data size
N=find_N(h, L, dim)



#PLOT LOSS AND ACCURACY
ax1=plt.subplot(211, ylim=(0.0, 0.6), xscale='log')
ax2=plt.subplot(212, ylim=(0.5, 1.0), xscale='log')
for irun in range(nrep):
	times    = np.array([runs[irun]['dynamics'][it]['step' ]    for it in range(nt)])
	loss     = np.array([runs[irun]['dynamics'][it]['train'][1] for it in range(nt)])
	error    = np.array([runs[irun]['dynamics'][it]['train'][3] for it in range(nt)])/p
	accuracy = 1-error

	ax1.plot(times,loss)
	ax1.set_ylabel('Train Loss')
	ax1.set_xlabel('time')
	ax2.plot(times,accuracy)
	ax2.set_ylabel('Train Accuracy')
	ax2.set_xlabel('time')


# Now Averages
losses     = np.array([[runs[irun]['dynamics'][it]['train'][1] for it in range(nt)] for irun in range(nrep)])
accuracies = 1-np.array([[runs[irun]['dynamics'][it]['train'][3] for it in range(nt)] for irun in range(nrep)])/p
meanLoss = np.mean(losses,axis=0)
meanAcc  = np.mean(accuracies,axis=0)

tx=find_tx(args.X,times,meanAcc)

ax1.plot(times,meanLoss, linewidth=5, color='black', label='mean Loss')
ax1.set_ylabel('Train Loss')
ax1.set_xlabel('time')
ax1.legend()
ax2.plot(times,meanAcc, linewidth=5, color='black', label='mean Accuracy')
ax2.set_ylabel('Train Accuracy')
ax2.set_xlabel('time')
ax2.legend()

plt.savefig(path.basename(args.log_dir)+'_lossAcc.png')
if args.showplots: plt.show()



np.savetxt(	args.log_dir+"/t{}.txt".format(args.X), 
			np.column_stack([L, p, N, tx, args.X, np.max(meanAcc)]), 
			header="L p N t_{} X maxAcc".format(args.X),
			fmt="%d %d %d %g %g %g")
