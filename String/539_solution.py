class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        if len(timePoints) > len(set(timePoints)):
            return 0

        def calculate_mins(time1, time2):
            if time1[0:2] == time2[0:2]:
                return int(time2[3:5]) - int(time1[3:5])
            else:
                return 60 - int(time1[3:5]) + int(time2[3:5]) + 60 * (int(time2[0:2]) - int(time1[0:2]) - 1)

        sorted_timePoints = sorted(timePoints, key=lambda time: time[3:5])
        sorted_timePoints = sorted(sorted_timePoints, key=lambda time: time[0:2])

        sorted_timePoints.append(str(int(sorted_timePoints[0][0:2]) + 24) + sorted_timePoints[0][2:5])

        ret = calculate_mins(sorted_timePoints[0], sorted_timePoints[1])

        for i in range(len(sorted_timePoints) - 1):
            if sorted_timePoints[i] == sorted_timePoints[i + 1]:
                return 0
            diff = calculate_mins(sorted_timePoints[i], sorted_timePoints[i + 1])
            ret = min(ret, diff)

        return ret


