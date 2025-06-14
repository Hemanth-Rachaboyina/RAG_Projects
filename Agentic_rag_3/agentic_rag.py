from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex



documents = SimpleDirectoryReader("./data").load_data()
vector_index = VectorStoreIndex.from_documents(documents)
vector_index.as_query_engine()

query_engine = vector_index.as_query_engine()
response = query_engine.query("What is this about?")
print(response)