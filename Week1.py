class Edge:
    def __init__(self,f,t):
        self.__from_=f
        self.__to=t
    def set_from(self,f):
        self.__from_=f
    def get_from(self):
        return self.__from_
    def set_to(self,to):
        self.__to=to
    def get_to(self):
        return self.__to
    def __str__(self):
        return str(self.__from_)+" "+str(self.__to)



class AdjacencyMatrix:
    def __init__(self, matrix):
        self.__matrix=matrix

    def is_edge(self,v1,v2):
        return self.__matrix[v1][v2]
    
    def list_edge(self):
        _list=[]
        for i in range(len(self.__matrix)):
            for j in range(i,len(self.__matrix[i])):
                if self.__matrix[i][j]:
                    _list.append(Edge(i,j))

        return _list

    def list_nbrs(self,v):
        _list=[]
        for i in range(len(self.__matrix)):
            if self.__matrix[v][i]:
                _list.append(i)
        return _list

#--------------------------------------------------------------
class EdgeList:
    def __init__(self,_list):
        self.__list_=_list
    def is_edge(self,v1,v2):
        for i in self.__list_:
            if i.get_from()==v1 and i.get_to()==v2 or i.get_from()==v2 and i.get_to()==v1:
                return True
        return False

    def list_edge(self):
        return self.__list_.copy()

    def list_nbrs(self,v):
        _list=[]
        for i in self.__list_:
            if i.get_from()==v:
                _list.append(i.get_to())
            if i.get_to()==v:
                _list.append(i.get_from())
        return _list


#----------------------------------------------------------------

class AdjacencyList:
    def __init__(self,arr):
        self.__arr=arr
    def is_edge(self,v1,v2):
        for i in self.__arr[v1]:
            if i==v2:
                return True
        return False

    def list_edge(self):
        _list=[]
        for i in range(len(self.__arr)):
            for j in self.__arr[i]:
                if i<=j:
                    _list.append(Edge(i,j))
        return _list

    def list_nbrs(self,v):
        return self.__arr[v].copy()




matrix=[
    [0,1,1,1],
    [1,0,0,0],
    [1,0,0,1],
    [1,0,1,0]
]

am=AdjacencyMatrix(matrix)
el=EdgeList(am.list_edge())
mat=[
    [1,2,3],
    [0],
    [0,3],
    [0,2]
]
al=AdjacencyList(mat)


# for i in am.list_edge():
#     print(i.__str__())

# print(am.is_edge(2,0))

# print(am.list_nbrs(0))

# for i in el.list_edge():
#     print(i.__str__())

# print(el.is_edge(2,0))

# print(el.list_nbrs(0))

for i in al.list_edge():
    print(i.__str__())

print(al.is_edge(2,0))

print(al.list_nbrs(0))

print("this is my change!!!!")
print("this is the second cahge!!!!!!!!")
print("the theard change:)")


    
