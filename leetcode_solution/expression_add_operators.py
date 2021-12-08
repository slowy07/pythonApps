class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        state = [(int(num[0]), 1, 0, num[0])]

        for d in num[1:]:
            d = int(d)
            next_state = []

            for last_digits, multiplier, sum_before, s in state:
                if last_digits > 0:
                    next_state.append(
                        (last_digits * 10 + d, multiplier, sum_before, f"{s}{d}")
                    )
                elif last_digits < 0:
                    next_state.append(
                        (last_digits * 10 - d, multiplier, sum_before, f"{s}{d}")
                    )

                next_state.append(
                    (d, 1, sum_before + last_digits * multiplier, f"{s}+{d}")
                )

                next_state.append(
                    (-d, 1, sum_before + last_digits * multiplier, f"{s}-{d}")
                )

                next_state.append((d, last_digits * multiplier, sum_before, f"{s}*{d}"))

            state = next_state

        result = []
        for last_digits, multiplier, sum_before, s in state:
            val = sum_before + multiplier * last_digits

            if val == target:
                result.append(s)

        return result
