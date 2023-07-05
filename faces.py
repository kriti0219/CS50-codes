#function called convert
def convert(sentence):
    emo1 = ":)"
    emo2 = ":("
    modified_sen = sentence.replace(emo1, "🙂").replace(emo2, "🙁")
   
    return modified_sen

#implement a function called main
def main():
    sentence = input("what do you wanna say?\n")
    modified_sen = convert(sentence)
    
    print(modified_sen)

#call main at the bottom of your file.
main()

