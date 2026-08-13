class TimeMap:

    def __init__(self):
        self.timeStamp_array = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeStamp_array : 
            self.timeStamp_array[key] = []
        self.timeStamp_array[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        elements = self.timeStamp_array.get(key, [])
        result = ""
        left_pointer, right_pointer = 0, len(elements) -1
        while left_pointer <= right_pointer : 
            mid = (left_pointer + right_pointer )//2
            if elements[mid][1] <= timestamp : 
                result = elements[mid][0]
                left_pointer = mid + 1
            else : 
                right_pointer = mid - 1
        return result
                
