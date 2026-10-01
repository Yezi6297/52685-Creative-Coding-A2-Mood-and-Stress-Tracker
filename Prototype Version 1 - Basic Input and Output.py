print("Mood and Stress Tracker")
print("Please enter your daily commute, stress and mood information.")

day = input("Enter the day: ")
commute_time = int(input("Enter today's commute time in minutes: "))
stress_level = int(input("Enter stress level (1-5): "))
mood_level = int(input("Enter mood level (1-5): "))

print("\nDaily Record")
print("Day:", day)
print("Commute:", commute_time, "minutes")
print("Stress:", stress_level)
print("Mood:", mood_level)