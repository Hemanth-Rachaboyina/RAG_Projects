
import sys
import os

# # Get the parent directory of the current file
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(parent_dir)



# # from llama_index.llms.groq import Groq
# from Declarations.models import cerebras_client

# # llm = Groq(model="llama3-70b-8192", api_key="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")

# response = groq_llm.complete("who are you ?")



# print(response)
from dotenv import load_dotenv
load_dotenv()

import os
from cerebras.cloud.sdk import Cerebras

cerebras_client = Cerebras(
    # This is the default and can be omitted
    api_key="csk-m56hk4xvmc4jdmv4ejetn6ehn4x5femvfcnyfw4y6py2w4h8"
)



stream = cerebras_client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Explain about the history of the world in 100 words."
        }
    ],
    model="llama-4-scout-17b-16e-instruct",
    stream=True,
    max_completion_tokens=2048,
    temperature=0.2,
    top_p=1
)

print(stream)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="")
