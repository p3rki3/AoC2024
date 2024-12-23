import AoCFramework as AoC

def next_secret_num(num: int) -> int:
    num1 = ((num << 6) ^ num) % 16777216
    num2 = ((num1 >> 5) ^ num1)
    return ((num2 << 11) ^ num2) % 16777216

def get_all_scores(Prices):
    scores, Price_changes = dict(), [Prices[i]-Prices[i-1] for i in range(1, len(Prices))]
    for i in range(3, len(Price_changes)):
        pattern = (Price_changes[i-3], Price_changes[i-2], Price_changes[i-1], Price_changes[i])
        if pattern not in scores:
            scores[pattern] = Prices[i+1]
    return scores

def part_1():
    global Scores
    p1answer = 0
    for num in Nums:
        Prices, nxt_num = [num % 10], num
        for i in range(2000):
            nxt_num = next_secret_num(nxt_num)
            Prices.append(nxt_num % 10)
        p1answer += nxt_num
        newscores = get_all_scores(Prices)
        for key, val in newscores.items():
            if key not in Scores:
                Scores[key] = val
            else: Scores[key] += val
    return p1answer

Nums, Scores = [int(num) for num in AoC.Init("data/day22.txt")[0]], dict()
AoC.verify(19822877190, 2277)
AoC.run(part_1(), max(Scores.values()) )
