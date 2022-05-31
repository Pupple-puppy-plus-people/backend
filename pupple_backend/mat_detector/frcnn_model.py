import os
import numpy as np
import torch
import torchvision
from PIL import Image
from torchvision import transforms, datasets, models
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import time
# from bs4 import BeautifulSoup

# def generate_box(obj):
#     # training dataset에서서 box 지정
#     xmin = float(obj.find('xmin').text)
#     ymin = float(obj.find('ymin').text)
#     xmax = float(obj.find('xmax').text)
#     ymax = float(obj.find('ymax').text)
    
#     return [xmin, ymin, xmax, ymax]

# adjust_label = 1

# def generate_label(obj):
#     # mat detected : 2, other : 1
#     if obj.find('name').text == "with_mat":

#         return 1 + adjust_label

#     return 0 + adjust_label

# def generate_target(file): 
#   # boxes, label 데이터 생성
#     with open(file) as f:
#         data = f.read()
#         soup = BeautifulSoup(data, "html.parser")
#         objects = soup.find_all("object")

#         num_objs = len(objects)

#         boxes = []
#         labels = []
#         for i in objects:
#             boxes.append(generate_box(i))
#             labels.append(generate_label(i))

#         boxes = torch.as_tensor(boxes, dtype=torch.float32) 
#         labels = torch.as_tensor(labels, dtype=torch.int64) 
        
#         target = {}
#         target["boxes"] = boxes
#         target["labels"] = labels
        
#         return target


# class TestDataset(object):
#     def __init__(self, transforms, image):
#         self.transforms = transforms
#         # self.img = image
#         self.img = Image.open(image).convert("RGB")

#     def __getitem__(self,idx): #special method
#         # load images ad masks
#         img = self.transforms(self.img)
#         return img

#     def __len__(self): 
#         return 3

# class MatDataset(object):
#     def __init__(self, transforms, path):
#         '''
#         path: path to train folder or test folder
#         '''
#         # transform module과 img path 경로를 정의
#         self.transforms = transforms
#         self.path = path
#         self.imgs = list(sorted(os.listdir(self.path)))


#     def __getitem__(self, idx): #special method
#         # load images ad masks
#         file_image = self.imgs[idx]
#         file_label = self.imgs[idx][:-4] + 'xml'
#         img_path = os.path.join(self.path, file_image)
        
#         if 'test' in self.path:
#             label_path = os.path.join("test_annotations/", file_label)
#         else:
#             label_path = os.path.join("annotations/", file_label)

#         img = Image.open(img_path).convert("RGB")
#         #Generate Label
#         target = generate_target(label_path)
        
#         if self.transforms is not None:
#             img = self.transforms(img)

#         return img, target

#     def __len__(self): 
#         return len(self.imgs)

# data_transform = transforms.Compose([  # transforms.Compose : list 내의 작업을 연달아 할 수 있게 호출하는 클래스
#         transforms.ToTensor() # ToTensor : numpy 이미지에서 torch 이미지로 변경
#     ])

# def collate_fn(batch):
#     return tuple(zip(*batch))

# # for training data
# dataset = MatDataset(data_transform, 'images/')
# test_dataset = MatDataset(data_transform, 'test_images/')
# data_loader = torch.utils.data.DataLoader(dataset, batch_size=4, collate_fn=collate_fn)
# test_data_loader = torch.utils.data.DataLoader(test_dataset, batch_size=10, collate_fn=collate_fn)

def get_model_instance_segmentation(num_classes):
      
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    return model
