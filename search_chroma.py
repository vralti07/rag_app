from embed_store_chroma import use_model_embed
from langchain_chroma import Chroma
from embed_store_chroma import embedding_model_name

persist_dir = './chroma_db_java_notes'

def vector_data_search_config() -> Chroma:
    vector_data_search = Chroma(
        persist_directory=persist_dir, 
        embedding_function=use_model_embed(embedding_model_name)
    )
    return vector_data_search


query = 'explain recursion'

def similarity_search(query :str, k :int) -> str:
    print('collect data from similarity search')
    context_data = []
    context_string = ''
    
    try:
        query_results = vector_data_search_config().similarity_search(query, k=k)
        print(f">>> search completed <<< ")
    except Exception as e:
        print(f"exception {e}")
    

    print("create context string")
    for result in query_results:
        context_data.append(result.page_content)
    
    context_string = "\n---\n".join(context_data)
    print('context string for LLM created')
    return context_string
    