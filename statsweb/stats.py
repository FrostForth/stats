"""
Created on Fri Nov 29 17:40:01 2019

@author: Kaitlin

1. Provide library of functions:
    - intialize
    - sample
    - graph
    - stats
    - output
2. Execute functions depending on version
    1. Import necessary libraries
        - os
        - sys
        - numpy
        - matplotlib pyplot and ticker
        - seaborn
        - pandas
        - math
    2. Set default variables
        - mean = 5.0
        - number of trials = 1000
        - bin size = 0.5
        - trial size = 50
    3. Use user-imputted values for variables if applicible
        1. Check for values from command line or input fields
        2. Update each corresponding value
    4. Take the sample
        1. Make a list of length t
        2. Append the average value of the list to list of averages
        3. Repeat n times
    5. Create and output graphs
        1. Histogram
        2. Dotplot
    6. Calculate statistical data
        - Mean
        - Standard Deviation
    7. Output results
        1. graphs and stats
        2. save to file if chosen in command line
        
"""

''' Libraries'''
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd
import math


'''
Description: Read data from a file
Params: csv file f
Output: List
'''


'''
Description: Sets default values for variables
Params: None
Output: list values containing the mean, number of trials, size of bins, and size of trials
'''
def initialize():
    #Probability
    p = 5.0
    #Number of trials
    n = 1000
    #Size of bins in percent integer
    b = 0.5
    #Size of trials
    t = 50
    #Create a list with core values
    values = [p, n, b, t]
    return values


'''
Description: Creates a random sample
Params: p, n, t
Output: list avg
'''
def sample(p, n, t):
    avg = []
    for i in range(n):
        list = np.random.choice(2,t, p=[(1-(p/10.0)),(p/10.0)])
        avg.append(sum(list)*10/t)
    return avg


'''
Description: Creates and outputs graphs
Params: avg, b
Output: histogram, dotplot
'''
def qualgraph(avg, b):
    b = b*10

    '''histogram'''
    bx = plt.figure()
    bx = sns.distplot(pd.Series(avg,name="Self-Rating"))
    
    
    '''dotplot :('''
    #number of bins
    bins = np.arange((100.0/b)+2)*b/10
    
    #figure scaling, axis labels, and ticks
    p = plt.figure(figsize=(10,20))
    ax = plt.axes()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(b/5))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(b/10))
    p.add_axes(ax)
    p.suptitle('Distribution of Averages', fontsize=20)
    plt.xlabel('Average', fontsize=18)
    plt.ylabel('Frequency', fontsize=18)
    
    #set up and set frequency and value tables
    hist, edges = np.histogram(avg,bins=bins,)#range=(0,10))
    y = np.arange(1,hist.max()+1)
    x = np.arange((100.0/b)+1)/(10.0/b)
    X,Y = np.meshgrid(x,y)
    
    #plot the points
    s = 1000/len(avg)
    plt.scatter(X,Y, c=Y<=hist, cmap="Greys",s=s)
    
    #save the figure to dot.png
    #p.savefig("dot")
    return bx, p
 
    
'''
Description: Calculates statistical data
Params: values, avg
Output: mean, standard deviance, if & why normally distributed
'''
def stats(avg):
    n = len(avg)
    
    #mean
    list = []
    m = sum(avg)/n
    
    #StDev
    for i in range(len(avg)):
        list.append(avg[i] - m)
    #print(avg)
    s = math.sqrt(sum(avg)/(n-1))
    
    return m,s


'''
Description: Saves output to file
Params: values, avg, stats, graphs, filenames
Output: updated output file
'''
def outputp(avg, stats, hist, dot, imgname, output):
    output.write("{}\n\nMean: {}\nStandard Dev: {}".format(avg,stats[0],stats[1]))
    hist.figure.savefig("Images\{}{}".format(imgname,1))
    dot.savefig('Images\{}{}'.format(imgname,2))
    

'''
Program to run when file is not imported
Same as web version
'''
if __name__ == '__main__':
    
    # Initialize values
    os.chdir(os.path.dirname(os.getcwd()))
    values = initialize()
    file = 0
    
    #Command line arguments
    if(len(sys.argv)):
        for i in range(1,len(sys.argv)):
            #Probability
            if sys.argv[i][0]=='p':
                values[0] = float(sys.argv[i][2:])
            #Number of Trials
            elif sys.argv[i][0]=='n':
                values[1] = int(sys.argv[i][2:])
            #Size of bins
            elif sys.argv[i][0]=='b':
                values[2] = float(sys.argv[i][2:])
            #Size of trials
            elif sys.argv[i][0]=='t':
                values[3] = int(sys.argv[i][2:])
            #Seed for trial generation
            elif sys.argv[i][0]=='s':
                s = int(sys.argv[i][2:])
                np.random.seed(s)
            #Flag for file reading
            elif '.csv' in sys.argv[i]:
                file = sys.argv[i]
            #error if not any of these
            else:
                raise ValueError(sys.argv[i],' is not a valid argument.')

    #Read file
    if (file):
        #print(file)
        data = pd.read_csv(file)
        #print(data)
        avg = [[],[]]
        for i in range(len(data.index)):
            if data.iloc[i,2]>=0:
                if (data.iloc[i,1] == 'A'):
                    avg[0].append(data.iloc[i,2])
                else:
                    avg[1].append(data.iloc[i,2])
                    
        'Group A'
        #Create graphs
        hist, dot = qualgraph(avg[0], values[2])
        
        #Create statistics
        statistics = stats(avg[0])
        
        #Output
        output = open('groupa.txt','w')
        imgname = 'a'
        outputp(avg[0], statistics, hist, dot, imgname, output)
        output.close()
        
        'Group B'
        #Create graphs
        hist, dot = qualgraph(avg[1], values[2])
        
        #Create statistics
        statistics = stats(avg[1])
        
        #Output
        output = open('groupb.txt','w')
        imgname = 'b'
        outputp(avg[1], statistics, hist, dot, imgname, output)
        output.close()
            
            
    else:
        #Take sample
        avg = sample(values[0],values[1],values[3])
    
        #Create graphs
        hist, dot = qualgraph(avg, values[2])
        
        #Create statistics
        statistics = stats(avg)
        
        #Output
        output = open('simresults.txt','w')
        imgname = 'sim'
        outputp(avg, statistics, hist, dot, imgname, output)
        output.close()