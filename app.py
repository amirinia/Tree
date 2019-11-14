import pandas as pd 

df = pd.read_csv('parent_child.csv')
print(df.sort_values("Level",ascending=False))



import networkx as nx
import matplotlib.pyplot as plt 
import random
G = nx.Graph()
for index, row in df.iterrows():
    #print(row['Function'])
    G.add_node(row['Function'],pos=(random.randint(1,1000),row['Level']))
        #ani = animation.FuncAnimation(fig, animate, interval=1000)


listf = df['Level']
print(max(listf))
for i in range(max(listf)):
    print("\n level ",max(listf)-i)
    print(df.loc[df['Level'] == max(listf)-i])
    #print(row['Parent']=="NaN")
for index, row in df.iterrows():
    if( pd.isna(row['Parent']) == False):
        print(row['Parent'],row['Function'],pd.isna(row['Parent']))
        G.add_edge(row['Function'],row['Parent'])

#for index,row in df.iterrows():
#    print(row.Level)
nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=400)

plt.show()