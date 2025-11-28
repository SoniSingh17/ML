import random
import pandas as pd


names = ["Aarav", "Vivaan", "Aditya", "Kabir", "Arjun",
         "Diya", "Anaya", "Isha", "Kritika", "Riya",
         "Mohan", "Sohan", "Rohan", "Simran", "Priya",
         "Shreya", "Nikhil", "Tarun", "Varun", "Aditi"]

departments = ["CSE", "ECE", "EEE", "ME", "CE"]

data = []


for i in range(1, 21):
    row = {
        "roll_no": 1000 + i,
        "name": names[i - 1],
        "age": random.randint(18, 22),
        "department": random.choice(departments),
        "cgpa": round(random.uniform(6.0, 10.0), 2)
    }
    data.append(row)


df = pd.DataFrame(data)


print(df)


df.to_csv("students.csv", index=False)

print("\nDataset saved as 'students.csv'")   