import keras
from keras.models import Model
from keras.layers import Input, concatenate, Conv2D, MaxPooling2D, Conv2DTranspose, Dropout
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras.utils import plot_model
from keras import backend as K

K.set_image_data_format('channels_last') 

img_row = 32
img_col = 32
smooth = 1

def create_conv_layer(f,stride,activationfn,padding,prevlayer,dropout):

	conv = Conv2D(f,stride,activation=activationfn,padding=padding)(prevlayer)
	conv = Dropout(dropout)(conv)
	conv = Conv2D(f,stride,activation=activationfn,padding=padding)(conv)

	return conv

def maxpooling_fn(prevlayer):

	return MaxPooling2D(pool_size=(2,2))(prevlayer)

def concatenate_fn(f,kernal,stride,padding,src,dest):

	return concatenate([Conv2DTranspose(f,kernal,strides=stride,padding=padding)(src),dest],axis=3)

def dice_coef(y_true,y_pred):

	y_true_f = K.flatten(y_true)
	y_pred_f = K.flatten(y_pred)

	intersection = K.sum(y_true_f * y_pred_f)

	return (2. * intersection + smooth) / (K.sum(y_true_f) + K.sum(y_pred_f) + smooth)

def dice_coef_loss(y_true,y_pred):

	return -dice_coef(y_true,y_pred)

def getnetwork():

	inputs = Input((img_row,img_col,1))

	conv1 = create_conv_layer(32,(3,3),'relu','same',inputs,0.2)
	pool1 = maxpooling_fn(conv1)

	conv2 = create_conv_layer(64,(3,3),'relu','same',pool1,0.2)
	pool2 = maxpooling_fn(conv2)

	conv3 = create_conv_layer(128,(3,3),'relu','same',pool2,0.3)
	pool3 = maxpooling_fn(conv3)

	model = Model(inputs=[inputs],outputs=[pool3])

	model.compile(optimizer=Adam(lr=0.00001),loss=dice_coef_loss,metrics=[dice_coef])

	return model

model = getnetwork()
print(model.summary())
plot_model(model, to_file='model.png')