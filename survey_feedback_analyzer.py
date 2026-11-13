"""
Module End Assignment 4: Survey Feedback Analyzer
"""

# ---------------------------------------------------------------
# Step 1: Preloaded feedbacks (given data)
# ---------------------------------------------------------------
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# ---------------------------------------------------------------
# Step 2: Add more feedbacks
# ---------------------------------------------------------------
def add_feedbacks():
    n = int(input("How many more feedbacks do you want to add? "))

    for _ in range(n):
        name = input("\nEnter name: ")
        text = input("Enter feedback: ")

        # Keep asking until the rating is a valid number between 1 and 5
        while True:
            rating = int(input("Enter rating (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Invalid rating. Please enter a number between 1 and 5.")

        # S_No continues automatically from the last entry (11 onward)
        feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)
        feedback_data['Name'].append(name)
        feedback_data['Feedback'].append(text)
        feedback_data['Rating'].append(rating)


# ---------------------------------------------------------------
# Step 3: Text cleaning
# ---------------------------------------------------------------
def clean_text(text):
    # Remove punctuation (. , ! ?)
    for ch in ['.', ',', '!', '?']:
        text = text.replace(ch, '')

    # split() with no argument removes leading/trailing spaces and
    # collapses multiple spaces; ' '.join() puts words back with one space
    text = ' '.join(text.split())

    # Convert to lowercase
    return text.lower()


def clean_all_feedbacks():
    cleaned = []
    for text in feedback_data['Feedback']:
        cleaned.append(clean_text(text))
    feedback_data['Feedback'] = cleaned


# ---------------------------------------------------------------
# Step 4: Word count insights
# ---------------------------------------------------------------
def count_word_in_feedbacks(word):
    """Return the number of feedbacks that contain the given word (case-insensitive)."""
    word = word.lower()
    count = 0
    for text in feedback_data['Feedback']:
        if word in text.lower().split():
            count += 1
    return count


# ---------------------------------------------------------------
# Main program
# ---------------------------------------------------------------
add_feedbacks()
clean_all_feedbacks()

print("\n=== Word Count Insights ===")
for w in ['good', 'poor', 'excellent']:
    print(f'Number of feedbacks containing "{w}": {count_word_in_feedbacks(w)}')

# ---------------------------------------------------------------
# Step 5: Final summary & insights
# ---------------------------------------------------------------
print("\n=== Final Cleaned Feedback Data ===")
print(feedback_data)

# Average rating
average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print(f"\nAverage rating: {average_rating:.2f}")

# Feedback with the longest comment (by word count)
longest_index = 0
max_words = 0
for i in range(len(feedback_data['Feedback'])):
    word_count = len(feedback_data['Feedback'][i].split())
    if word_count > max_words:
        max_words = word_count
        longest_index = i

print("\nLongest feedback:")
print(f"  S_No    : {feedback_data['S_No'][longest_index]}")
print(f"  Name    : {feedback_data['Name'][longest_index]}")
print(f"  Feedback: {feedback_data['Feedback'][longest_index]}")
print(f"  Rating  : {feedback_data['Rating'][longest_index]}")
print(f"  Words   : {max_words}")

# Unique words used across all feedbacks
unique_words = []
for text in feedback_data['Feedback']:
    for word in text.split():
        if word not in unique_words:
            unique_words.append(word)

print("\nUnique words used across all feedbacks:")
print(sorted(unique_words))

# ---------------------------------------------------------------
# Optional: Sort feedbacks by rating (highest to lowest)
# ---------------------------------------------------------------
print("\n=== Feedbacks Sorted by Rating (Highest to Lowest) ===")
combined = zip(feedback_data['Rating'], feedback_data['S_No'],
               feedback_data['Name'], feedback_data['Feedback'])
sorted_feedbacks = sorted(combined, key=lambda item: item[0], reverse=True)

for rating, s_no, name, text in sorted_feedbacks:
    print(f"Rating: {rating} | S_No: {s_no} | Name: {name} | Feedback: {text}")
