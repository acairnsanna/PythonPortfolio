def emoji_converter(message):
    message = input(">")
    words = message.split(' ')
    emojis = {
        ':)': '😁',
        ':(': '☹️'
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
emoji_converter(message)
print(emoji_converter(message))