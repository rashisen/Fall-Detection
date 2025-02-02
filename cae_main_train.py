from models import *
from ae_exp import AEExp
import numpy as np


def init_cae_exp(pre_load = None):
	'''
	These are the training setting. 
	'''
	batch_size = 32

	hor_flip = True
	zoom_range = 0

	regularizer_list = []
	epochs = 2
	img_width, img_height = 64,64

	dset = 'UR-Filled'
	initial_epoch = 0

	#Convautoencooder-------------------

	model, model_name, model_type = CAE(img_width = img_width, 
		img_height = img_height)

	convautoencoder_experiment = AEExp(model = model, img_width = img_width,\
	img_height = img_height, model_name = model_name, model_type = model_type, \
	pre_load = pre_load, initial_epoch = initial_epoch,\
	epochs = epochs, batch_size = batch_size, hor_flip = hor_flip, zoom_range = zoom_range, dset = dset
	)

	return convautoencoder_experiment

if __name__ == "__main__":

	cae_exp = init_cae_exp()

	cae_exp.set_train_data(raw = False)

	data = cae_exp.train_data.reshape(len(cae_exp.train_data), 64, 64, 1)
	cae_exp.train()
