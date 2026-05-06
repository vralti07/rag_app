import os
from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph, GraphCypherQAChain
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate


load_dotenv()

NEO4J_URI=os.getenv("NEO4J_URI")
NEO4J_USERNAME=os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD=os.getenv("NEO4J_PASSWORD")

def neo4j_graph():
    graph = Neo4jGraph(
        url=NEO4J_URI,
        username=NEO4J_USERNAME,
        password=NEO4J_PASSWORD
    )
    return graph

neo4j_graph().refresh_schema()

CYPHER_GENERATION_TEMPLATE = """Task: Generate a Cypher statement to query a Neo4j graph.
Nodes: Character, Location, Event, Object (also labeled as __Entity__)
Schema:
{schema}

Instructions:
1. Use 'toLower(n.id) CONTAINS toLower("{question}")' for the search.
2. Do NOT restrict the search to just one label. Use (n:__Entity__) to search everything.
3. Return the node and its immediate neighbors.

Example Cypher:
MATCH (n:__Entity__) WHERE toLower(n.id) CONTAINS toLower("{question}") 
OPTIONAL MATCH (n)-[r]-(m) 
RETURN n, r, m

Question: {question}
Cypher Query:"""

CYPHER_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], 
    template=CYPHER_GENERATION_TEMPLATE
)



chain = GraphCypherQAChain.from_llm(
    OllamaLLM(model="llama3.1:8b"),
    graph=neo4j_graph(),
    verbose=True,
    cypher_prompt=CYPHER_PROMPT,
    allow_dangerous_requests=True
)
# CORRECT (using a colon creates a dictionary)
response = chain.invoke({"query": "Baskerville Hall"})
print(response["result"])
