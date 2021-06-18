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

def concateStringsWithDelim(delimiter, lst):
    result = ""
    for i in range(len(lst)):
        result += lst[i]
        if i + 1 != len(lst):
            result += delimiter
    return result
    
    
def main():
    names = []
    print(len(os.listdir('.')))
    total = 0
    for i in range(74):  
        matchText = str(i).zfill(3)
        allWordsPattern = f'([WTAE]-)*({matchText})([abcde])* (.+)(\..+)'
        lessonsPattern = f'^({matchText} .+)(\.pdf|\.pptx)$' 
        
        print(matchText)
        names = []
        names = [f for f in os.listdir('.') if re.match(allWordsPattern, f)]
        
        lessonNames = []
        if (len(names)) != 0:
            lessonNames = [re.search(lessonsPattern, n).group(1) for n in names if re.match(lessonsPattern, n) and not checkForPresence(n.lower(), forbiddenWords)]
        
        total += len(names)
        folderName = ""
        print(names)
        if len(names) > 0:
            if lessonNames == []:
                os.system(f'mkdir "{names[0][2:-4]}"')
                print("Folder name:", names[0][2:-4])
                folderName = names[0][2:-4]
            else:
                result = concateStringsWithDelim(" + ", lessonNames) if (len(lessonNames) > 1) else lessonNames[0]
                os.system(f'mkdir "{result}"')
                print("Folder name:", result)
                folderName = result 
            print("|----------|")
            
        for file in names:
            os.system(f'move "./{file}" "./{folderName}/"')
        # str(i).zfill(3) filling code
        print("Done doing everything!\n\n")
    print(total)

if __name__ == "__main__":
    main()