scores = {
    "riazi1": 15,
    "mabani": 19,
    "fizik1": 16,
    "vasaya": 8,
    "arabi": 7,
    "shimi": 20,
    "zaban": 18,
}

for k, v in scores.items():
    if v >= 10:
        print("Passed :", k)
    else:
        print("Failed :", k)

average = sum(scores.values()) / len(scores)
print("Average :", average)
