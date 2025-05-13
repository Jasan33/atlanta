from flask import Flask, render_template, jsonify
import random

app = Flask(
    __name__,
    template_folder="../Frontend/templates", # Folder direction to templates and static
    static_folder="../Frontend/static"
)

@app.route("/")
def home():
    words = select_words()  # Generates a list of words
    return render_template('index.html', words=words) #return page


@app.route("/random-word")
def random_word():
    word = random.choice(word_categories['word_list'])
    return jsonify({'word': word})


def select_words():
    # Select 45 words from category 'word_list'
    words = random.sample(word_categories['word_list'], 1)
    random.shuffle(words)  # Randome and Shuffled words are selected
    return words

# A list of 200 commonly used words
word_categories = {
    'word_list': [
        "Github", "developer", "phone", "electronic", "sky", "safe", "keyboard", "human", "New Delhi", "Oslo", "India", "Norway", 
        "Javascript", "Paris", "philippines", "Manila", "robot", "chat-gpt", "Brazil", "2fa", "billiard", "Danmark", "Russia", 
        "China", "Seoul", "Souht Korea", "North Korea", "white", "black", "Sykehusparter", "France", "Maiken", "Grefsenkållen", 
        "tennis", "sand", "diamond", "gold", "United States of America", "Black gorilla", "Ai", "zero", "rope", "sex", "pistol", 
        "solder", "fire", "water", "speak", "question", "task", "pilot", "girlfriend", "barcelona", "pasta", "pizza", "Burger Kind", 
        "Macdonalds", "Kebab", "some", "computer", "flag", "Mumbai", "Hong Kong", "Mexico", "Argentina", "fidget spinner", "bear", 
        "cat", "first", "dog", "Tiktok", "Instagram", "school", "Lunch", "Iceland", "over", "Basketball", "Friday", "Monday", "webnesday",
        "sunday", "saturday", "help", "skip", "many", "must", "look", "before", "great", "back", "through", "long", "where", "much", "should", "well", "people", "down", "own", "just",
        "because", "good", "each", "those", "feel", "seem", "how", "high", "too", "place", "little", "world", "very", "still", "nation",
        "hand", "old", "life", "tell", "write", "become", "here", "show", "house", "both", "between", "need", "mean", "call", "develop",
        "under", "last", "right", "move", "thing", "general", "school", "never", "same", "another", "begin", "while", "number", "part",
        "turn", "real", "leave", "might", "want", "point", "form", "off", "child", "few", "small", "since", "against", "ask", "late",
        "home", "interest", "large", "person", "end", "open", "public", "follow", "during", "present", "without", "again", "hold",
        "govern", "around", "possible", "head", "consider", "word", "program", "problem", "however", "lead", "system", "set", "order",
        "eye", "plan", "run", "keep", "face", "fact", "group", "play", "stand", "increase", "early", "course", "change", "help", "line"
    ]
}


if __name__ == '__main__':
    app.run(debug=True, port=7000)