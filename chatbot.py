

import nltk
from nltk.chat.util import Chat, reflections

"""**Create a Dataset**"""

dialogs = [
    [
        r"hi|hello|hey|howdy|yo",
        ["Hello!", "Hi there!", "Hey!", "Howdy!", "Yo! How can I assist you today?"]
    ],
    [
        r"what is your name|who are you?",
        ["I'm a chatbot.", "I'm just a chatbot created in Python.", "Call me ChatGPT."]
    ],
    [
        r"how are you|how's it going|what's up?",
        ["I'm just a computer program, so I don't have feelings, but I'm here to help you!", "I'm good, thanks for asking!", "Not much, just here to assist you."]
    ],
    [
        r"bye|goodbye|see you|adios|farewell",
        ["Goodbye!", "See you later!", "Adios!", "Farewell!", "Have a great day!"]
    ],
    [
        r"what can you do|what are your abilities|how can you help",
        ["I can answer questions, provide information, and have conversations with you.", "I can help you with various tasks, just ask!"]
    ],
    [
        r"tell me a joke|say something funny",
        ["Why don't scientists trust atoms? Because they make up everything!", "I used to play piano by ear, but now I use my hands."]
    ],
    [
        r"how old are you|when were you created",
        ["I don't have an age, but I was created by Vignesh G.", "I'm a relatively new creation, born in the realm of algorithms."]
    ],
    [
        r"thanks|thank you",
        ["You're welcome!", "No problem, happy to help!", "Anytime!"]
    ],
    [
        r"how do I contact support|need help|I have a problem",
        ["For support, please visit our website or contact our customer support at vickystft@gmail.com."]
    ],
    [
        r"tell me a fun fact|give me an interesting fact",
        ["Honey never spoils. Archaeologists have even found pots of honey in ancient Egyptian tombs that are over 3,000 years old!", "A group of flamingos is called a 'flamboyance'."]
    ],
    [
        r"who is your creator|who made you",
        ["I was created by a team of engineers and developers at Vignesh G.", "My creators are a talented group of individuals at Vignesh."]
    ],
    [
        r"what's your favorite color|favorite color",
        ["I don't have a favorite color since I'm just a chatbot, but I can help you find information about colors!"]
    ],
    [
        r"tell me a quote|give me an inspiring quote",
        ["The only way to do great work is to love what you do. - Steve Jobs", "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"]
    ],
    [
        r"who won the last Super Bowl|Super Bowl winner",
        ["I'm not sure about the most recent Super Bowl winner. You can check the latest sports news for that information."]
    ],
    [
        r"tell me a riddle|give me a riddle",
        ["I'm as light as a feather, yet the strongest person can't hold me for much longer than a minute. What am I? (A breath)", "I am taken from a mine and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I? (A pencil lead)"]
    ],
    [
        r"what's the weather like today|current weather",
        ["I don't have real-time data, but you can check your local weather forecast on weather websites or apps like Weather.com or AccuWeather."]
    ],
     [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "How can I help you today?"]
    ],
    [
        r"what is your name|who are you?",
        ["I'm a chatbot.", "I'm just a chatbot created in Python."]
    ],
    [
        r"how are you|how's it going?",
        ["I'm just a computer program, so I don't have feelings, but I'm here to help you!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "See you later!", "Have a great day!"]
    ],
    [
        r"hi|hello|hey",
        [
            "Hello!",
            "Hi there!",
            "Hey!",
            "Greetings!",
            "Hi, how can I assist you?",
        ]
    ],
    [
        r"what is your name|who are you?",
        [
            "I'm a chatbot.",
            "I'm just a chatbot created in Python.",
            "You can call me ChatGPT.",
        ]
    ],
    [
        r"how are you|how's it going?",
        [
            "I'm just a computer program, so I don't have feelings, but I'm here to help you!",
            "I'm doing well in terms of processing data!",
            "I'm functioning as expected.",
        ]
    ],
    [
        r"bye|goodbye",
        [
            "Goodbye!",
            "See you later!",
            "Farewell!",
            "Have a great day!",
        ]
    ],
    [
        r"(.*) your name(.*)",
        [
            "My name is ChatGPT.",
            "I go by the name ChatGPT.",
        ]
    ],
    [
        r"(.*) help (.*)",
        [
            "Sure! How can I help you?",
            "What do you need assistance with?",
            "I'm here to help. What do you need?",
        ]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        [
            "I'm sorry, I don't have real-time information. You can check a weather website or app for that.",
            "I don't have the ability to provide current weather information. Please use a weather service.",
        ]
    ],
    [
        r"(.*) age (.*)",
        [
            "I don't have an age. I'm just a program.",
            "Age doesn't apply to me. I'm a computer program.",
        ]
    ],
    [
        r"(.*) (love|like) (.*)",
        [
            "I'm not capable of experiencing emotions, but I'm here to help you.",
            "I don't have feelings, but I'm here to assist you.",
        ]
    ],
    [
        r"(.*) (created|made) (.*)",
        [
            "I was created by OpenAI using Python.",
            "I'm a product of OpenAI's GPT-3.5 architecture.",
            "OpenAI is responsible for my creation.",
        ]
    ],
    [
        r"(.*) (thanks|thank you) (.*)",
        [
            "You're welcome!",
            "You're very welcome!",
            "No problem! If you have more questions, feel free to ask.",
        ]
    ],
    [
        r"(.*)",
        [
            "I'm not sure I understand. Can you please rephrase?",
            "Could you provide more context?",
            "I'm sorry, I'm not sure how to respond to that.",
        ]
    ],
    [
        r"what is your name|who are you?",
        ["I'm a chatbot.", "I'm just a chatbot created in Python."]
    ],
    [
        r"how are you|how's it going?",
        ["I'm just a computer program, so I don't have feelings, but I'm here to help you!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "See you later!", "Have a great day!"]
    ],
    [
        r"help|what can you do?",
        ["I can answer questions, provide information, and have general conversations with you."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"how old are you?",
        ["I don't have an age. I'm just a computer program."]
    ],
    [
        r"what is your favorite color?",
        ["I don't have preferences for colors. I'm here to assist you."]
    ],
    [
        r"who created you|who is your developer?",
        ["I was created by a developer using Python and NLTK."]
    ],
    [
        r"thanks|thank you",
        ["You're welcome!", "No problem!"]
    ],
    [
        r"what is the meaning of life?",
        ["The meaning of life is a philosophical question. Different people have different answers."]
    ],
    [
        r"how do I contact support?",
        ["You can contact support by visiting our website or emailing support@company.com."]
    ],
    [
        r"tell me about yourself",
        ["I'm just a chatbot designed to answer your questions and have conversations."]
    ],
    [
        r"what is the weather like today?",
        ["I'm sorry, I don't have access to real-time weather information. You can check a weather website or app for that."]
    ],
    [
        r"tell me a fun fact",
        ["Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"]
    ],
    [
        r"what's the time?",
        ["I don't have access to real-time information like the current time."]
    ],
    [
        r"who won the last Super Bowl?",
        ["I'm not up-to-date with sports results. You can search online for the latest Super Bowl winner."]
    ],
    [
        r"what's your favorite book?",
        ["I don't have preferences for books. What's your favorite book?"]
    ],
    [
        r"tell me a riddle",
        ["I'm terrible at solving riddles, but here's one for you: I'm tall when I'm young and short when I'm old. What am I?"]
    ],
]

"""**Create a ChatBot**"""

chatbot = Chat(dialogs, reflections)

"""**Define a Function for Interaction**"""

def chat_with_bot():
    print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

"""**Start the Conversation**"""

if __name__ == "__main__":
    chat_with_bot()
