High_scores = [45,56,66,78,98]
for i in range(len(High_scores)):
    print(i+1,".",High_scores[i])

score = int(input("Enter new high score:"))
High_scores.append(score)
High_scores.sort(reverse=True)
for i in range(len(High_scores)):
    print(i+1,".",High_scores[i])

