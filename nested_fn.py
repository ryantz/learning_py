def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word) # using the nested function

talk('I am going to buy the milk')