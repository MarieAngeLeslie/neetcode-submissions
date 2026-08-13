class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_merged_position_and_speed = []
        cars_fleet = []
        latest_fleet_arrival_time = 0

        for i in range(len(position)) : 
            cars_merged_position_and_speed.append((position[i],speed[i]))        
        cars_merged_position_and_speed.sort(reverse=True)

        for i, elt in enumerate(cars_merged_position_and_speed) : 
            if (cars_fleet) : 
                arrival_time = (target - cars_merged_position_and_speed[i][0]) / cars_merged_position_and_speed[i][1]
                if(arrival_time <= latest_fleet_arrival_time) : 
                    continue
                else :
                    cars_fleet.append(arrival_time)
                    latest_fleet_arrival_time = arrival_time 
            else : 
                arrival_time = (target - cars_merged_position_and_speed[i][0]) / cars_merged_position_and_speed[i][1]
                cars_fleet.append(arrival_time)
                latest_fleet_arrival_time = arrival_time

        return len(cars_fleet)  

