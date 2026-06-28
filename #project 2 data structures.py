#project 2 data structures
scores = [2, 3, 6, 6, 5]

scores = list(set(scores))
scores.sort()

print("Runner-up score:", scores[-2])