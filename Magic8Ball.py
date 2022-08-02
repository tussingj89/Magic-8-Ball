import streamlit as st
from random import *

answers = [ 'it is definitely possible.',
            'ask me again in 5 years.',
            'you\'ve got to be kidding.',
            'well of course, silly person.',
            'are you serious?',
            'well i should hope so!',
            'not on your life.',
            ' of course not, no.',
            'no sane person would ask me that.',
            'could be.',
            'no shit Sherlock.',
            'what are you, stupid?'  ]

def on_ask():
    n = randint(0, len(answers) - 1)
   
st.title("Magic 8 Ball")
text = st.text_input("Enter your question if you dare.")

if st.button("ask"):
    n = randint(0, len(answers)-1)
    st.write(answers[n])
