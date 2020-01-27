def LetterChanges(str):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW"
    changes = "bcdEfghIjklmnOpqrstUvwxyzABCDEFGHIJKLMNOPQRSTUVWZ"
    mapping = { k:v for (k,v) in zip(str+letters,str+changes) }
    return "".join([ mapping[c] for c in str ])
    
# keep this function call here  
print LetterChanges(input())