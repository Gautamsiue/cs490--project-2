import os
NEG_BEDS_DIR = "negs_beds"
NEG_CLEAN_DIR = "negs_clean"
POS_CLEAN_DIR = "pos_clean"
PREPPED_FILE = "prepped_seqs.txt"
MEAN = "mean.txt"
DATA = f"{PATH}/data"
TEST = f"{DATA}/test.txt"
TRAIN = f"{DATA}/train.txt"
VALID = f"{DATA}/validation.txt"
ONE_HOT_TRAIN = f'{DATA}/hot_train.npy'
ONE_HOT_TEST = f'{DATA}/hot_test.npy'
ONE_HOT_VALID = f'{DATA}/hot_validate.npy'
GNET = './Gnet'
NUCLEOS = ['A', 'T', 'C', 'G']
ALEXNETSAVE= './Alexnetsave'
PATH = os.getcwd()
