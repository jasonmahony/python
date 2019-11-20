#!/usr/bin/python3

from os import walk
from os import listdir
from os.path import isfile, join


# CFRS dir contains all the directories with RZ recommendation files
# This code runs from ../CFRS
mypath = "CFRS"
output_ec2_file_paths = []
output_asg_file_paths = []
output_rds_file_paths = []
ec2_output_file = "/Users/mahonyj/Desktop/output_file_ec2.csv"
asg_output_file = "/Users/mahonyj/Desktop/output_file_asg.csv"
rds_output_file = "/Users/mahonyj/Desktop/output_file_rds.csv"
account_dirs = [f for f in listdir(mypath)]
#account_ids = [account_name[:12] for account_name in account_dirs]

for account_dir in account_dirs:
    ec2_files = [f for f in listdir(mypath + "/" + account_dir) if "rightsizing-EC2.csv" in f]
    asg_files = [f for f in listdir(mypath + "/" + account_dir) if "rightsizing-ASG.csv" in f]
    rds_files = [f for f in listdir(mypath + "/" + account_dir) if "rightsizing-RDS.csv" in f]
    for output_f in ec2_files:
        output_ec2_file_path = f"{mypath}/{account_dir}/{output_f}"
        output_ec2_file_paths.append(output_ec2_file_path)
    for output_f in asg_files:
        output_asg_file_path = f"{mypath}/{account_dir}/{output_f}"
        output_asg_file_paths.append(output_asg_file_path)
    for output_f in rds_files:
        output_rds_file_path = f"{mypath}/{account_dir}/{output_f}"
        output_rds_file_paths.append(output_rds_file_path)

with open(ec2_output_file, 'w') as outfile:
    for f in output_ec2_file_paths:
        infile = open(f)
        account_id = f.split("/")[1][:12]
        print(f'ec2, {account_id}')
        lines = infile.readlines()[1:]
        for line in lines:
            outfile.write(account_id + "," + line)

with open(asg_output_file, 'w') as outfile:
    for f in output_asg_file_paths:
        infile = open(f)
        account_id = f.split("/")[1][:12]
        print(f'asg, {account_id}')
        lines = infile.readlines()[1:]
        for line in lines:
            outfile.write(account_id + "," + line)

with open(rds_output_file, 'w') as outfile:
    for f in output_rds_file_paths:
        infile = open(f)
        account_id = f.split("/")[1][:12]
        print(f'rds, {account_id}')
        lines = infile.readlines()[1:]
        for line in lines:
            outfile.write(account_id + "," + line)