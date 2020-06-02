import cv2
import os
import numpy as np

directories = ["TED", "No disease", "Other disease"];
new_directories = ["resized_TED", "resized_None", "resized_Other"];
ratio = 2.336;

for id, directory in enumerate(directories):
	os.mkdir("data/" + new_directories[id]);
	for root, dirs, files in os.walk("data/" + directory):
		for filename in files:
			try: 
				print(filename);
				img = cv2.imread("data/" + directory + "/" + filename);
				dimensions = img.shape;
				height = dimensions[0];
				width = dimensions[1];
				channels = img.shape[2];

				cropped_height = int(width/ratio);
				cropped_width = width;
				if (cropped_height > height):
					cropped_height = height;
					cropped_width = int(height*2.336);


				y = int((height-cropped_height)/2);
				x = int((width-cropped_width)/2);
				cropped_img = img[y:y+cropped_height, x:x+cropped_width];
				resized_img = cv2.resize(cropped_img, (233, 100))
				cv2.imwrite("data/" + new_directories[id] + "/" + filename, resized_img);

			except:
				print("ERROR with file " + filename);

os.mkdir("data/test");
os.mkdir("data/train");
os.mkdir("data/test/TED");
os.mkdir("data/test/No disease");
os.mkdir("data/test/Other disease");
os.mkdir("data/train/TED");
os.mkdir("data/train/No disease");
os.mkdir("data/train/Other disease");

for id, directory in enumerate(new_directories):
	for root, dirs, files in os.walk("data/" + directory):
		for filename in files:
			try:
				img = cv2.imread("data/" + directory + "/" + filename);
				p = np.random.choice(np.arange(1, 3), p=[0.8, 0.2])
				if (p == 1):
					cv2.imwrite("data/train/" + directories[id] + "/" + filename, img);
				else:
					cv2.imwrite("data/test/" + directories[id] + "/" + filename, img);

			except:
				print("ERROR with file " + filename);


