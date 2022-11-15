import heapq
class node:
    def __init__(self,freq,symbol='',left = None ,right = None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    def __lt__(self, nxt):
        return self.freq < nxt.freq

chars = ['a','b','c','d','e','f']
freq=[50,10,30,5,3,2]
# freq = [5,9,12,13,16,45]
nodes =[]
for x in range(len(chars)):
    heapq.heappush(nodes,node(freq[x],chars[x]))

while len(nodes) > 1:
    a= heapq.heappop(nodes)
    a.huff = 0
    b= heapq.heappop(nodes)
    b.huff = 1
    temp = node(a.freq+b.freq,'',a,b)
    heapq.heappush(nodes,temp)
print(nodes)
def dfs(node,code):
    if node.symbol != '':
        print(node.symbol,code)
    if node.left is not None:
        dfs(node.left,code+'0')
    if node.right is not None:
        dfs(node.right,code+'1')

dfs(nodes[0],'')


