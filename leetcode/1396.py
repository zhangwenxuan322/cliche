# 1396. Design Underground System
from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.all_times = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_station, check_in_time = self.check_in[id]
        self.all_times[check_in_station + ', ' + stationName].append(t - check_in_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.all_times[startStation + ', ' + endStation]) / len(
            self.all_times[startStation + ', ' + endStation])


undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)  # Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20)  # Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22)  # Customer 32 "Paradise" -> "Cambridge" in 22 - 8 = 14
print(undergroundSystem.getAverageTime("Paradise",
                                       "Cambridge"))  # return 14.00000.One trip "Paradise" -> "Cambridge", (14) / 1 = 14
print(undergroundSystem.getAverageTime("Leyton",
                                       "Waterloo"))  # return 11.00000.Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))  # return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38)  # Customer 10 "Leyton" -> "Waterloo" in 38 - 24 = 14
print(undergroundSystem.getAverageTime("Leyton",
                                       "Waterloo"))  # return 12.00000.Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12
