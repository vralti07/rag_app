import os
from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph

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

#print(neo4j_graph.query("RETURN 'ok' AS msg"))