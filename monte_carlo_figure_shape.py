import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

obj = np.array(Image.open(r"C:\Desktop\image.png"))[:, :, 0]
plt.imshow(obj)
 
gen_num = 100
a = np.random.uniform(0, 740, gen_num)
b = np.random.uniform(0, 455, gen_num)
rand_map = np.vstack((a, b)).astype('int')
plt.plot(rand_map[0, :], rand_map[1, :], 'o')

#mapping
a = obj[rand_map[1, :], rand_map[0, :]] == 0
#find number of point in zone
number_of_p_in_zone = np.sum(a)


total_area = obj.shape[0]*obj.shape[1]
area = (number_of_p_in_zone/gen_num)*total_area

def MCarea(total_area, gen_num):
    obj = np.array(Image.open(r"C:\Desktop\image.png"))[:, :, 0]    
    a = np.random.uniform(0, len(obj[0, :]), gen_num)
    b = np.random.uniform(0, len(obj[:, 0]), gen_num)
    rand_map = np.vstack((a, b)).astype('int')
    plt.plot(rand_map[0, :], rand_map[1, :], 'o')
    
    #mapping
    a = obj[rand_map[1, :], rand_map[0, :]] == 0
    #find number of point in zone
    number_of_p_in_zone = np.sum(a)
    
    #area
    area = (number_of_p_in_zone/gen_num)*total_area
    
    return(area)


#test on stability
gen_test = np.arange(10, 50000, 150)
data = []
for i in range(len(gen_test)):
    print(i)
    data.append(MCarea(total_area, gen_test[i]))
    
plt.figure(figsize=(10,8))
plt.plot(gen_test, data)






