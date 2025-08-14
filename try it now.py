# students scores
scores_book={"denis":98,"shema":90,"esther":50,"john":44,"sandra":80,"sofia":85,"zoob":30,"ruth":60,"master":58,"emma":20,"star":35,"rose":20}
# calculate the average scores
average_score=sum(scores_book.values())/len(scores_book)
print(f"average_scores:{average_score:.2f}")
# highest scores
highest_score = max(scores_book.values())
for name,score in scores_book.items():
    if score == highest_score:
        print(f"highest_score:{name}:with:{score}")
# update one student
scores_book["ruth"]=89
print(scores_book)
#students with scores above 80
print(f"students with scores above 80:")
for name,score in scores_book.items():
    if score> 80:
        print(f"{name}: {score}")
