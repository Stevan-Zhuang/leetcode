class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        h_vals = []
        prev_h = int(10e5) + 1
        for x, h in enumerate(height):
            if h == 0:
                prev_h = 0
                continue
            remove = False
            if h > prev_h:
                while h_vals:
                    h_top, h_bot, prev_x = h_vals[-1]
                    if h_top <= h: # Complete fill
                        rain += (x - prev_x - 1) * (h_top - h_bot)
                        h_vals.pop()
                        remove = True
                    else: # Partial fill
                        rain += (x - prev_x - 1) * (h - h_bot)
                        h_vals[-1][1] = h
                        break
            if h <= prev_h:
                if h_vals:
                    h_vals[-1][1] = h
                h_vals.append([h, 0, x])
            if h > prev_h:
                if h_vals and prev_h != 0 and not remove:
                    h_vals.pop()
                h_vals.append([h, 0, x])

            prev_h = h
        return rain
