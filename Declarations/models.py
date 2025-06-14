from llama_index.llms.groq import Groq
from cerebras.cloud.sdk import Cerebras

groq_llm = Groq(model="llama3-70b-8192", api_key="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")

cerebras_client = Cerebras(
    # This is the default and can be omitted
    api_key="csk-m56hk4xvmc4jdmv4ejetn6ehn4x5femvfcnyfw4y6py2w4h8"
)