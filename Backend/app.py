from flask import Flask, render_template, request, redirect, session, url_for, flash
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


def select_words():
    # Select 45 words from category 'word_list'
    words = random.sample(word_categories['word_list'], 1)
    random.shuffle(words)  # Randome and Shuffled words are selected
    return words

# A list of 200 commonly used words
word_categories = {
    'word_list': [
        "the", "develop", "of", "and", "a", "to", "in", "he", "have", "it", "that", "for", "they", "much", "with", "as", "not", "on", "she",
        "at", "by", "this", "we", "you", "do", "but", "from", "or", "which", "one", "would", "all", "will", "there", "say", "who",
        "make", "when", "can", "more", "if", "no", "man", "out", "other", "so", "what", "time", "up", "go", "about", "than", "into",
        "could", "state", "only", "new", "year", "some", "take", "come", "these", "know", "see", "use", "get", "like", "then", "first",
        "any", "work", "now", "may", "such", "give", "over", "think", "most", "even", "find", "day", "also", "after", "way", "many",
        "must", "look", "before", "great", "back", "through", "long", "where", "much", "should", "well", "people", "down", "own", "just",
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