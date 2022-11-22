import pyperclip
import random, time

toAdd = [
    "😘",
    "♥️",
    "❣️",
    "❤️",
    "🤍",
    "🤎",
    "🥰",
    "🏩",
    "💓",
    "💖",
    "💕",
    "💝",
    "💗",
    "💞",
    "💘",
    "💟",
    "💌",
    "🧡",
    "💛",
    "💚",
    "💙",
    "💜",
    "🤎",
    "🖤",
    "🤍",
    "😘",
    "😗",
    "😙",
    "♥️",
    "☺️",
    "😚",
    "😊",
    "🤗",
    "🤩",
    " i love you ",
    " you're so kind ",
    " awwwwwwwwwwww ",
    " thanks!!!!!!! ",
    " <3 ",
    " love u :))) ",
    " YAY ",
    " YAYYYYY ",
    " awwww ",
    " you're so sweeeeeet ",
    " best gf ever!!!! ",
    " yayyayyaya lovvvvvvvv lov "
]

while True:
    text = ""
    while (len(text) < 400):
        text += toAdd[random.randint(0, len(toAdd) - 1)]

    pyperclip.copy(text)

    # wait for 5 seconds and generate a new one
    time.sleep(5)
    print("generating new one")
