from bisect import bisect_right

class Solution:
    def maxValue(self, events, k):
        events.sort()
        starts = [e[0] for e in events]
        n = len(events)

        memo = {}

        def dp(i, remaining):
            if i == n or remaining == 0:
                return 0
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            # Option 1: Skip current event
            skip = dp(i + 1, remaining)

            # Option 2: Take current event
            next_i = bisect_right(starts, events[i][1])
            take = events[i][2] + dp(next_i, remaining - 1)

            memo[(i, remaining)] = max(skip, take)
            return memo[(i, remaining)]

        return dp(0, k)
