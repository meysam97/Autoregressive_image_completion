from trainARImage import trainARImage
from testARImage import testARImage
import pickle as pickle
import torch
torch.backends.cudnn.benchmark = True

train_path = './dataset/train/'
val_path = './dataset/val/'
test_path = './dataset/test/'

# training stage
# After running trainARImage for the first time, the training/validation 
# images are saved into imgs.npy.gz and info.p
# If you run it again, to avoid re-loading images from scratch, 
# set data_npy_exists to True below
# model, info = trainARImage(train_path, val_path, verbose=False, data_npy_exists = True)

# TO SAVE TIME for just testing code, uncomment the following 2 lines to load your pre-trained model
model = torch.load('model/model_epoch_40.pth', map_location=lambda storage, location: storage)["model"]
info = pickle.load( open( "info.p", "rb" ) )

# testing stage
testARImage(test_path, model, info, verbose=True)
