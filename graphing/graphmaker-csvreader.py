#!/usr/bin/python3

# from python std library
import csv

# python3 -m pip install np
import numpy as np
# python3 -m pip install matplotlib
import matplotlib
matplotlib.use('Agg')
# sudo apt install python3-tk
import matplotlib.pyplot as plt

def parsecsvdata():
    """returns a list. [0] is 10gb and [1] 25gb data"""
    summary = [] # list that will contain [(10gb), (25gb)]

    # open csv data
    with open("/home/student/mycode/graphing/2018summary3.csv",\
     "r") as downtime:
        # parse csv data with csv.reader
        downdata = csv.reader(downtime, delimiter=",")
        for row in downdata:
            rowdat = (int(row[0]), int(row[1]), int(row[2]), int(row[3]),int(row[4]), int(row[5]), int(row[6]))
            summary.append(rowdat) # add dict to list
    return summary

def main():
    N = 4
    ## grab our data
    summary = parsecsvdata() # grab our data
    localnetMeans = summary[0] # 10gb data
    wanMeans = summary[1] # 25gb data

    ind = np.arange(N)    # the x locations for the groups
    # the width of the bars: can also be len(x) sequence
    width = 0.35

    # describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    # Describe the table metadata
    plt.ylabel("Length of Outage (IOPS)")
    plt.title("2018 Network Test Summary")
    plt.xticks(ind, ("T1", "T2", "T3", "T4", "T5", "T6", "T7" ))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("10gb", "25gb"))

    # SAVE the graph locally
    plt.savefig("/home/student/mycode/graphing/2018summaryv3.png")
    # Save to "~/static"
    plt.savefig("/home/student/static/2018summaryv3.png")       
    print("Graph created.")

if __name__ == "__main__":
    main()

