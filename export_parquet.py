import pandas as pd
import numpy as np
import itertools
from sklearn.model_selection import train_test_split

chunks = pd.read_json("train.jsonl",lines=True,chunksize=300000,compression='')
indexChunk = 0
for initialDf in chunks:
    initialDf.info()
    print(initialDf.shape)
    print(initialDf.head(2))


    initialDf['countEv'] = [len(ev) for ev in initialDf['events'] if ev]


    # Obtain list of all the events by unpacking the json file
    events = [event for session in initialDf['events'] for event in session]


    sessionsSeq = [np.full(initialDf['countEv'].iloc[i], initialDf['session'].iloc[i]) for i in range(len(initialDf['session']))]
    sessions = [session for seq in sessionsSeq for session in seq]

    eventsSession = np.hstack((np.reshape(sessions,[-1,1]),np.reshape(events,[-1,1])))

    events = pd.DataFrame([[row[0],row[1]['aid'], row[1]['type'], row[1]['ts']] for row in eventsSession], columns=['sessionId','aid', 'type', 'ts'])
    events['ts'] = pd.to_datetime(events['ts'],unit='ms')
    events = events.set_index('ts')


    events.to_parquet("train_"+str(indexChunk)+".parquet")
    indexChunk = indexChunk +1

