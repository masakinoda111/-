
#!python k_means.py
# -*- coding: utf-8 -*- #
import numpy as np
import matplotlib
# matplotlib.use('Agg') # この行を追記
import matplotlib.pyplot as plt
import sys

input_file = sys.argv[1]
print(input_file)

# data = np.genfromtxt(input_file,delimiter="     ",dtype=float)
# print(data)

f = open(input_file,"r")
lines = f.readlines()
f.close()

file_name = input_file[:-4]
print(file_name)


data=np.zeros((0,2))
for i in range(1,len(lines)):
    # print (lines[i])
    if lines[i][0] != '\n':
        tmp = lines[i].split()
        tmpar = [float(tmp[0])*100,float(tmp[1])*100]
        # print(tmpar)
        data = np.vstack((data,tmpar))
        # data.append(tmp)
        # print(tmpar)
        # print(data)

data = np.hstack((data,np.zeros((len(data),1))))
# print(data)

data_menseki = 1799
data_syuutyou = 201

while(True):
    bairitux=1
    bairituy=1
    if(data_menseki<1800):
        bairituy = 1801.0/(data_menseki)
    elif (data_menseki>1810):
        bairituy = 1799.0/(data_menseki)
    elif (data_syuutyou>200):
        bairitux = 199.0/(data_syuutyou)
    elif (data_syuutyou<190):
        bairitux = 201.0/(data_syuutyou)
    else:
        break

    data[:,0] *= bairitux
    data[:,1] *= bairituy
    data_menseki = 0
    data_syuutyou = 0
    for i in range(0,len(data)-1):
        data_menseki += data[i][0]*data[i+1][1] - data[i][1]*data[i+1][0]
        data_syuutyou += np.sqrt((data[i][0]-data[i+1][0])**2 + (data[i][1]-data[i+1][1])**2)
    print (data_menseki)
    print(data_syuutyou)



# グラフを描画
plt.scatter(data[:,0],data[:,1])
plt.show()  

data_o = []
for i in range(len(data)):
    print(str(data[i]))
    data_o.append(str(data[i][0])+'\t'+str(data[i][1])+'\t'+'0'+'\n')
file_output = open(file_name+'.txt',"w")
file_output.write('\n'.join(data_o))
file_output.close()