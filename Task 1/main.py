import tkinter as tk
from equation import generate_equation, solve_equation

# Global variables
user_score = 0
question_number = 1
max_question_number = 5
max_number_range = 10


def submit_answer():
    """Display whether the user is correct or incorrect and then move to the next question or end the game"""
    global question_number, user_score
    checked_answer = check_answer()
    if checked_answer == True:
        feedback_label.config(text="Correct!", foreground='green')
        user_score += 1
    elif checked_answer == False:
        feedback_label.config(text="Incorrect! Answer is " +
                              str(answer), foreground='red')
    # Check whether to continue asking questions or end the game
    if checked_answer == True or checked_answer == False:
        if question_number < max_question_number:
            question_number += 1
            # Delay asking the next question by 1.5 seconds so that answer feedback can be read
            frame.after(1500, ask_question)
        else:
            # Delay ending the game by 1.5 seconds so that answer feedback can be read
            frame.after(1500, end_game)

def check_answer():
    """Check whether the user's entered answer equals the correct answer."""
    try:
        user_answer = entry_box.get()
        # Check if the user's answer is a fraction
        if '/' in user_answer:
            # Convert fraction to float rounded to 2 decimal places
            user_answer = round(eval(user_answer), 2)
        if float(user_answer) == answer:
            return True
        else:
            return False
    except (ValueError, ZeroDivisionError) as error:
        submit_button.config(text="Invalid Input", fg="red")
        frame.after(1500, lambda: submit_button.config(
            text="Save", fg="black"))
        # Clear entry box
        entry_box.delete(0, tk.END)

def ask_question():
    """Clear and then create the widgets for the question screen."""
    global answer, feedback_label, submit_button, entry_box
    clear_frame()
    # Get random equation
    equation, equation_arr = generate_equation(max_number_range)
    # Get answer to the equation
    answer = solve_equation(equation_arr)
    # Create the widgets for the question answering screen
    tk.Label(frame, text="Question "+str(question_number) +
             " - Solver for x (2 decimal places):\n"+equation).pack()
    feedback_label = tk.Label(frame, width=40)
    entry_box = tk.Entry(frame, width=27)
    submit_button = tk.Button(frame, text='Submit',
                              width=25, command=submit_answer)
    # Add the widgets to the frame
    feedback_label.pack()
    entry_box.pack()
    submit_button.pack()

def settings():
    """Clear, resize the window and then create the widgets for the settings screen."""
    global save_button, max_questions_entry, max_values_entry, settings_description_label
    clear_frame()
    window.geometry("400x225")
    tk.Label(frame, text="Settings").pack()
    settings_description_label = tk.Label(frame, text=f"Number of questions: {
                                          max_question_number}\nValues range: (1-{max_number_range})")
    settings_description_label.pack()
    max_questions_label = tk.Label(
        frame, text="Number of questions: ", width=25)
    max_questions_entry = tk.Entry(frame, width=27)
    max_values_label = tk.Label(frame, text="Max value: ", width=25)
    max_values_entry = tk.Entry(frame, width=27)
    max_questions_label.pack()
    max_questions_entry.pack()
    max_values_label.pack()
    max_values_entry.pack()
    save_button = tk.Button(
        frame, text="Save", width=25, command=save_settings)
    save_button.pack()
    tk.Button(frame, text="Return", width=25, command=main_menu).pack()

def save_settings():
    """
    Saves user entered settings whilst checking for any invalid inputs.

    It allows for the user to save one entry box if the other is empty and both at the same time.
    """
    global max_question_number, max_number_range
    try:
        max_question_number_temp = None
        max_number_range_temp = None
        # If entries are not blank, assign them to temporary values
        if not max_questions_entry.get() == "":
            max_question_number_temp = int(max_questions_entry.get())
        if not max_values_entry.get() == "":
            max_number_range_temp = int(max_values_entry.get())
        # Raise an error if for either field a number has been entered and it is below 1, or if both fields are empty
        if (not max_question_number_temp == None and max_question_number_temp < 1) or (not max_number_range_temp == None and max_number_range_temp < 1) or (max_question_number_temp == None and max_number_range_temp == None):
            raise ValueError
        # For each entry field, if the entry is not blank, assign the temporary variable to the actual variable
        if not max_question_number_temp == None:
            max_question_number = max_question_number_temp
        if not max_number_range_temp == None:
            max_number_range = max_number_range_temp
        settings_description_label.config(text=f"Number of questions: {
                                          max_question_number}\nValues range: (1-{max_number_range})")
        # Change the 'Save' button's text to 'Saved!' and green
        save_button.config(text="Saved!", fg="green")
        # Change the 'Save' button's format back after 1.5 seconds
        frame.after(1500, lambda: save_button.config(text="Save", fg="black"))
    except ValueError:
        # Change the 'Save' button's text to 'Invalid Input' and red
        save_button.config(text="Invalid Input/s", fg="red")
        # Change the 'Save' button back after 1.5 seconds
        frame.after(1500, lambda: save_button.config(text="Save", fg="black"))

def end_game():
    """Clear and then create the widgets for the end of game screen."""
    clear_frame()
    tk.Label(frame, text=f"End of Game, Score: {user_score}").pack()
    tk.Button(frame, text="Play Again", width=15, command=start_game).pack()
    tk.Button(frame, text="Exit", width=15, command=exit_window).pack()

def exit_window():
    """Close the GUI."""
    window.destroy()

def start_game():
    """Set the variables so when 'Play Again' is selected, the variables are reset before starting the game."""
    global question_number, user_score
    question_number = 1
    user_score = 0
    main_menu()

def main_menu():
    """Clear, resize the window and then create the widgets for the main menu screen."""
    clear_frame()
    window.geometry("400x135")
    tk.Label(frame, text="Welcome to the Equation Solver, Press Start to Begin").pack()
    tk.Label(
        frame, text="Note: You may enter your answer as a fraction (a/b)", fg="grey").pack()
    tk.Button(frame, text='Start', width=25, command=ask_question).pack()
    tk.Button(frame, text='Settings', width=25, command=settings).pack()
    tk.Button(frame, text="Exit", width=25, command=exit_window).pack()

def clear_frame():
    """Iterate through all widgets in the frame and remove them."""
    for widget in frame.winfo_children():
        widget.destroy()

# Initialize the window
window = tk.Tk()
window.title("Solve Equations")
window.geometry("400x135")

# Create a frame to hold all widgets
frame = tk.Frame(window)
frame.pack(fill="both", expand=True)
start_game()
window.mainloop()
