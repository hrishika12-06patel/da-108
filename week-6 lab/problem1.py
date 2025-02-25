import random

# Dictionary mapping words to emojis
word_to_emoji = {
    "hello": "👋",
    "hi": "👋",
    "how": "❓",
    "you": "👉",
    "doing": "🔧",
    "happy": "😊",
    "sad": "😢",
    "excited": "😃",
    "birthday": "🎂",
    "love": "❤️",
    "good": "👍",
    "morning": "🌞",
    "night": "🌜",
    "coffee": "☕",
    "dog": "🐶",
    "cat": "🐱",
    "yes": "✅",
    "no": "❌",
    "party": "🎉",
    "congratulations": "🎊",
    # Add more words and their corresponding emojis here
}

# Dictionary mapping moods to a list of relevant emojis
mood_to_emojis = {
    "happy": ["😃", "🎉", "🥳", "😊", "🌞"],
    "sad": ["😢", "😭", "😞", "☔", "🌧️"],
    "excited": ["🤩", "😆", "🎊", "🎉", "🏆"],
    "angry": ["😡", "😠", "👿", "💢", "🔥"],
    "love": ["❤️", "😍", "😘", "💕", "💖"],
    # Add more moods and their corresponding emojis here
}

def translate_to_emojis(sentence):
    
    words = sentence.split()  # Split the sentence into words
    translated_sentence = []
    
    for word in words:
        emoji = word_to_emoji.get(word.lower(), word)  # Get the emoji for the word if it exists
        translated_sentence.append(emoji)
    
    return ' '.join(translated_sentence)  # Join the words back into a sentence

def mood_fill(sentence, mood):
    
    if mood in mood_to_emojis:
        emojis = mood_to_emojis[mood]
        random_emojis = random.sample(emojis, min(3, len(emojis)))  # Pick up to 3 random emojis
        return f"{sentence} {' '.join(random_emojis)}"
    else:
        return sentence

def main():
    
    while True:
        user_input = input("Enter a sentence (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break
        
        if "(fill with" in user_input and ")" in user_input:
            # Extract mood from the user's input
            mood_start = user_input.find("(fill with") + len("(fill with ")
            mood_end = user_input.find(")")
            mood = user_input[mood_start:mood_end].strip()
            base_sentence = user_input[:user_input.find("(fill with")].strip()
            translated_sentence = translate_to_emojis(base_sentence)  # Translate the base sentence to emojis
            final_sentence = mood_fill(translated_sentence, mood)  # Append mood-based emojis
        else:
            final_sentence = translate_to_emojis(user_input)  # Translate the input to emojis
        
        print("Translated Sentence: ", final_sentence)

if __name__ == "__main__":
    main()

