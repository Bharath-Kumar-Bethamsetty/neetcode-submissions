class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        n = len(speed)
        if n == 0:
            return 0
        dist_n_time = []
        for i in range(n):
            dist_n_time.append((position[i], (target - position[i])/speed[i]))

        dist_n_time.sort(reverse=True)
        fleet = 1
        curr_fleet = dist_n_time[0][1]

        for dist, tm in dist_n_time[1:]:
            if tm > curr_fleet:
                curr_fleet = tm
                fleet += 1
        
        return fleet
        