import os

path1 = '/home/ctam/Desktop/SankarMTP/stage2/images/testset'
path2 = '/home/ctam/Desktop/SankarMTP/stage2/images/testimages'
files = os.listdir(path1)

i = 1

for file in files:
    os.rename(os.path.join(path1, file), os.path.join(path2, 'test'+ str(i)+'.jpg'))
    i = i+1
    if (file==0):
        break
