# -*- coding: utf-8 -*-

"""
 usage: 
 
 $ baseline_taskAB.py gold_file system_file taskName
 
 - gold_file and system_file are tab-separated, UTF-8 encoded files
 - taskName is the name of the task (A|B)
 
"""

import argparse, sys
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import confusion_matrix


def preproc(infile, task):
    y = []
    
    reader = infile.readlines() 
    for row in reader:
        if row.startswith("id"):
            continue
        if task == "A":
            label = row.split('\t')[2]
        elif task == "B":
            label = row.split('\t')[3].rstrip()
        y.append(label)
        
    return y


def eval(y_test, y_predicted):    

    precision, recall, fscore, _ = score(y_test, y_predicted)
    print('\n     {0}   {1}'.format("0","1"))
    print('P: {}'.format(precision))
    print('R: {}'.format(recall))
    print('F: {}'.format(fscore))    
    #"""
    _, _, fscore, _ = score(y_test, y_predicted, average='macro')
    print('Macro-F1: {}'.format(fscore))

    print('\n Confusion matrix:')       
    print(confusion_matrix(y_test, y_predicted)) 

    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('test', help='haspeede test set')
    parser.add_argument('predicted', help='system output')
    parser.add_argument('task', type=str, help="the name of the task, i.e. A or B")
    args = parser.parse_args()  
    
    with open(sys.argv[1], 'r',encoding="utf8") as f:
        y_test = preproc(f,sys.argv[3])
        
    with open(sys.argv[2], 'r', encoding="utf8") as f:
        y_predicted = preproc(f,sys.argv[3])
        
    eval(y_test, y_predicted)
            
      
  