from ae_exp import AEExp


if __name__ == "__main__":

	pre_load = './Models/DAE-relu_tanh-Dropout-Thermal.h5'
	pre_load = './Models/SDU-Filled/DAE-relu_tanh-Dropout-hor_flip.h5'
	pre_load = 'O:/AIRR/FallDetection-current/ThermalFallDetect2017/JNogasPy/Models/UR-Filled/DAE-relu_tanh-Dropout-UR-Filled.h5' #paper? Y


	hor_flip = True
	dset = 'UR-Filled'
	raw = True
	img_width, img_height = 64,64

	dae_exp = AEExp(pre_load = pre_load, hor_flip = hor_flip, dset = dset,\
		img_width = img_width, img_height = img_height, raw = False)

	dae_exp.test()