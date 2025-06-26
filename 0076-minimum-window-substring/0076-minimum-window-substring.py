class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)  # Counts of chars in t
        window_count = {}
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window_count[c] = window_count.get(c, 0) + 1

            if c in t_count and window_count[c] == t_count[c]:
                have += 1

            while have == need:
                # update result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # shrink from left
                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
        
        