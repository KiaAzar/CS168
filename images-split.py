#!/usr/bin/python

import cv2
import os
import numpy as np

directories = ["ted", "none", "other"]

os.mkdir("samples/test");
os.mkdir("samples/train");
os.mkdir("samples/test/ted");
os.mkdir("samples/test/none");
os.mkdir("samples/test/other");
os.mkdir("samples/train/ted");
os.mkdir("samples/train/none");
os.mkdir("samples/train/other");

for id, directory in enumerate(directories):
	for root, dirs, files in os.walk("samples/" + directory):
		for filename in files:
			try:
				img = cv2.imread("samples/" + directory + "/" + filename);
				p = np.random.choice(np.arange(1, 3), p=[0.8, 0.2])
				if (p == 1):
					cv2.imwrite("samples/train/" + directories[id] + "/" + filename, img);
				else:
					cv2.imwrite("samples/test/" + directories[id] + "/" + filename, img);

			except:
				print("ERROR with file " + filename);


