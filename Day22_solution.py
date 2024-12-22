import AoCFramework as AoC

def next_secret_num(num: int) -> int:
    num1 = ((num * 64) ^ num) % 16777216
    num2 = ((num1 // 32) ^ num1) % 16777216
    return ((num2 * 2048) ^ num2) % 16777216

def get_all_scores(Prices, Price_changes):
    scores = dict()
    for i in range(len(Price_changes)-3):
        pattern = (Price_changes[i], Price_changes[i+1], Price_changes[i+2], Price_changes[i+3])
        if pattern not in scores:
            scores[pattern] = Prices[i+4]
    return scores

def part_1():
    global Scores
    p1answer = 0
    for num in Nums:
        Prices, nxt_num = [], num
        for i in range(2000):
            nxt_num = next_secret_num(nxt_num)
            Prices.append(nxt_num % 10)
        p1answer += nxt_num
        Price_changes = [Prices[i+1]-Prices[i] for i in range(len(Prices)-1)]
        newscores = get_all_scores(Prices, Price_changes)
        for key, val in newscores.items():
            if key not in Scores:
                Scores[key] = val
            else:
                Scores[key] += val
    return p1answer

Nums = [int(num) for num in AoC.Init("data/day22.txt")[0]]
Scores = dict()
AoC.verify(19822877190, 2277)
AoC.run(part_1(), max(Scores.values()) )
