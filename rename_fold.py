import os

# TEST = "Test"
# TRAIN = "Train"
dir = './{local_directory}'


## 폴더명 자체를 바꿀때
# for name in os.listdir(dir):
#     path = os.path.join(dir, name)
#     rename = name.split('(label)')[0]
#     dir_name = os.path.join(dir, rename)
#     os.rename(path, dir_name)

## 폴더 하나만 바꿀때
# i = 1
# for plant_name in os.listdir(dir):
#     path = os.path.join(dir, plant_name)
#     print(path)
#     c_plant_n = dir.split('/')[-1]
#     print(c_plant_n)
#     dst = 'a'#c_plant_n + str(i) + '.jpg'
#     dst = os.path.join(dir, c_plant_n)
#     os.rename(path,dst)
#     i += 1

## 두개이상 폴더에 파일명을 변경할때
for plant_name in os.listdir(dir):
    i = 1
    uniq = 1
    path = os.path.join(dir, plant_name)
    print(path)
    for name in os.listdir(path):
        src = os.path.join(path, name)
        if i >= 1:
            dst = plant_name + str(i) + '.jpg'
        if os.path.exists(dst):
            dst = plant_name + '(%d)' + '.jpg' % (uniq)
            uniq += 1
        dst = os.path.join(path, dst)
        os.rename(src, dst)
        i += 1

