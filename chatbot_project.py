# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 13:55:17 2023

@author: ATISHKUMAR
"""

from nltk.chat.util import Chat,reflections

#pairs is list of patterns and responsesfrom nltk.chat.util import Chat, reflections

#Pairs is a list of patterns and responses.

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Antaryami created me using Python's NLTK library ","Prakash ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Hyderabad, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["virat"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['Our customer service will reach out to you'] 
    ],
]


print(reflections)


my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
    }

#Now let’s print a default message, and finish our chatbot:

#default message at the start of chat
print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")

#Create Chat Bot
chat = Chat(pairs, reflections)


# Start conversation

chat.converse() 


pairs=[
     [
       r"(.*)my name is (.*)",
       ["hello %2,how are u today",]
       
      ],
      [ 
        r"(.*) help (.*)",
        ["i can help you"]
       
      ],
      [
        r"(.*) your name ?",
        ["my name is cleaverprogrammer, but u can call me a robot and i am a chatbot. ",]
        
      ],
      [
        r" how are you (.*) ?",
        ["I'am doing very well,i am great !"]
        
      ],
      [
        r"sorry (.*)",
        ["ïts alright","its ok, never mind that",]
        
      ],
      [
        r"i'm (.*) (good/well/okay/ok)",
        ["nice to hear that","Alright great !",]
        
      ],
      [
        r"(hi/hello/hey/hola/holla)(.*)",
        ["hello","hey there",]
        
      ],
      [
        r"what (.*) want ?",
        ["make me an offer I can't refuse",]
        
      ],
      [
        r"(.*)created(.*)",
        ["Antaryami created me using Python NLTK library","Atish ;",]
        
      ],
      [
        r"(.*) (location/city) ?",
        ["Hydrabad ,India",]
        
      ],
      [
        r"(.*) raining in (.*)",
        ["No rain in the past 4 days here in 2%","in 2% there is 50% chance of rain",]
        
      ],
      [
        r"how (.*) health (.*)",
        ["health is very important,but i am a computer , so I don't need to worry about my health",]
        
      ],
      [
        r"(.*)(sports/game/sport)(.*)",
        ["I'am big fan of cricket",]
        
      ],
      [
        r"who(.*) (cricketer/batsman)?",
        ["Virat"]
        
      ],
      [
        r"quit",
        ["by for now.see u soon :) ", "It was nice talking to you.see you soon :)"]
        
      ],
      [
       r"(.*)",
       ["our customer service will reach out to you"]
      ],
]

print(reflections)


my_dummy_reflections={
    "go" : "gone",
    "hello" : "hi there"}

#now lets print deafaluts message and finsish our chatbot

#default message at the start of the chat

print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")


#create chatbot

chat=Chat(pairs,reflections)

#start converse

chat.converse()      
