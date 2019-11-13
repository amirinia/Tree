import pandas as pd 

df = pd.read_csv('TreeLevel.csv')
print(df.sort_values("Level",ascending=False))



import networkx as nx
import matplotlib.pyplot as plt 
import random
G = nx.Graph()
for index, row in df.iterrows():
    #print(row['Function'])
    G.add_node(row['Function'],pos=(random.randint(1,1000),row['Level']))
nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=400)
        #ani = animation.FuncAnimation(fig, animate, interval=1000)


listf = df['Level']
print(max(listf))
for i in range(max(listf)):
    print("level ",max(listf)-i)
    print(df.loc[df['Level'] == max(listf)-i])

#for index,row in df.iterrows():
#    print(row.Level)

plt.show()