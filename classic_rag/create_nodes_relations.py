from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_ollama import ChatOllama
from chunk_pdf import create_chunks
from test_langchain_wrapper import neo4j_graph
from tqdm.auto import tqdm
#import pickle

#allowed_nodes = ["Class", "Method", "Framework", "Concept", "Package"]

#allowed_relationships = ["USES", "BELONGS_TO", "DEPENDS_ON", "MENTIONS", "PART_OF", ]

allowed_nodes = ["Character", "Location", "Event", "Object"]
allowed_relationships = [
    "KNOWS",
    "VISITS",
    "INVESTIGATES",
    "ASSOCIATED_WITH",
    "THREATENS"
]



llm = ChatOllama(
    model="gpt-oss:20b", 
    temperature=0
)

llm_transformer = LLMGraphTransformer(
    llm=llm,
    allowed_nodes=allowed_nodes,
    allowed_relationships=allowed_relationships,
    strict_mode=True
)

chunks = create_chunks("./the_gift")

print(">>>start creating nodes and relationships<<<")

graph_documents = []
for chunk in tqdm(chunks, desc="converting chunks to graph:"):

    if isinstance(chunk, tuple):
        doc_to_process = chunk[0]
    else:
        doc_to_process = [chunk]

    try:
        graph_doc = llm_transformer.convert_to_graph_documents(doc_to_process)
        graph_documents.extend(graph_doc)
        print(chunk.page_content)
    except Exception as ex:
        print(f"error processing : {ex}")

neo4j_graph().add_graph_documents(
    graph_documents,
    baseEntityLabel=True,
    include_source=True
)

print(">>>Graph Doc added to Neo4j<<<")

# Save the extracted data to your Mac
#with open("extracted_graph.pkl", "wb") as f:
#    pickle.dump(graph_documents, f)

#print("Data saved! You can now experiment with Neo4j without re-running the LLM.")
