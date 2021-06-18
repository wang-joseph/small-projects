import os, re

forbiddenWords = [
    "worksheet",
    "exercises",
    "exercise",
    "nicholas",
    "practice"
]

lessonExtensions = [
    ".pdf",
    ".pptx",
    
]

def checkForPresence(word, forbiddenWords):
    for w in forbiddenWords:
        if w in word:
            return True
    
    return False
    
def main():
    names = []
    os.system(f'mkdir "Possibly Completed Work"')
    for i in range(74):  
        matchText = str(i).zfill(3)
        
        print(matchText)
        names = []
        names = [f for f in os.listdir('.') if re.match(f'W-({matchText})([ab])* (.+)(\..+)', f)]

        print(names)
        
        for file in names:
            os.system(f'move "./{file}" "./Possibly Completed Work/"')
        # str(i).zfill(3) filling code
        print("Done doing everything!\n\n")

if __name__ == "__main__":
    main()