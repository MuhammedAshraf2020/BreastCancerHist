
import numpy as np
import os
from tqdm import tqdm
import shutil
from sklearn.model_selection import train_test_split

code = {0:"Adenosis" , 1 : "Fibroadenoma" , 2 :"Phyllodes" , 
		3 : "Tubular",  4 : "Ductal",  5 : "Lobular" ,
		 6 : "Mucinous" , 7:"Papillary" }


class Data:
  def __init__(self , path , oversampling = True , ratio = [0.7 , 0.1 , 0.2]):
    self.path          = path
    self.main_classes  = ["benign" , "malignant"]
    self.source_paths  = ["train" , "test" , "val"]
    self.main_path     = os.getcwd() 
    self.ratio         = ratio
    self.partial_paths = []
    for folder in self.source_paths:
      folder_path = os.path.join(self.main_path , folder)
      try:
        os.state(folder_path)
      except:
        os.mkdir(folder_path)
        for i in range(8):
          partial_path = folder_path + "/" + code[i] 
          os.mkdir(partial_path)
          self.partial_paths.append(partial_path)
  def generate(self):
    Lists = self.get_pathes() # list of lists to get the pathes of every class in the main folder
    for index_class , Class in enumerate(Lists): # for class in Classes
      images_indeces = get_indeces(Class) # list of lists [list of train exs , list of test exs , list of val exs]
      for index , examples in enumerate(images_indeces): # list of train exs , //               , //
        distenation = images_indeces[index] + "/" + code[index_class]
        for img in examples:
          shutil.copy(Lists[img] , distenation)

  def get_indeces(self  , Class):
    len_list  = len(Class)
    len_list  = np.array(range(len_list))
    train_indeces , test_indeces = train_test_split(len_list , test_size = self.ratio[1])
    train_indeces , val_indeces  = train_test_split(train_indeces , test_size = self.ratio[2])
    return train.tolist() , test_indeces.tolist() , val_indeces.tolist()
  
  def get_pathes(self):
    LIST_PATHES = []
    for mc in self.main_classes:
      SOB_path = os.path.join(self.path , mc) + "/SOB"
      for cls in os.listdir(SOB_path):
        PATH = []
        cls_path  = SOB_path + "/" + cls
        for folder in tqdm(os.listdir(cls_path)):
          file_path = cls_path + "/" + folder + "/100X"
          for img in os.listdir(file_path): 
            img_path = os.path.join(file_path , img)
            PATH.append(img_path)
        LIST_PATHES.append(PATH)
    return LIST_PATHES