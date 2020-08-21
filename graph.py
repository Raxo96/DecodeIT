from collections import defaultdict
import time

class Graph:

    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(list)
    def addVerticle(self):
        self.V+=1

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def graph_keys(self):
        return self.graph.keys()

    def isReachable(self, s, d):
        visited =[False]*(self.V)
        queue=[]
        queue.append(s)
        visited[s] = True

        while queue:
            n = queue.pop(0)
            if n == d:
                 return True
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False

ip_list={}
counter=0
g = Graph(0)
# with open('test.txt') as f:
#     lines = [l.strip() for l in f.readlines()]
uin=[]
c_start = time.time()
while time.time()-c_start<0.02:
    uin.append(input())
for i in range(len(uin)):
    u_in = uin[i].split()
    action = u_in[0]
    start = u_in[1]
    end = u_in[2]
    if action == 'B':
        if start not in ip_list.keys():
            ip_list[start]=counter
            counter+=1
        if end not in ip_list.keys():
            ip_list[end]=counter
            counter+=1
        start = ip_list[start]
        end = ip_list[end]
        if start not in g.graph_keys():
            g.addVerticle()
        if end not in g.graph_keys():
            g.addVerticle()
        g.addEdge(start,end)
        g.addEdge(end,start)
    elif action =='T':
        if start not in ip_list.keys() or end not in ip_list.keys():
            print('N')
            continue
        if g.isReachable(ip_list[start],ip_list[end]):
            print('T')
        else:
            print('N')
