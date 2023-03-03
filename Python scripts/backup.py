import os
import sys
import json
import configparser
from shutil import copytree

def read_config(filename='config.ini'):
    disk_list=[]
    src_folder=''
    dst_folder=''
    
    config = configparser.ConfigParser()
    
    config.read(filename)
	
    disk_list = config['Settings']['disk_list']
    src_folder = config['Settings']['src_folder']
    dst_folder = config['Settings']['dst_folder']
    
    return disk_list, src_folder, dst_folder

if __name__ == "__main__":
    filename = 'config.ini'
    if len (sys.argv) == 3:
        filename = sys.argv[1]
    else:
        print('Using default path to config file')
        
    disk_list, src_folder, dst_folder = read_config(filename)

    try:
        copytree(src_folder, dst_folder)
        print("Destination after copying", os.listdir(dst_folder))
    except OSError as err:
        print(err)