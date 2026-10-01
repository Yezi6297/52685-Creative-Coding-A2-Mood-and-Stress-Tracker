# Import libraries for file storage
import csv
import os

print("Mood and Stress Tracker")
print("This program records commute time, stress and mood from Monday to Friday.")
print("Stress level: 1= very low, 5= very high")
print("Mood level: 1= very bad, 5= very good")

#File used to save the data
folder = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(folder, "mood_stress_data.csv")

# Ask the  user which week they are recording
week = input("\nEnter week number (for example, 1): ")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

commute_times = []
stress_levels = []
mood_levels = []

# Collect data for each weekday
for day in days:
    print("\nEnter data for", day)
    commute_time = int(input("Enter commute time in minutes: "))
    stress_level = int(input("Enter stress level (1-5): "))
    mood_level = int(input("Enter mood level (1-5): "))

    commute_times.append(commute_time)
    stress_levels.append(stress_level)
    mood_levels.append(mood_level)

# Display the current weekly record
print("\nWeekly Record")

for i in range(len(days)):
    print("\nDay:", days[i])
    print("Commute:", commute_times[i], "minutes")
    print("Stress:", stress_levels[i])
    print("Mood:", mood_levels[i])

# Function to calculate averages
def calculate_average(data):
    return sum(data) / len(data)

average_commute = calculate_average(commute_times)
average_stress = calculate_average(stress_levels)
average_mood = calculate_average(mood_levels)

highest_stress = max(stress_levels)
highest_stress_index = stress_levels.index(highest_stress)

lowest_mood = min(mood_levels)
lowest_mood_index = mood_levels.index(lowest_mood)

# Weekly summary
print("\nWeekly Summary")
print("Average commute time:", round(average_commute,1), "minutes")
print("Average stress level:", round(average_stress,1))
print("Average mood level:", round(average_mood,1))
print("Highest stress level was on", days[highest_stress_index])
print("Lowest mood level was on", days[lowest_mood_index])

# Check if the CSV file already exists
file_exists = os.path.exists(file_name)

# Save the new weekly data to an external CSV file
with open(file_name,'a', newline='') as file:
    writer = csv.writer(file)
    
    # Add headings only when the file is created for the first time
    if not file_exists:
        writer.writerow(["Week", "Day", "Commute Time", "Stress Level", "Mood Level"])
    
    for i in range(len(days)):
        writer.writerow([week, days[i], commute_times[i], stress_levels[i], mood_levels[i]])
print("\nYour weekly data has been saved to", file_name)

# Load previous data from the CSV file
print("\nSaved Records")

with open(file_name, 'r') as file:
    reader = csv.reader(file)
   
    for row in reader:
        print(row)