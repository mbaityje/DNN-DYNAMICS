from functions import *  # functions.py contains useful functions

log_dir = "R40d40h5L"
runs = list(load_dir2(log_dir))
print("{} runs in this directory".format(len(runs)))  # 1 if you ran the command above

run = runs[0]  # pick the first one
print("{depth} layers of {width} units trained on {p} points".format(**run['desc']))

dynamics = run['dynamics']  # list containing many measures during the training

model_init, model_last, trainset, testset = load_run(runs[0])

print("Final train loss : {}".format( dynamics[-1]['train'][1]  ))
print("Final train error: {}".format( dynamics[-1]['train'][3] / run['desc']['p'] ))
print("Final train accuracy: {}".format( 1 - dynamics[-1]['train'][3] / run['desc']['p'] ))


#Plot loss
from matplotlib import pyplot as plt
times    = np.array([dynamics[it]['step'] for it in range(len(dynamics))])
loss     = np.array([dynamics[it]['train'][1] for it in range(len(dynamics))])
error    = np.array([dynamics[it]['train'][3] for it in range(len(dynamics))])/run['desc']['p'])
accuracy = 1-error


ax=plt.subplot(211)
ax.plot(times,loss)
ax.set_ylabel('Train Loss')
ax.set_xlabel('time')
# plt.show()

ax=plt.subplot(212)
ax.plot(times,accuracy)
ax.set_ylabel('Train Accuracy')
ax.set_xlabel('time')
plt.show()


