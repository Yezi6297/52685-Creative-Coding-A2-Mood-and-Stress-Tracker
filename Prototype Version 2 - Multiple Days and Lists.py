print("Mood and Stress Tracker")
print("Please enter your commute, stress and mood information for Monday to Friday.")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

commute_times = []
stress_levels = []
mood_levels = []

for day in days:
    print("\nEnter data for", day)
    commute_time = int(input("Enter commute time in minutes: "))
    stress_level = int(input("Enter stress level (1-5): "))
    mood_level = int(input("Enter mood level (1-5): "))

    commute_times.append(commute_time)
    stress_levels.append(stress_level)
    mood_levels.append(mood_level)

print("\nWeekly Record")

for i in range(len(days)):
    print("\nDay:", days[i])
    print("Commute:", commute_times[i], "minutes")
    print("Stress:", stress_levels[i])
    print("Mood:", mood_levels[i])
