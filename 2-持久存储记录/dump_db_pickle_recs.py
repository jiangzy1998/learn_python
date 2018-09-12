import pickle
import glob

for fielname in glob.glob('*.pkl'):  # 针对 bob， sue， tom
    recfile = open(fielname, 'rb')
    record = pickle.load(recfile)
    print(fielname, '=>\n', record)

suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])  # 获取sue的名字
