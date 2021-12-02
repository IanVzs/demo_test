import torch

# Model
model = torch.hub.load('./yolov5', 'yolov5s', source='local')  # or yolov5m, yolov5l, yolov5x, custom

# Images
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list
img_local = './zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list
img_local = '../axie_some/images/20211025-160926.png'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
# results = model(img)
results = model(img_local)

# Results
print("-*-" * 12)
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
