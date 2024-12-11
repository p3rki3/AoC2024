import AoCFramework as AoC
import functools

def has_even_digits(num: int) -> int:
    count = 0 
    while num != 0: 
        num //= 10 
        count += 1 
    return count

@functools.lru_cache(None)
def blink(num: int, blinksleft: int) -> int:
    if blinksleft == 0:
        return 1
    else:
        if num == 0:
            newcount = blink(1, blinksleft - 1)
        else:
            count = has_even_digits(num)
            if count % 2 == 0:
                factor = 10 ** (count // 2)
                num1, num2 = num // factor, num % factor
                newcount = blink(num1, blinksleft - 1)
                newcount += blink(num2, blinksleft - 1)
            else:
                newcount = blink(num * 2024, blinksleft - 1)
    return newcount

def solve(blinks: int) -> int:
    return sum(blink(num, blinks) for num in Stones)

Stones = [int(num) for num in AoC.Init("data/day11.txt", test=False, nolines=True).split()]
AoC.verify(191690, 228651922369703)
AoC.run(solve(25), solve(75))
