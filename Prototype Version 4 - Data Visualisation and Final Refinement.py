import csv  # For saving and reading data in a CSV file
import os   # For finding and using the correct file path
import matplotlib.pyplot as plt  # For creating graphs

# Display the program title and instructions for the user
print("Mood and Stress Tracker")
print("Please enter your commute, stress and mood information for Monday to Friday.")
print("stress level: 1 = very low, 5 = very high")
print("mood level: 1 = very bad, 5 = very good")

# File used to save the data
folder = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(folder, "mood_stress_data.csv")

while True:
    
    # Ask the user which week they are recording
    while True:
        try:
            week = int(input("\nEnter week number (for example,1):"))

            if week >= 1:
                break
            else:
                print("Please enter a week number of 1 or higher.")

        except ValueError:
            print("Please enter a whole week number.")

    # Store the weekdays that will be used in the tracker
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Create empty lists to store the user's weekly data
    commute_times = []
    stress_levels = []
    mood_levels = []

    # Ask the user to enter data for each weekday
    for day in days:
        print("\nEnter data for", day)

        # Record the daily commute time in minutes
        while True:
            try:
                commute_time = int(input("Enter commute time in minutes: "))

                if commute_time >= 0:
                    break
                else:
                    print("Please enter a commute time of 0 or more.")

            except ValueError:
                print("Please enter a whole number.")

        # Record stress level and make sure it is between 1 and 5
        while True:
            try:
                stress_level = int(input("Enter stress level (1-5): "))

                if 1 <= stress_level <= 5:
                    break
                else:
                    print("Please enter a stress level between 1 and 5.")

            except ValueError:
                print("Please enter a whole number.")

        # Record mood level and make sure it is between 1 and 5
        while True:
            try:
                mood_level = int(input("Enter mood level (1-5): "))

                if 1 <= mood_level <= 5:
                    break
                else:
                    print("Please enter a mood level between 1 and 5.")

            except ValueError:
                print("Please enter a whole number.")

        # Add each day's data to the correct list
        commute_times.append(commute_time)
        stress_levels.append(stress_level)
        mood_levels.append(mood_level)
    
    # Display all recorded data for the week
    print("\nWeek" + str(week) + " Record")

    for i in range(len(days)):
        print("\nDay:", days[i])
        print("Commute:", commute_times[i], "minutes")
        print("Stress:", stress_levels[i])
        print("Mood:", mood_levels[i])

    # Function to calculate the average value of a list
    def calculate_average(data):
        return sum(data) / len(data)

    # Calculate weekly average commute, stress, and mood values
    average_commute = calculate_average(commute_times)
    average_stress = calculate_average(stress_levels)
    average_mood = calculate_average(mood_levels)

    # Find highest stress, lowest mood and longest commute
    highest_stress = max(stress_levels)
    lowest_mood = min(mood_levels)
    longest_commute = max(commute_times)

    highest_stress_days = [days[i] for i in range(len(days)) if stress_levels[i] == highest_stress]
    lowest_mood_days = [days[i] for i in range(len(days)) if mood_levels[i] == lowest_mood]
    longest_commute_days = [days[i] for i in range(len(days)) if commute_times[i] == longest_commute]

    # Display a summary of the weekly results
    print("\nWeekly Summary")
    print("Average commute time:", round(average_commute,1), "minutes")
    print("Average stress level:", round(average_stress,1))
    print("Average mood level:", round(average_mood,1))
    print("Longest commute:", longest_commute, "minutes on", ", ".join(longest_commute_days))
    print("Highest stress level:", highest_stress, "on", ", ".join(highest_stress_days))
    print("Lowest mood level:", lowest_mood, "on", ", ".join(lowest_mood_days))

    # Check if the CSV file already exists
    file_exists = os.path.exists(file_name)

    # Save the weekly data to an external CSV file
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)

        # Write the header row if the file does not already exist
        if not file_exists:
            writer.writerow(["Week", "Day", "Commute Time (minutes)", "Stress Level", "Mood Level"])

        # Write the data for each day of the week
        for i in range(len(days)):
            writer.writerow([week, days[i], commute_times[i], stress_levels[i], mood_levels[i]])
    
    print("\nYour weekly data has been saved to", file_name)

    # Load and display previously saved data
    print("\nSaved Records")

    with open(file_name, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

    #Create line charts for weekly stress and mood levels
    plt.plot(days, stress_levels, marker='o', label="Stress")
    plt.plot(days, mood_levels, marker='o', label="Mood")

    plt.title("Weekly Stress and Mood")
    plt.xlabel("Days")
    plt.ylabel("Levels")
    plt.ylim(1, 5)
    plt.yticks([1, 2, 3, 4, 5])

    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

    # Ask the user if they want to record another week
    another_week = input("\nDo you want to enter another week? (yes/no):")

    if another_week.lower() != "yes":
        break

print("Program finished. Thank you for using the Mood and Stress Tracker!")