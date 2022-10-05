# A TrainComposition is built by attaching and detaching wagons from the left and the right sides
from collections import deque

class TrainComposition:
    
    def __init__(self):
#         self.trainList = []
        self.trainList = deque()
        pass
    
    def attach_wagon_from_left(self, wagonId):
        """
        :param wagonId: (int) The number of the wagon to attach to the left
        """
        self.trainList.insert(0, wagonId)
        pass
    
    def attach_wagon_from_right(self, wagonId):
        """
        :param wagonId: (int) The number of the wagon to attach to the right
        """
        self.trainList.append(wagonId)
        pass

    def detach_wagon_from_left(self):
        """
        :returns: (int) The number of the wagon detached from left
        """
#         wagon = self.trainList[0]
#         self.trainList.remove(wagon)
#         return wagon
        return self.wagons.popleft() if self.wagons else None
    
    def detach_wagon_from_right(self):
        """
        :returns: (int) The number of the wagon detached from right
        """
#         wagon = self.trainList[len(self.trainList)-1]
#         self.trainList.remove(wagon)
#         return wagon
        return self.wagons.pop() if self.wagons else None
        

if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right()) # should print 7
    print(train.detach_wagon_from_left()) # should print 13
