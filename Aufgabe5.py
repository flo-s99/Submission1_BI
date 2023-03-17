import random as rd

# Wahrscheinlichkeit für einen Jackpot (Formel aus https://www.studysmarter.de/schule/mathe/stochastik/lotto-formel/)
numerator = 1
denominator = 1
for i in range(6):
    numerator *= (45 - i)
    denominator *= (i + 1)
probability = numerator / denominator
print("Die Wahrscheinlichkeit für einen Lotto Jackpot beim österreichischen System (6 aus 45) beträgt: 1 zu", int(probability))

lotto_nums = rd.sample(range(1, 46), 6)
print("Die Lottozahlen sind:", lotto_nums)
