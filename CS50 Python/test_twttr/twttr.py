def main():
    tweet = str(input("Input: "))
    new_tweet = shorten(tweet)
    print("Output: " + new_tweet)

def shorten(word):
    vowel = ['a', 'e', 'i', 'o', 'u']
    new_tweet = ""
   # tweet = str(input('Input: '))
    for char in word:
        if not char.lower() in vowel:
            new_tweet += (char)
    return new_tweet


if __name__ == "__main__":
    main()