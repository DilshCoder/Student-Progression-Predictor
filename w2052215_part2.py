# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# https://www.pythontutorial.net/python-basics/
# Student ID: 20232125 / w2052215
# Date: 11/12/2023

#import the graphics module
from graphics import *

# range of values for credits
number_range = [0, 20, 40, 60, 80, 100, 120]

#create dictionary to keep outcomes count
outcomes_count = {"Progress": 0, "Trailer": 0, "Retriever": 0, "Exclude": 0}

#list to store progression data
progression_data = []

#check and process result function
def results_check(outcomes_count):
    while True:
        try:
             #prompt to enter another set of data or quit
            view_results_choice = input("""\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:""").lower()
        except ValueError:
            print("\nPlease enter y or q!\n")

        if view_results_choice == "y":
            #if enter "y",call to the validation function
            validation(outcomes_count)

        elif view_results_choice == "q":
            #if enter "q",quit and display the bar chart and break the loop
            bar_chart(outcomes_count)
            print_progression_data()
            break

        else:
            print("Invalid input")
            
# Function to validate user inputs
def validation(outcomes_count):
    while True:
        try:
            # Prompt the user to enter credits at pass 
            credit_pass = int(input("Enter your credit at pass:"))
        except ValueError:  # only for integers
            print("Integer required\n")
        else:
            if credit_pass not in number_range:
                print("Out of range\n")
            else:
                break
    while True:
        try:
            # Prompt the user to enter credits at defer
            credit_defer = int(input("Enter your credit at defer:"))
        except ValueError:
            print("Integer required\n")
        else:
            if credit_defer not in number_range:
                print("Out of range\n")
            else:
                break
    while True:
        try:
            # Prompt the user to enter credits at fail
            credit_fail = int(input("Enter your credit at fail:"))
        except ValueError:
            print("Integer required\n")
        else:
            if credit_fail not in number_range:
                print("Out of range\n")
            else:
                break

    total_credit = credit_pass + credit_defer + credit_fail

    if total_credit != 120:
        # If the total credits are incorrect,call to validation function
        print("Total incorrect")
        validation(outcomes_count)
    elif credit_pass == 120:
         #If all the credits are pass,get as "progress",update the outcomes_count
        print("progress")
        outcomes_count["Progress"] += 1
        #append data b to a list
        progression_data.append([credit_pass, credit_defer, credit_fail, "Progress"])
        #call results_check function,add another set of values or quit
        results_check(outcomes_count)
    elif credit_pass == 100 and (credit_defer == 20 or credit_fail == 20):
        #get as "progress(module trailer)",update the outcomes_count
        print("progress(module trailer)")
        outcomes_count["Trailer"] += 1
        progression_data.append([credit_pass, credit_defer, credit_fail, "Progress (module trailer)"])
        results_check(outcomes_count)
    elif credit_fail >= 80:
        #get as "Exclude",update the outcomes_count
        print("Exclude")
        outcomes_count["Exclude"] += 1
        progression_data.append([credit_pass, credit_defer, credit_fail, "Exclude"])
        results_check(outcomes_count)
    else:
        #if any condition don't support to this,get as "Do not progress-module retriever",update the outcomes_count
        print("Do not progress-module retriever")
        outcomes_count["Retriever"] += 1
        progression_data.append([credit_pass, credit_defer, credit_fail, "Module retriever"])
        results_check(outcomes_count)

        
#function to create a bar chart
def bar_chart(outcomes_count):
    # Create a graphics window for the bar chart 
    win = GraphWin("Histogram", 550, 350)
    win.setBackground("white")
    bar_width = 80
    bar_gap = 10
    x = 50

    #colors for the Bars
    colors = {
        "Progress": color_rgb(174, 248, 161),      # Dark green
        "Trailer": color_rgb(160, 198, 137),       # Medium green
        "Retriever": color_rgb(167, 188, 119),     # Light green
        "Exclude": color_rgb(210, 182, 181)        # Light red
    }

    # Title of the chart
    title = Text(Point(win.getWidth() / 2, 20), "Histogram Results")
    title.setSize(14)
    title.draw(win)
    title.setTextColor("black")

    for outcome, count in outcomes_count.items():
         # Calculate the height of the bar based on the count
        bar_height = count * 20
        color = colors.get(outcome)
        # Draw the bar and set color 
        Rectangle(Point(x, 250), Point(x + bar_width, 250 - bar_height)).draw(win).setFill(color)
        Text(Point(x + bar_width / 2, 270), f"{outcome}: {count}").draw(win)
        # Display the outcome
        text_center = Point(x + bar_width/2,(250 - bar_height)-20)
        Text(text_center,count).draw(win)
        
        # Display count at the top of each bar
        count_text = Text(Point(text_center.getX(), text_center.getY()), str(count))
        count_text.setSize(12)
        count_text.setTextColor("black")
        count_text.draw(win)
        
        x += bar_width + bar_gap
        
    #Display the Total outcomes at the bottom # Total outcomes
    total_outcomes = sum(outcomes_count.values())
    Text(Point(win.getWidth() / 5, 295), f"Total Outcomes: {total_outcomes}").draw(win)
    # Wait for a mouse click to close the window 
    win.getMouse()
    win.close()
    
    
# Function to print progression data  
def print_progression_data():
    print("Part 2:")
    for data in progression_data:
        print(f"{data[3]} - {data[0]}, {data[1]}, {data[2]}")
    
# Call the validation function to start the program
validation(outcomes_count)


