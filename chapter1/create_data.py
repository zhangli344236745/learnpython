import os
import pandas as pd


# os.makedirs(os.path.join(".","data"),exist_ok=True)
# data_file = os.path.join(".",'data','house_tiny.csv')
#
# with open(data_file,"w") as f:
#     f.write('NumRooms,Alley,col1,col2,col3,Price\n')  # 列名
#     f.write('NA,Pave,NA,NA,245274,127500\n')  # 每行表示一个数据样本
#     f.write('2,NA,1541,NA,45,106000\n')
#     f.write('4,NA,NA,415,554,178100\n')
#     f.write('NA,NA,NA,15,54154,140000\n')
data_file = os.path.join(".",'data','house_tiny.csv')
data = pd.read_csv(data_file)
print(data)

inputs,outputs = data.iloc[:,0:-1],data.iloc[:,5]
print(inputs)
print(outputs)
inputs = inputs.fillna(inputs.mean())
inputs = pd.get_dummies(inputs,dummy_na=True)
print(inputs)