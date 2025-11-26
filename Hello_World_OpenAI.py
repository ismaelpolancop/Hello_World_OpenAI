from openai import OpenAI
import os

client = OpenAI(api_key="API KEY")
if client.api_key is None:
    print("Error: OpenAI API Key not found. Please set a API KEY")
else:
    try:
        promt_text = "Say hello world from OPENAI"

        response = client.responses.create(
            model= "gpt-4o",
            input = promt_text,
            stream=False,
        )
        llm_response = response.output_text
        print("LLM response: ", llm_response)
    except Exception as e:
        print("Error: An erro has occured:", str(e))