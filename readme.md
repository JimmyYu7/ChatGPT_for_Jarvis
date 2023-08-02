# Voice Assistant with OpenAI GPT-3

This project is a voice assistant powered by OpenAI's GPT-3 model. The assistant listens to the user's input, processes the speech to text, sends the text to the GPT-3 model, and then speaks the generated text back to the user.

## Features
- Speech to text conversion using the `speech_recognition` library
- Text to speech conversion using the `pyttsx3` library
- Conversation management with the OpenAI GPT-3 model
- Ability to interrupt the response after a specific duration

## Dependencies

The following Python libraries are required to run this voice assistant:

- openai
- pyttsx3
- speech_recognition
- playsound

To install these dependencies, you can use pip:
```shell
pip install -r requirements.txt
```

## Usage

To start the voice assistant, simply run the script with Python:
```shell
python main.py
```

The assistant will greet you with a welcome message. You can then start speaking to the assistant. If the assistant does not understand you, it will tell you so. You can terminate the conversation by saying "thank you for your help".

Please note that you need to replace `"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"` with your actual OpenAI API key.

## Future Enhancements

Future enhancements could include improving speech recognition accuracy, adding more conversational features, or integrating with other services.


