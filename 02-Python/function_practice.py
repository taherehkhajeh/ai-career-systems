def show_welcome():
    print("Wellcome to AI Career Project")
    print("Let's learn AI with me")
def show_next_step():
    print("Next step: practice python")

user_name = input("Enter your user name:")

def greet_user(name):
    print("Wellcome,", name)

def chek_study_hours(hours):
    if hours >=1:
        print("Good progress")
    else:
        print("Small progress")
daily_hours = input("Enter your daily study hours:")
daily_hours = float(daily_hours)
def calculate_weekly_hours(daily_hours):
    return daily_hours * 7




print("Program started")
greet_user(user_name)
show_welcome()
show_next_step()
chek_study_hours(2)
chek_study_hours(0.5)
weekly_hours = calculate_weekly_hours(daily_hours)
print(weekly_hours)
print("Program finished")
