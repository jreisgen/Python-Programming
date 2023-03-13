
while True:
    editor = input("Editor: ")
    lowereditor = editor.lower()
    if lowereditor == "visual studio code":
        print("an excellent choice!")
        break
    elif lowereditor == "word" or lowereditor == "notepad":
        print("awful")
    else:
        print("not good")
