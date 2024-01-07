import numpy as np
import pandas as pd
data = pd.DataFrame(data=pd.read_csv("Dataset.csv"))
concept =np.array(data.iloc[:,0:-1])
target =np.array(data.iloc[:,-1])

def learn(concept,target):
    specific_h=concept[0].copy()
    general_h=[["?" for i in range(len(specific_h))]for i in range(len(specific_h))]
    for i,h in enumerate(concept):
        if target[i]=='yes':
            for x in range(len(specific_h)):
                if h[x] !=specific_h[x]:
                    specific_h[x]="?"
                    general_h[x][x]="?"
        if target[i]=='no':                    
            for x in range(len(specific_h)):
                if h[x] !=specific_h[x]:
                    general_h[x][x]=specific_h[x]
                else:
                    general_h[x][x]="?"
    indices = [i for i,val in enumerate(general_h) if val== ['?','?','?','?','?','?']]
    print(indices)
    for i in indices:
        general_h.remove(['?','?','?','?','?','?'])
    return specific_h,general_h

sfinal,gfinal =learn(concept,target)
print("final S :",sfinal,sep="\n")
print("final G :",gfinal,sep="\n")
data.head()




