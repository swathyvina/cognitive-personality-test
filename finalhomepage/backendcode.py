# Display the introduction
def display_intro():
    clear_output()
    display(HTML("<h2>Welcome to the Self-Assessment Questionnaire</h2>"))
    display(HTML("<p>This test is designed to help you evaluate your skills and attributes in three key areas: Empathy, Adaptability, and Communication. You will go through each section separately and receive a detailed result based on your responses.</p>"))

    # Dropdown to select the section
    section_selector = widgets.Dropdown(
        options=["Empathy", "Adaptability", "Communication"],
        description="Select Section:",
        style={'description_width': 'initial'}
    )

    start_button = widgets.Button(description="Start Section")
    start_button.on_click(lambda b: display_section(section_selector.value, questions[section_selector.value], handle_section_callback))

    display(section_selector, start_button)

# Display a section and collect responses
def display_section(category, questions_list, next_button_callback):
    clear_output()
    display(HTML(f"<h2>{category} Assessment</h2>"))
    widgets_list = create_widgets(questions_list)
    for widget in widgets_list:
        display(widget)
    next_button = widgets.Button(description="Submit Section")
    next_button.on_click(lambda b: next_button_callback(category, widgets_list))
    display(next_button)

# Collect the results from each section
scores = {"Empathy": 0, "Adaptability": 0, "Communication": 0}

# Callback function for handling section submission
def handle_section_callback(category, widgets_list):
    scores[category] = sum(widget.value for widget in widgets_list)

    # Check if there are any sections left to complete
    remaining_sections = [sec for sec in questions if scores[sec] == 0]
    if remaining_sections:
        display_section_selector(remaining_sections)
    else:
        display_final_results()

# Display the section selector again if there are more sections to complete
def display_section_selector(remaining_sections):
    clear_output()
    section_selector = widgets.Dropdown(
        options=remaining_sections,
        description="Select Section:",
        style={'description_width': 'initial'}
    )

    next_button = widgets.Button(description="Next Section")
    next_button.on_click(lambda b: display_section(section_selector.value, questions[section_selector.value], handle_section_callback))

    display(section_selector, next_button)

# Display the final results
def display_final_results():
    clear_output()

    def provide_narrative(score, category):
        if category == "Empathy":
            if 21 <= score <= 25:
                return "High Empathy: You are highly empathetic, understanding, and supportive. You are very aware of others' emotions and needs and respond with care and compassion."
            elif 16 <= score <= 20:
                return "Moderate Empathy: You have a good level of empathy. You generally understand and care about others' feelings but may occasionally miss subtle cues."
            elif 11 <= score <= 15:
                return "Average Empathy: Your empathy is average. You show concern for others but might not always fully understand their emotions or respond appropriately."
            elif 6 <= score <= 10:
                return "Low Empathy: You might struggle to understand and relate to others' feelings. You may need to work on being more attentive and responsive to the emotions of those around you."
            else:
                return "Very Low Empathy: You have significant difficulty in understanding and relating to others' emotions. Developing greater emotional awareness and sensitivity could benefit your relationships."

        elif category == "Adaptability":
            if 21 <= score <= 25:
                return "Highly Adaptable: You excel in adapting to new situations and changes. You are flexible, resilient, and thrive in dynamic environments."
            elif 16 <= score <= 20:
                return "Moderately Adaptable: You are fairly adaptable and can handle changes well, though there may be times when you find adjustments challenging."
            elif 11 <= score <= 15:
                return "Average Adaptability: Your adaptability is average. You manage changes adequately but may feel uncomfortable with significant or sudden shifts."
            elif 6 <= score <= 10:
                return "Low Adaptability: You might find it challenging to adapt to new situations and changes. Working on being more open to new experiences could help improve your adaptability."
            else:
                return "Very Low Adaptability: You struggle significantly with adapting to change. Developing greater flexibility and resilience can help you navigate changes more effectively."

        elif category == "Communication":
            if 21 <= score <= 25:
                return "Excellent Communication: You have excellent communication skills. You express yourself clearly, listen well, and effectively resolve conflicts."
            elif 16 <= score <= 20:
                return "Good Communication: Your communication skills are strong. You generally convey your thoughts well and are good at interacting with others."
            elif 11 <= score <= 15:
                return "Average Communication: Your communication skills are average. You manage basic communication well but might need to improve in areas like feedback and conflict resolution."
            elif 6 <= score <= 10:
                return "Poor Communication: You may find it difficult to communicate effectively. Working on clarity, listening, and adaptability in your communication style could benefit you."
            else:
                return "Very Poor Communication: You have significant difficulties with communication. Improving your skills in expressing thoughts, listening, and adapting your style to different audiences is essential."

    results = []
    for category, score in scores.items():
        narrative = provide_narrative(score, category)
        results.append(f"{category} Score: {score} - {narrative}")

    # Calculate the overall score and type of person
    total_score = sum(scores.values())
    if total_score >= 63:
        personality_type = "You are a well-rounded, highly empathetic, adaptable, and communicative individual."
    elif total_score >= 48:
        personality_type = "You have strong attributes but with some areas for improvement."
    elif total_score >= 33:
        personality_type = "You are moderately developed across these areas but may need to work on certain aspects."
    elif total_score >= 18:
        personality_type = "You may find challenges in these areas and would benefit from significant development."
    else:
        personality_type = "You face considerable difficulties in these areas and should focus on improvement."

    final_result = f"Overall Assessment: {personality_type}"

    # Display the results
    display(HTML("<h2>Assessment Results</h2>"))
    display(HTML("<br>".join(results)))
    display(HTML(f"<h3>{final_result}</h3>"))

# Start by displaying the introduction
display_intro()