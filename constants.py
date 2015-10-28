__author__ = 'foxcarlos'
from os import getcwd
from os.path import expanduser, join
import ConfigParser

PROTOCOL_VERSION = 3

dataFolderPath = expanduser('~')
currentPath = getcwd()
myFileConfig = 'ob.cfg'
finalFileConfig = join(currentPath, myFileConfig)
fc = ConfigParser.ConfigParser(allow_no_value=True)
fc.read(finalFileConfig)

# name of section in Config File ob.cfg
mySection = 'CONSTANTS'

# if exist the sections in file config
if fc.has_section(mySection):
    # capture info
    data_f1 = join(dataFolderPath, fc.get(mySection, 'DATA_FOLDER'))
    data_f2 = join(data_f1, '')  # is necesary for "/" the end
    seed_n = fc.get(mySection, 'SEED_NODE')
    seed_n_p = fc.getint(mySection, 'SEED_NODE_PORT')
    seed_n_t = fc.get(mySection, 'SEED_NODE_TESTNET')
    seed_n_t_p = fc.getint(mySection, 'SEED_NODE_TESTNET_PORT')
    ks = fc.getint(mySection, 'KSIZE')
    alp = fc.getint(mySection, 'ALPHA')
    trans_f = fc.getint(mySection, 'TRANSACTION_FEE')

    DATA_FOLDER = data_f2
    SEED_NODE = (seed_n, seed_n_p)
    SEED_NODE_TESTNET = (seed_n_t, seed_n_t_p)
    KSIZE = ks
    ALPHA = alp
    TRANSACTION_FEE = trans_f
