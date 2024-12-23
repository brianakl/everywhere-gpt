Have access to chatgpt everywhere you can type!


### Requirements
- Python >= 10
- OpenAI
- Pynput


### Instructions
Ensure the above packages are installed

```
pip install openai pynput
```

Have your openai python api linked to your oepnai api key. Do this by opening pyton in your terminal and setting it up as below

```
? python
> import openai
> openai.api_key = "YOUR_API_KEY"
> exit()
```

Now you can run the program

```
python kb.py
```

Keep this terminal open since it is the one running the program


### Default keys

<F9> is the default toggle key to start recording, when it is pressed again, it will send out an api call to open ai with all the text typed since the last <F9> button press. There is a limit to the length of the query you can send which is set in kb.py:14 as MAX_QUERY_LEN to 1000 characters. Additionally the max_tokens parameter MAX_TOKENS is set to 800 line right above it.
