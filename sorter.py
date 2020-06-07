import cv2
import os
import numpy as np

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


