emoji = input('Please type here -->')
if ":)" and ":(" in emoji:
    msg = (emoji.replace(':)',"🙂"))
    new_msg = (msg.replace(':(',"🙁"))
    print(new_msg)
elif ":)" in emoji:
    print(emoji.replace(':)',"🙂"))
elif ":(" in emoji:
    print(emoji.replace(':(',"🙁"))
