class Dinglemouse(object):   
    def __init__(self, queues, capacity):
        self.queues = [list(queue) for queue in queues]
        self.capacity = capacity
        
    def theLift(self):
        stops = [0]
        direction = 1 # 1 for up -1 for down
        top_floor = len(self.queues) - 1
        start_floor = 0
        end_floor = top_floor
        people = [] # people in the elevator
        
        while not (all(queue == [] for queue in self.queues) and people == []): # there are people waiting or in the lift
            start_floor = int(-0.5*top_floor*(direction-1))
            end_floor = int(0.5*(top_floor+2)*direction + 0.5*top_floor)
            direction = - direction
            
            for  floor in range(start_floor,end_floor, -direction):
                # check if people can be left in current floor
                if floor in people:
                    stops.append(floor)
                while floor in people:
                    people.remove(floor)
                # check if people can enter    
    
                if self.queues[floor] != []:
                    queue_after = self.queues[floor].copy()
                    for person in self.queues[floor]:
                        if  -floor*direction < -person*direction:
                            if len(people) < self.capacity:
                                people.append(person)
                                queue_after.remove(person)
                            if stops[-1] != floor:
                                stops.append(floor)
                    self.queues[floor] = queue_after
        if stops[-1] != 0:
            stops.append(0) # return to ground
        print(stops)
        return stops
    
    
    
queues = [[ ( (),   (),    (5,5,5), (),   (),    (),    () ),     [0, 2, 5, 0]          ],
         [ ( (),   (),    (1,1),   (),   (),    (),    () ),     [0, 2, 1, 0]          ],
         [ ( (),   (3,),  (4,),    (),   (5,),  (),    () ),     [0, 1, 2, 3, 4, 5, 0] ],
         [ ( (),   (0,),  (),      (),   (2,),  (3,),  () ),     [0, 5, 4, 3, 2, 1, 0] ]]


skata = [[], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

lift = Dinglemouse(skata, 5)
lift.theLift()

#
#[0, 6, 5, 0, 5, 4, 0, 4, 3, 0, 3, 2, 0, 1, 0] should equal 
#[0, 6, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 3, 2, 1, 0, 1, 0]