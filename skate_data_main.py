#from os import name
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#--- LOAD DATAFRAME ---
df = pd.read_csv('skate_data.csv')
df.columns = df.columns.str.strip()

#--- BOOLEAN ---
save_files = False

#--- VARIABLES ---
name_list = df["Name"]

#--- FUNCTIONS ---
#--- MENU ---
def menu():
    index = 0

    for skater_name in name_list:
        skate_part = df.loc[index, 'Part Name']
        print(f"{index} - {skater_name} - '{skate_part}'")
        index += 1

    option = int(input("> "))
    if option == 111:
        save_visualize_files()
        print("Success!")
        exit()

    skater_details(option)
    visualize(option)

    goagain = input("\n Go again? (y/n): > ")
    if(goagain.startswith("y")):
        menu()
    else:
        exit()

#--- DATA OVERVIEW ---
def data_overview():
    print(df["Total Tricks"].mean())

#--- SHOW SKATER OVERVIEW --- 
def skater_details(option):

    details = {
        "Name" : df.loc[option, 'Name'],
        "Stance" : df.loc[option, 'Stance'],
        "Board Size" : df.loc[option, 'Board Size'],
        "Birth Year" : df.loc[option, 'Birth Year'],
        "Country" : df.loc[option, 'Country'],
        "Part Name" : df.loc[option, 'Part Name'],
    }

    for name, detail in details.items():
        print(f"{name}: {detail}")

#--- STANCE VISUALIZATION ---
def stance_vis(option, save_files):

    #--- SAVE FILE VARIABLES ---
    name = df.loc[option, 'Name']
    part = df.loc[option, 'Part Name']
    dir_path = f"images/{name}/{part}"
    file_path = f"{dir_path}/stance.jpg"

    #--- TOTAL TRICK COUNT ---
    total_tricks = df.loc[option, 'Total Tricks']

    #--- STANCE COUNT CALCULATION ---
    stance_count = {
        "regular_count" : df.loc[option, 'Regular'],
        "switch_count" : df.loc[option, 'Switch'],
        "nollie_count" : df.loc[option, 'Nollie'],
        "fakie_count" : df.loc[option, 'Fakie'],
    }

    #--- PIE CHART VISUALIZATION ---
    # Define data
    stances = ['Regular', 'Switch', 'Nollie', 'Fakie']
    counts = [stance_count['regular_count'], stance_count["switch_count"], stance_count['nollie_count'], stance_count['fakie_count']]
    colors = ['#8DB98B', '#D36D6A', '#E8B26D', '#7AAED6']

    # Create list of labels with stance name and count
    labels = [f"{stance} ({count})" for stance, count in zip(stances, counts)]

    # Create pie chart
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.pie(counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)

    plt.title('Stance Distribution')
    plt.text(0.5, 0.98, f'{df.loc[option, "Name"]} - "{df.loc[option, "Part Name"]}"', fontsize=8, ha='center', va='bottom', transform=ax.transAxes)
    plt.text(0.5, 0.96, f'Total Tricks: {total_tricks}', fontsize=8, ha='center', va='bottom', transform=ax.transAxes)

    if not save_files:
        plt.show()
    else:
        os.makedirs(dir_path, exist_ok=True)
        plt.savefig(file_path, bbox_inches='tight', pad_inches=0.1)

#--- TERRAIN VISUALIZATION ---
def obstacle_vis(option, save_files):
    
    #--- SAVE FILE VARIABLES ---
    name = df.loc[option, 'Name']
    part = df.loc[option, 'Part Name']
    dir_path = f"images/{name}/{part}"
    file_path = f"{dir_path}/obstacle.jpg"

    #--- TOTAL TRICKS COUNT ---
    total_tricks = df.loc[option, 'Total Tricks']

    terrain_count = {
        "Rail" : df.loc[option, 'Rail'],
        "Hubba" : df.loc[option, 'Hubba'],
        "Ledge" : df.loc[option, 'Ledge'],
        "Flatground" : df.loc[option, 'Flatground'],
        "Gap or Stairs" : df.loc[option, 'Gap or Stairs'],
        "Transition" : df.loc[option, 'Transition'],
        "Manual" : df.loc[option, 'Manual']
    }

    #--- PIE CHART VISUALIZATION ---
    # Define data
    obstacles = ['Rail', 'Hubba', 'Ledge', 'Flatground', 'Gap or Stairs', 'Transition', 'Manual']

    # Filter data
    filtered_obstacles = [obstacle for obstacle in obstacles if terrain_count[obstacle] > 0]
    counts = [terrain_count[obstacle] for obstacle in filtered_obstacles]

    # Adjusted colors for muted effect
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#9370DB', '#87CEEB']

    labels = [f"{obstacle} ({count})" for obstacle, count in zip(filtered_obstacles, counts)]

    # Create pie chart
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.pie(counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)

    # Add information labels for total tricks count and total flip tricks count under the title
    plt.title('Obstacle Distribution')
    plt.text(0.5, 0.98, f'{df.loc[option, "Name"]} - "{df.loc[option, "Part Name"]}"', fontsize=8, ha='center', va='bottom', transform=ax.transAxes)
    plt.text(0.5, 0.96, f'Total Tricks: {total_tricks}', fontsize=8, ha='center', va='bottom', transform=ax.transAxes)

    if not save_files:
        plt.show()
    else:
        os.makedirs(dir_path, exist_ok=True)
        plt.savefig(file_path, bbox_inches='tight', pad_inches=0.1)

#--- THE NUMBERS BAR GRAPH ---
def the_numbers(option, save_files):
    # Extract the attributes and their corresponding values for Wes Kremer (row 0)
    skater_data = df.iloc[option]

    #--- SAVE FILE VARIABLES ---
    name = df.loc[option, 'Name']
    part = df.loc[option, 'Part Name']
    dir_path = f"images/{name}/{part}"
    file_path = f"{dir_path}/numbers.jpg"

    # Remove unwanted columns
    skater_data = skater_data.drop(['Name', 'Stance', 'Country', 'Part Name', 'Year Filmed', 'Length (s)', 'Board Size', 'Birth Year'])

    # Convert the values to numeric (in case they are not already)
    skater_data = pd.to_numeric(skater_data, errors='coerce')

    # Remove any NaN values (if any)
    skater_data = skater_data.dropna()

    # Define muted colors for each attribute
    colors = [(0.7, 0.7, 0.2, 0.5)] * len(skater_data)  # Yellow as the default muted color
    colors[skater_data.index.get_loc('Regular')] = (0.2, 0.2, 0.7, 0.5)  # Blue
    colors[skater_data.index.get_loc('Fakie')] = (0.2, 0.2, 0.7, 0.5)  # Blue
    colors[skater_data.index.get_loc('Nollie')] = (0.2, 0.2, 0.7, 0.5)  # Blue
    colors[skater_data.index.get_loc('Switch')] = (0.2, 0.2, 0.7, 0.5)  # Blue
    colors[skater_data.index.get_loc('Total Tricks')] = (0.2, 0.7, 0.2, 0.5)  # Green
    colors[skater_data.index.get_loc('Flips')] = (0.5, 0.2, 0.5, 0.5) # Purple
    colors[skater_data.index.get_loc('Spins')] = (0.5, 0.2, 0.5, 0.5) # Purple
    colors[skater_data.index.get_loc('180')] = (0.5, 0.2, 0.5, 0.5) # Purple
    colors[skater_data.index.get_loc('360')] = (0.5, 0.2, 0.5, 0.5) # Purple

    # Create horizontal bar chart
    plt.figure(figsize=(10, 6))
    skater_data.plot(kind='barh', color=colors)
    plt.xlabel('Number of Tricks')
    plt.title(f'Tricks Distribution by {df.loc[option, "Name"]} in "{df.loc[option, "Part Name"]}"')

    plt.gca().invert_yaxis()  # Invert y-axis to have the highest count at the top
    plt.xticks(np.arange(0, max(skater_data) + 1, 5))  # Adjust the step value as needed
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    if not save_files:
        plt.show()
    else:
        os.makedirs(dir_path, exist_ok=True)
        plt.savefig(file_path, bbox_inches='tight', pad_inches=0.1)

def save_visualize_files():
    save_file_index = 0
    save_files = True

    for skater_name in name_list:
        stance_vis(save_file_index, save_files)
        obstacle_vis(save_file_index, save_files)
        the_numbers(save_file_index, save_files)
        save_file_index += 1

#--- ALL ---
def visualize(option):
        stance_vis(option)
        obstacle_vis(option)
        the_numbers(option)

if __name__ == '__main__':
    menu()