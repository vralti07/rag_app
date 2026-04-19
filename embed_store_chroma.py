from chunk_pdf import create_chunks
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

pdf_path = "./wellsFargoStatments"
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
model_kwargs = {"device": "cpu"}


def use_model_embed(embedding_model_name :str) -> HuggingFaceEmbeddings:

    print(">>> creating model embedding object <<<")
    print(f"model name {embedding_model_name}.")
    print(f"model device ::: {model_kwargs}.")

    embedding = HuggingFaceEmbeddings(
        model_name=embedding_model_name,
        model_kwargs=model_kwargs,
    )

    print(">>> created embedding model <<<")
    return embedding



persist_directory = "./wellsFargo"

if __name__ == "__main__":
    page_content_list = []
    metadata_list = []
    docs = create_chunks(pdf_path)
    if(len(docs) <= 0):
        print('docs are null or empty')
        raise SystemExit(1)
    
    for doc in docs:
        metadata = doc.metadata
        metadata_list.append(metadata)

        page_content = doc.page_content
        page_content_list.append(page_content)
    
    print(f"building texts and metadatas: {len(page_content_list)} items")

    print(">>> creating Chroma vector store <<<")
    vector_store = Chroma.from_texts(
        texts=page_content_list, 
        metadatas=metadata_list, 
        embedding=use_model_embed(embedding_model_name), 
        persist_directory=persist_directory
    )
    print(">>> done: stored embeddings in Chroma at", persist_directory)
