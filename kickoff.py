#%%
"""Vina single experiments runner"""
import os 
import sys
import subprocess
from wasabi import Printer
msg = Printer()

def read_txt(file_path):
	"""read a txt file and return a list of lines"""
	with open(file_path, 'r') as f:
		lines = f.readlines()
	return lines

def read_parameters(path):
	"""read the parameters from a txt file"""
	config_default = read_txt(path)
	receptor_line = [i for i in config_default if "receptor" in i][0]
	receptor = receptor_line.split("=")[1].strip()
	ligand_line = [i for i in config_default if "ligand" in i][0]
	ligand = ligand_line.split("=")[1].strip()
	center_x_line = [i for i in config_default if "center_x" in i][0]
	center_x = center_x_line.split("=")[1].strip()
	center_y_line = [i for i in config_default if "center_y" in i][0]
	center_y = center_y_line.split("=")[1].strip()
	center_z_line = [i for i in config_default if "center_z" in i][0]
	center_z = center_z_line.split("=")[1].strip()
	energy_line = [i for i in config_default if "energy" in i][0]
	energy = energy_line.split("=")[1].strip()
	exhaustiveness_line = [i for i in config_default if "exhaustiveness" in i][0]
	exhaustiveness = exhaustiveness_line.split("=")[1].strip()
	return {'receptor': receptor,
			'ligand': ligand,
			'center_x': center_x,
			'center_y': center_y,
			'center_z': center_z,
			'energy': energy,
			'exhaustiveness': exhaustiveness}


experiments_dir = os.path.join("data","experiments")
experiments = [i for i in os.listdir(experiments_dir) if os.path.isdir(os.path.join(experiments_dir,i))]

parameters = []
for experiment in experiments:
	parameters.append(read_parameters(os.path.join(experiments_dir,experiment,"ConfigDFU.txt")))

for parameter in parameters:
	msg.info("Running tests on ... {}".format(parameter['ligand']))

