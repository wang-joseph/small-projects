# this is the same as my juypter notebook, but in a .py file because I want to hide outputs

file_to_open = "nov-2023-hours.txt"

tasks_and_times = {}
with open(f"./hours/{file_to_open}") as f:
    for line in f:
        line = line.replace('"', '')
        task, time = line.split(":")
        tasks_and_times[task] = time.strip()

tasks_and_times


import pandas as pd
import numpy as np

# Function to convert time strings to minutes
def time_to_minutes(time_str):
    hours = 0
    minutes = 0
    if 'h' in time_str:
        hours, time_str = time_str.split('h')
        hours = int(hours)
    if 'm' in time_str:
        minutes = int(time_str.replace('m', ''))
    return 60 * hours + minutes

# Function to round time to the nearest quarter hour
def round_to_nearest_quarter(minutes):
    return int(np.round(minutes / 15.0) * 15)

# Create DataFrame
df = pd.DataFrame(list(tasks_and_times.items()), columns=['Task', 'Time'])

# Convert time to minutes and round to nearest quarter hour
df['Minutes'] = df['Time'].apply(time_to_minutes)
df['Rounded Time'] = df['Minutes'].apply(round_to_nearest_quarter)

# Convert rounded time back to hours and minutes format
df['Rounded Time'] = df['Rounded Time'].apply(lambda x: f"{x // 60}h{x % 60}m")

# Calculate total time
total_minutes = df['Minutes'].sum()
total_hours = total_minutes // 60
remaining_minutes = total_minutes % 60

# Calculate total rounded time
total_rounded_minutes = df['Rounded Time'].apply(time_to_minutes).sum()
total_rounded_hours = total_rounded_minutes // 60
remaining_rounded_minutes = total_rounded_minutes % 60

# adding one more row for total
df.loc[len(df.index)] = ['Total', f"{total_hours}h{remaining_minutes}m", total_minutes, f"{total_rounded_hours}h{remaining_rounded_minutes}m"]

# Display the DataFrame as a styled HTML table
df_style = df.style.set_properties(**{'text-align': 'left'}).set_table_styles(
    [dict(selector='th', props=[('text-align', 'left')])]
)

df_style


# using df_style's total row, calculate the amount earned by doing time * hourly rate
hourly_rate = 30
amount = total_minutes * hourly_rate / 60

print(f"Minutes worked: {total_minutes} with a rate of ${hourly_rate}/hr")
print(f"Total amount earned: ${amount}")
