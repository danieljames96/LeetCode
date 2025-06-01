class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        altitude = 0

        for i in gain:
            altitude += i
            max_altitude = max(altitude, max_altitude)

        return max_altitude