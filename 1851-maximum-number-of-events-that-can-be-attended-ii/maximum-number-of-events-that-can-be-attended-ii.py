from bisect import bisect_right

class Solution:
    def maxValue(self, events, k):
        # Sort events by end time
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Extract start times for binary search
        start_times = [event[0] for event in events]

        # Initialize DP table: dp[i][j] = max value using first i events and at most j selections
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find last non-overlapping event using binary search
            prev = self.findLastNonOverlapping(events, i - 1, start)

            for j in range(1, k + 1):
                # Option 1: skip current event
                # Option 2: take current event + best from prev
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[prev + 1][j - 1] + value
                )

        return dp[n][k]

    def findLastNonOverlapping(self, events, right, targetStart):
        # Binary search to find last event ending before targetStart
        left = 0
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if events[mid][1] < targetStart:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
