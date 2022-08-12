import copy
import random


class Node:
    def __init__(self , data=None , location=None):
        self.data = data
        self.location = location
        self.utara = None
        self.selatan = None
        self.barat = None
        self.timur = None
        self.barat_laut = None
        self.timur_laut = None
        self.barat_daya = None
        self.tenggara = None

class ChessBoard:
    def __init__(self , panjang , lebar , initialState):
        self.panjang = panjang
        self.lebar = lebar
        self.data = {}
        self.utama = initialState.copy()
        self.initialState = initialState
        self.alreadyExplored = []
        self.alreadyExplored.append(initialState)
        for x in range(self.lebar):
            for y in range(self.panjang):
                if (str(x) + str(y)) in self.initialState:
                    self.data[str(x) + str(y)] = Node(data='Q'+ str(y+1), location=(x , y))
                else:
                    self.data[str(x) + str(y)] = Node(data=None, location=(x , y))
        for x in self.data.keys():
            x_int = int(x[0])
            y_int = int(x[1]) 
            if x_int == 0  and y_int == 0:
                self.data[x].selatan = self.data['10']
                self.data[x].timur = self.data['01']
                self.data[x].tenggara = self.data['11']
            if x_int == 0 and y_int != 0 and y_int != (self.panjang-1):
                self.data[x].barat = self.data[str(x_int)+str(y_int-1)]
                self.data[x].timur = self.data[str(x_int)+str(y_int+1)]
                self.data[x].tenggara = self.data[str(x_int+1)+str(y_int+1)]
                self.data[x].barat_daya = self.data[str(x_int+1)+str(y_int-1)]
                self.data[x].selatan = self.data[str(x_int+1) + str(y_int)]
            if x_int == 0 and y_int == (self.panjang-1):
                self.data[x].barat= self.data[str(x_int)+str(y_int-1)]
                self.data[x].selatan= self.data[str(x_int+1)+str(y_int)]
                self.data[x].barat_daya = self.data[str(x_int+1)+str(y_int-1)]
            if x_int != 0 and x_int != (self.lebar-1) and y_int == 0:
                self.data[x].utara= self.data[str(x_int-1)+str(y_int)]
                self.data[x].timur_laut = self.data[str(x_int-1)+str(y_int+1)]
                self.data[x].timur = self.data[str(x_int)+str(y_int+1)]
                self.data[x].tenggara = self.data[str(x_int+1) + str(y_int+1)]
                self.data[x].selatan = self.data[str(x_int+1) + str(y_int) ]
            if x_int != 0 and x_int != (self.lebar-1) and y_int != 0 and y_int != (self.panjang-1):
                self.data[x].utara = self.data[str(x_int-1) + str(y_int) ]
                self.data[x].timur_laut = self.data[str(x_int-1) + str(y_int+1)]
                self.data[x].timur = self.data[str(x_int) + str(y_int+1)]
                self.data[x].tenggara = self.data[str(x_int+1) + str(y_int+1)]
                self.data[x].selatan = self.data[str(x_int+1)+ str(y_int)]
                self.data[x].barat_daya = self.data[str(x_int+1) + str(y_int-1)]
                self.data[x].barat = self.data[str(x_int) + str(y_int -1 ) ]
                self.data[x].barat_laut = self.data[str(x_int-1) + str(y_int-1)]
            if x_int != 0 and x_int != (self.lebar-1) and y_int == (self.panjang-1):
                self.data[x].utara = self.data[str(x_int-1) + str(y_int)]
                self.data[x].barat_laut = self.data[str(x_int - 1) + str(y_int-1) ]
                self.data[x].barat =  self.data[str(x_int) + str(y_int-1)]
                self.data[x].barat_daya = self.data[str(x_int+1) + str(x_int-1)]
                self.data[x].selatan = self.data[str(x_int+1) + str(y_int)]
            if x_int == (self.lebar-1) and y_int == 0:
                self.data[x].utara = self.data[str(x_int-1) + str(y_int)]
                self.data[x].timur_laut = self.data[str(x_int-1) + str(y_int+1)]
                self.data[x].timur  = self.data[str(x_int) + str(y_int+1)]
            if x_int == (self.lebar -1 ) and y_int != 0 and y_int != (self.panjang-1):
                self.data[x].utara = self.data[str(x_int-1) + str(y_int )]
                self.data[x].timur_laut = self.data[str(x_int-1) + str(y_int+1)]
                self.data[x].timur = self.data[str(x_int) + str(y_int+1)]
                self.data[x].barat = self.data[str(x_int) + str(y_int-1)]
                self.data[x].barat_laut = self.data[str(x_int-1) + str(y_int-1)]
            if x_int == (self.lebar - 1) and y_int == (self.panjang -1):
                self.data[x].utara = self.data[str(x_int -1) + str(y_int)]
                self.data[x].barat_laut = self.data[str(x_int - 1) + str(y_int -1)]
                self.data[x].barat  = self.data[str(x_int) + str(y_int-1)]
    
    def updateInitalState(self):
        """
        ! Update State 
        ! Memperbarui lokasi queen di papan catur
        ! Lokasi yang baru tidaak boleh sama dengan sebelumnya
        """

        while True:
            whichRow = str(random.randint(0,self.panjang-1))
            whichColumn = str(random.randint(0,self.panjang-1))
            temp = whichRow + whichColumn
            whereColumn = int(whichColumn)

            before = self.initialState.copy()
            sementara = self.initialState[whereColumn]
            self.initialState[whereColumn] = temp
            
            if self.initialState == before:
                self.initialState[whereColumn] = sementara
            else:
                self.data[sementara].data = None
                self.data[temp].data = 'Q' + str(whereColumn+1)
                break
    def checkKey(self , key , first , second , h):
        tmp = str(first) + str(second)
        if tmp not in key:
            key.append(tmp)
    def getState(self):
        hasil = []
        for x in self.initialState:
            nilai = 8- int(x[0])
            hasil.append(str(nilai))
        return hasil
    
    def estimateCost(self):
        key = []
        h = 0
        for x in self.initialState:
            parent = self.data[x]
            current_timur_laut = parent.timur_laut
            while current_timur_laut :
                if current_timur_laut.data != None:
                   
                    first = int(parent.data[1])
                    second = int(current_timur_laut.data[1])
                    if first < second:
                        self.checkKey(key , first , second , h)
                    else:
                        self.checkKey(key , second , first , h)     

                current_timur_laut = current_timur_laut.timur_laut
            current_timur = parent.timur
            while current_timur:
                if current_timur.data != None:
                    first = int(parent.data[1])
                    second = int(current_timur.data[1])
                    if first < second:
                        self.checkKey(key , first , second , h)
                    else:
                        self.checkKey(key , second , first , h)    
                current_timur = current_timur.timur
            
            current_tenggara = parent.tenggara
            while current_tenggara:
                if current_tenggara.data != None:
                    
                    first = int(parent.data[1])
                    second = int(current_tenggara.data[1])
                    if first < second:
                        self.checkKey(key , first , second , h)
                    else:
                        self.checkKey(key , second , first , h)
                current_tenggara = current_tenggara.tenggara             
            current_barat = parent.barat
            while current_barat:
                if current_barat.data != None:
                    
                    first = int(parent.data[1])
                    second = int(current_barat.data[1])
                    if first < second:
                        self.checkKey(key , first , second , h)
                    else:
                        self.checkKey(key , second , first , h)
                current_barat = current_barat.barat
            
            current_barat_laut = parent.barat_laut
            while current_barat_laut:
                if current_barat_laut.data != None:
                    
                    first = int(parent.data[1])
                    second = int(current_barat_laut.data[1])
                    if first < second:
                        self.checkKey(key , first , second,h)
                    else:
                        self.checkKey(key , second , first , h)
                current_barat_laut = current_barat_laut.barat_laut            
                        
            current_barat_daya = parent.barat_daya
            while current_barat_daya:
                if current_barat_daya.data != None:
                    
                    first = int(parent.data[1])
                    second = int(current_barat_daya.data[1])
                    if first < second:
                        self.checkKey(key , first , second , h)
                    else:
                        self.checkKey(key , second , first , h)
                current_barat_daya = current_barat_daya.barat_daya
        return len(key) , key





"""
! How to represent state as string

"""


population = []       
state_first = ['00' , '01' , '02' , '03' , '04' , '05' , '06' , '07'] 
chess = ChessBoard(panjang=8 , lebar=8 , initialState=state_first)




                    

    

class Data:
    def __init__(self,state , chromosome , value , persen=None):
        self.state  =state
        self.chromosome = chromosome
        self.value = value
        self.persen = persen



"""
! Initial Population
"""


for x in range(10):
    
    heuristic , pair = chess.estimateCost()    

    temp = copy.deepcopy(chess)
    
    not_attack = 28 - heuristic
    
    data = chess.getState()
    
    tempData = Data(temp , data , not_attack )
    
    population.append(tempData)

    chess.updateInitalState()
    


def calculation(population):
    
    total = 0
    for x in population:
        total = total + x.value
    for x in population:
        x.persen = x.value /total
        #print("Value : " , x.value)
        #print("Total : " , total)
        #print("Persen : " , round(x.persen * 100))
        #what = what + round(x.persen * 100)

nilai = None
"""
! Selection 
! Truncantion Selection
"""
def reproduce(male , female):
    #print("Male : " , male.value)
    #print("Female : " , female.value)

    first_child = male.chromosome[0:3] + female.chromosome[3:8]
    second_child = female.chromosome[0:3] + male.chromosome[3:8]

    # print("First Child : " , first_child)
    # print("Second Child : " , second_child)

    return first_child , second_child

for x in range(1000): 
    calculation(population)
    population.sort(key=lambda x:x.value ,reverse=True)
    first_child , second_child = reproduce(population[0] , population[1])  
    positionchildOne = random.randrange(0,8)
    positionChildTwo = random.randrange(0 ,8)

    whatPointOne = random.randrange(1,9)
    whatPointSecond = random.randrange(1, 9)

    first_child[positionchildOne] = whatPointOne
    second_child[positionChildTwo] = whatPointSecond

    #print(first_child)
    #print(second_child)

    newPoint = [ str(8-int(i)) for i  in first_child ]
    newPointSecond = [str(8-int(i)) for i in second_child]

    count = 0
    for x in range(len(newPoint)):
        newPoint[x] = newPoint[x] + str(x)
        newPointSecond[x] = newPointSecond[x] + str(x)

    #print(newPoint)
    #print(newPointSecond)

    chess = ChessBoard(panjang=8 , lebar=8 , initialState=newPoint)
    chess_second = ChessBoard(panjang=8 , lebar=8  , initialState=newPointSecond)

    heuristic , pair = chess.estimateCost()
    heuristic_second , pair_second = chess.estimateCost()

    #print(heuristic)
    #print(heuristic_second)

    #print("First Child" , 28 - heuristic)
    #print("Second Child " , 28 - heuristic_second)
    if ((28 - heuristic) == 28) or (( 28 - heuristic_second) == 28):
        break
    else:
        temp_first = copy.deepcopy(chess)
        temp_second = copy.deepcopy(chess_second)
        
        data_first = Data(temp_first , chess.getState() , 28 - heuristic)
        data_second = Data(temp_second , chess_second.getState() , heuristic_second)
        population.append(data_first)
        population.append(data_second)


print(population[0].value)
"""
! Cross Over
! Single Point
"""

    



"""
! Mutation
"""

