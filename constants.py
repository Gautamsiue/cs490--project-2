import os
NEG_BEDS_DIR = "negs_beds"
NEG_CLEAN_DIR = "negs_clean"
POS_CLEAN_DIR = "pos_clean"
PREPPED_FILE = "prepped_seqs.txt"
MEAN = "mean.txt"
data = f"{PATH}/data"
TEST = f"{data}/test.txt"
TRAIN = f"{data}/train.txt"
VALID = f"{data}/validation.txt"
train_one_hot = f'{data}/hot_train.npy'
test_one_hot = f'{data}/hot_test.npy'
valid_one_hot= f'{data}/hot_validate.npy'
GNET = './Gnet'
NUCLEOS = ['A', 'T', 'C', 'G']
ALEXNETSAVE= './Alexnetsave'
PATH = os.getcwd()
