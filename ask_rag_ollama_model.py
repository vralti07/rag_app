from search_chroma import similarity_search
from langchain_ollama import OllamaLLM

#your query or question 
query = 'get me all zelle transaction made by Sohini Koripelly'

#top k results
k = 10 

#context, meaning model should below given context to answer, 
#not go beyond the scope of context and hulluciante
context = similarity_search(query, k) 

ollama_model_name = "gpt-oss:20b"

def set_ollama_model(model_name :str) -> OllamaLLM:
    ollama = OllamaLLM(model=model_name)
    return ollama

llm = set_ollama_model(ollama_model_name)

prompt = f"""
You are a helpful assistant.
Answer the question using only the provided context.
If the answer is not in the context, say:
"I don't know based on the provided context."

Context:
{context}

Question:
{query}

Answer:
"""

response = llm.invoke(prompt)
print(response)



