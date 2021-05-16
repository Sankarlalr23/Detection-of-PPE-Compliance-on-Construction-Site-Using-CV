import os

path1 = 'men'
path2 = 'train5'
files = os.listdir(path1)

i = 74

for file in files:
    os.rename(os.path.join(path1, file), os.path.join(path2, 'ngimage'+ str(i)+'.jpg'))
    i = i+1
    if (file==0):
        break
