#!/usr/bin/env python3
import os
#------------------------------------------------------------------------------
#-This file contains all the method defs for creating and editing files on HDD-
#------------------------------------------------------------------------------

#Each website crawled will be a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project " + directory)
        os.makedirs(directory)

#create a queue to put (to be crawled) links and
# a crawled data structure to keep track of what sites have already been crawled
#Ex params:          theNewBoston   https://thenewboston.com/
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'      #list of links to be crawled
    crawled = project_name + '/crawled.txt'  #list of links already crawled
    if not os.path.isfile(queue):           #check to see if queue.txt already created
        write_file(queue, base_url)              #The first time queue.txt created, base_url placed inside as starting point
    if not os.path.isfile(crawled):         #check to see if crawled.txt already created
        write_file(crawled, '')

#Create a new file
def write_file(path, data):
    fh = open(path, 'w')#'w' used to write to a file
    fh.write(data)
    fh.close()

#Add data to an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:#'a' used to append to a file
        file.write(data + '\n')

#Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass#keyword when you want to do nothing

#We want to read file to a set as opposed to a list, in order to avoid duplicates
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as fh:#'rt' stands for read textfile
        for line in fh:
            results.add(line.replace('\n', ''))
    return results

#Iterate through a set, each item will correspond to a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):#could just as easily put line as varname instead of links here
        append_to_file(file, link)


