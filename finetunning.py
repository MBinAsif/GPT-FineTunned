import torch
import os

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import streamlit as st

# Update with your local file paths
model_directory = 'C:/Users/pc/Desktop/Semester 7/NLP/Project/MyModels'

# Load the fine-tuned GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained(model_directory)
tokenizer = GPT2Tokenizer.from_pretrained(model_directory)

st.title('Banking Chatbot with GPT-2')

st.sidebar.title('Options')
option = st.sidebar.selectbox('Choose an action', ('Chat', 'Settings'))

if option == 'Chat':
    st.markdown('### Chat with the Bot')
    user_input = st.text_input('You:', '')

    if st.button('Send'):
        input_text = user_input.strip()

        # Tokenize user input
        input_ids = tokenizer.encode(input_text, return_tensors='pt')

        # Generate bot response
        bot_response_ids = model.generate(
            input_ids.to(torch.device("cpu")),  # Set device to CPU or GPU as appropriate
            max_length=100,
            num_return_sequences=1,
            temperature=0.9,
            no_repeat_ngram_size=2,
            pad_token_id=tokenizer.eos_token_id
        )

        # Decode and display bot response
        bot_response = tokenizer.decode(bot_response_ids[0], skip_special_tokens=True)
        st.text_area('Bot:', value=bot_response, height=100)
elif option == 'Settings':
    st.markdown('### Settings')
    st.write("You can configure settings here.")

# Run the Streamlit app in your local IDE
if __name__ == "__main__":
    st.write("Make with ❤️ by [Muhammad & Danyaal](https://github.com/MBinAsif/GPT-FineTunned/blob/main/fine_tunning_gpt2.py)")
