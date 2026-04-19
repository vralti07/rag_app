from langchain_text_splitters import RecursiveCharacterTextSplitter
from read_pdf import pdf_loader
from langchain_core.documents import Document

chunk_size = 1000
chunk_overlap = 200 
separators=["\n\n","\n"," ",""]

#pdf_path = "./wellsFargoStatments/012524WellsFargo.pdf"
pdf_path =  "./wellsFargoStatments/javanotes5.pdf"


def long_overlap(prev :str, curr :str) -> int:
    max_len = min(len(prev), len(curr))
    for i in range(max_len,0,-1):
          if(prev[-i:] == curr[:i]):
               return i
    return 0

          
def create_chunks(pdf_path :str) -> list[Document]:
    print(f">>> load start for : {pdf_path} <<<")
    docs = pdf_loader(pdf_path)
    print(f"loaded {len(docs)} pages")
    print(">>> load complete <<<")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=separators
    )


    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} chunks and chunk processing completed")
    return chunks

'''def create_chunks(pdf_path :str) -> list[Document]:
    print(f">>> load start for : {pdf_path} <<<")
    docs = pdf_loader(pdf_path)
    print(f"loaded {len(docs)} pages")
    print(">>> load complete <<<")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=separators
    )


    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} chunks")
    return chunks
    total_pairs = 0
    overlapping_pairs = 0

    printed_examples = 0
    max_examples = 5
    
    for i in range(1, len(chunks)):
            total_pairs += 1
            current = chunks[i].page_content
            previous = chunks[i - 1].page_content
            ov_len = long_overlap(previous, current)



            if ov_len > 0:
                overlapping_pairs += 1

            if printed_examples < max_examples:
                print("\n====================================")
                print(f"Pair index: ({i-1}, {i})")
                print(f"Overlap length: {ov_len}")
                # Show the overlapping text itself
                overlap_text = previous[-ov_len:]
                print(f"Overlap text:\n{overlap_text}")
                print("Prev tail (200 chars):")
                print(previous[-200:])
                print("Curr head (200 chars):")
                print(current[:200])
                printed_examples += 1

    print("\n===== OVERLAP SUMMARY =====")
    print(f"Total chunk pairs checked: {total_pairs}")
    print(f"Pairs with any overlap:    {overlapping_pairs}")
    if total_pairs > 0:
        ratio = overlapping_pairs / total_pairs
        print(f"Overlap ratio:             {ratio:.2%}") '''
    


