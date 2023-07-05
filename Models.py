import signature
import openai
import secret

openai.api_key = secret.api_key


class Model():
    def __init__(self):
        self.messages = []
        self.functions = [
            signature.get_current_weather,
        ]
        
    def add_functions(self,function):
        self.functions.append(function)
        
    def add_messages(self,content):
        self.messages.append(content)
        
    def run_conversation(self):
        # Step 1: send the conversation and available functions to GPT
        ##messages = [{"role": "user", "content": content}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=self.messages,
            functions=self.functions,
            function_call="auto",  # auto is default, but we'll be explicit
        )
        response_message = response["choices"][0]["message"]
        self.add_messages(response_message)
        return response_message