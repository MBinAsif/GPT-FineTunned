# Banking Chatbot with GPT-2

This repository contains code for a banking chatbot powered by the GPT-2 language model. The chatbot allows users to interact with a pre-trained GPT-2 model fine-tuned on banking-related conversations.

## Overview

This project uses Streamlit, a Python library for building interactive web applications, to create a user interface for chatting with the GPT-2-powered banking chatbot.

The chatbot model was fine-tuned on a banking dataset using Hugging Face's Transformers library.

## Usage

### Running the Chatbot

To run the chatbot, follow these steps:

1. Open the provided Colab Notebook: [Banking Chatbot Colab Notebook](https://colab.research.google.com/drive/1HUSJ59yNOkLwGLpYR21K6QLUV3ucmC3P).
2. Run the notebook cells to fine-tune the GPT-2 model on your dataset and save the model in Google Drive.
3. Once the model is saved, copy the model to your local environment or another Colab notebook.
4. Create a `requirements.txt` file containing the necessary dependencies:

    ```
    streamlit
    datasets
    transformers
    torch
    ```

5. Install the required packages using:

    ```
    pip install -r requirements.txt
    ```

6. Run the Streamlit app:

    ```
    streamlit run app.py
    ```

### Chatbot Interface

The chatbot interface provides two main functionalities:

- **Chat**: Interact with the chatbot by typing messages and receiving responses.
- **Settings**: Configure settings for the chatbot.

## Directory Structure

- `app.py`: Python script for the Streamlit application.
- `model/`: Directory containing the fine-tuned GPT-2 model and tokenizer.
- `data/`: Placeholder for any additional datasets used for fine-tuning (if applicable).
- `requirements.txt`: File listing all required Python packages for running the application.

## Colab Notebook

The [Banking Chatbot Colab Notebook]([https://colab.research.google.com/drive/1HUSJ59yNOkLwGLpYR21K6QLUV3ucmC3P](https://colab.research.google.com/drive/1HUSJ59yNOkLwGLpYR21K6QLUV3ucmC3P)) includes step-by-step instructions for fine-tuning the GPT-2 model and saving it in Google Drive.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Hugging Face Transformers](https://github.com/huggingface/transformers)
- [Streamlit](https://github.com/streamlit/streamlit)
- [Google Colaboratory](https://colab.research.google.com/)

## Future Work

In future iterations of this project, we aim to implement automatic answering of pre-trained questions from a bank integrated with Whatsapp. Some of the planned steps include:

- Integrating the GPT-2 model with a system capable of receiving and processing Whatsapp messages.
- Building a mechanism to detect and answer pre-trained questions related to banking automatically.
- Enhancing the chatbot's functionality to provide more comprehensive and accurate responses to banking queries.
