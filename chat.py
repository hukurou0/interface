import json
from Models import Model
from utils import get_function

MAX_ACCESS = 10
content = input("入力：") # "What's the weather like in Boston?"

model = Model()
model.add_messages(
    {"role": "user", "content": content}
)
response_message = model.run_conversation()

count = 0
while True:
    if count > MAX_ACCESS:
        print("API呼び出し回数が上限を突破しました")
        break
    if response_message.get("function_call"):
        function_to_call = get_function(response_message) # 有効なfunctionが返ってきているかのチェックも行う
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = function_to_call(function_args)

        # Step 4: send the info on the function call and function response to GPT
        # extend conversation with assistant's reply
        model.add_messages(
            {
                "role": "function",
                "name": response_message["function_call"]["name"],
                "content": function_response,
            }
        )  # extend conversation with function response
        response_message = model.run_conversation()
        print(response_message)
        break
    else:
        print(response_message)
        content = input("入力：")
        model.add_messages(
        {"role": "user", "content": content}
        )
        response_message = model.run_conversation()
        count += 1