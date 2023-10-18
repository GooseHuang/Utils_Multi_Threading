import multiprocessing
import os
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(FILE_PATH)

import pandas as pd
import numpy as np
def worker(df, threading_i, lock):

    with lock:
        print('Some information')

    ################################ code here ################################
    # Some code here
    pass


    ###########################################################################

    # Return something
    return




def main():

# ========================================= Multiprocessing =========================================
    lock = multiprocessing.Lock()

    df = pd.read_csv('../input/XXXX.csv')

    # Define the inputs
    N = 24 # 1,3,5,8,10,24
    # Split a dataframe called my_dataframe into 29 equal sub-dataframes
    inputs = np.array_split(df, N)
    print('Total Length:', df.shape[0])
    print('Batch Length:', max(int(df.shape[0]/N),1))

    # create a list of processes
    processes = []
    for i,sub_df in enumerate(inputs):
        # create a process and pass the input and output queues to it
        p = multiprocessing.Process(target=worker, args=(sub_df,i, lock))
        processes.append(p)
        p.start()

    # wait for all processes to finish
    for p in processes:
        p.join()



if __name__ == '__main__':
    main()
    print('\nDone!\n')