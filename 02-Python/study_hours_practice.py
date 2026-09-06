study_hours = input("Enter your study hours for today :")
study_hours = float(study_hours)

if study_hours >= 3:
    print("Great job")
elif study_hours >= 1:
    print("Good progress")
elif study_hours > 0:
    print("Small progress")
else:
    print("No study today")