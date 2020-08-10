import matplotlib.pyplot as plt
import math

data = [[1,6,0],[2,3,0],[5,6,1],[1,1,0],[3,3,1],[5,7,1],[4,2,1],[9,1,1],[0,4,0],
        [2,6,0],[3,7,1],[1,4,0],[4,6,1]]
defined_point = [3,4]
distances = []
alldistances = []
datax = []
datay = []

class KNN():
    def __init__(self):
        pass
    
    def getDistances(self):
        global k
        for a in range(len(data)):
            distance_verify = (math.sqrt(((defined_point[0]-data[a][0])**2) + ((defined_point[1]-data[a][1])**2)))
            if distance_verify <= k:
                distances.append(data[a][2])
            else:
                alldistances.append([distance_verify,data[a][2]])
        list.sort(distances)
        list.sort(alldistances)
    
    def nearestNeighbour(self):
        prediction1 = distances.count(0)
        prediction2 = distances.count(1)
        if prediction1 > prediction2:
            print('prediction is red')
        elif prediction2 > prediction1:
            print('prediction is blue')
        elif prediction1 == 0 and prediction2 == 0:
            self.otherScenario()
        elif prediction1 == prediction2:
            self.otherScenario()
        else:
            print('something went wrong')
            
    def prediction(self):
        prediction = alldistances[0][1]
        if prediction == 1:
            print('prediction is blue')
        else:
            print('prediction is red')
    
    def otherScenario(self):
        if alldistances[0][0] != alldistances[1][0]:
            self.prediction()
        else:
            try:
                for b in range(len(alldistances)):
                    if alldistances[0][0] == alldistances[1][0] and alldistances[0][1] != alldistances[1][1]:
                        del alldistances[0]
                        del alldistances[0]
                    else:
                        self.prediction()
                        break
            except IndexError:
                if len(alldistances) == 0:
                    print('cannot classify point')
                else:
                    self.prediction()
                    
    def scatter(self):
        for x in range(len(data)):
            datax.append(data[x][0])
        for y in range(len(data)):
            datay.append(data[y][1])
            
if __name__ == "__main__":
    knn = KNN()
    k = 2
    knn.getDistances()
    knn.nearestNeighbour()
    knn.scatter()
    
    plt.scatter(datax, datay)
    plt.scatter(defined_point[0], defined_point[1])
    plt.show()