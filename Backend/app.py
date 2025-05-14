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
        "Github", "developer", "Phone", "Electronic", "Sky", "Safe", "Keyboard", "Human", "New Delhi", "Oslo", "India", "Norway", 
        "Javascript", "Paris", "philippines", "Manila", "robot", "chat-gpt", "Brazil", "2fa", "billiard", "Danmark", "Russia", 
        "China", "Seoul", "Souht Korea", "North Korea", "white", "black", "Sykehusparter", "France", "Maiken", "Grefsenkållen", 
        "Tennis", "Sand", "Diamond", "Gold", "USA", "Black gorilla", "Ai", "Zero", "Rope", "Sex", "Pistol", 
        "Solder", "Fire", "Water", "Speak", "Question", "Task", "Pilot", "Girlfriend", "Barcelona", "Pasta", "Pizza", "Burger King", 
        "Macdonalds", "Kebab", "Some", "Computer", "Flag", "Mumbai", "Hong Kong", "Mexico", "Argentina", "Fidget spinner", "Bear", 
        "Cat", "First", "Dog", "Tiktok", "Instagram", "School", "Lunch", "Iceland", "Joy Kill", "Basketball", "Friday", "Monday", "wednesday",
        "Sunday", "Saturday", "Help", "Skip", "Marry", "Church", "Look", "Before", "Spotify", "Laptop", "Fish", "Anal sex", "Whatsapp", 
        "Teams", "Italiy", "Nose", "Eyes", "Legs", "Bathroom", "Note", "Evidence", "Book", "Google", "Image", "Slave", "Afrika", "Point", 
        "High", "Alcohol", "Skin", "Phone", "Wires", "Mom", "Dad", "Database", "Bowling", "Cold", "Freeze", "Flashlight", "Ghost", "Fishing",
        "Demon", "Rope", "House", "Thunder", "Toilet", "Mirror", "lazy", "Scam call", "Headsett", "Python", "Burger", "Smile", "Chair", 
        "Geogusser", "Camera", "Dubai", "Torono", "Epost", "Highway", "Key", "Car", "Jam", "Tigretten", "Police", "Bank", "Radius", "Battery",
        "GPU", "CPU", "RAM", "Enter", "Child", "Ocen", "OperaGX", "Bag", "BankID", "Vipps", "Moan", "Pen", "Papper", "Exam", "Cheating", "Rust", 
        "Fingers", "Public", "Sink", "Football", "Chrome", "Poop", "Timer", "Presentation", "Video", "Pick", "Cock", "Head", "Airdrop", "Hotdog", 
        "City", "Tbane", "Songsvann", "Kid", "Documention", "Table", "Bed", "Bottle", "Plan", "Run", "Jogging", "Gorilla", "Monkey", "Group", "UK",
        "Explotion", "Word", "early", "Airpods", "Norwegian", "Photo", "Line"
    ]
}


if __name__ == '__main__':
    app.run(debug=True, port=7000)