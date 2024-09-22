import emoji


asdf = input((emoji.emojize("Input: ")))
asdf = emoji.emojize(asdf, language='alias')
print("Output:",asdf)
