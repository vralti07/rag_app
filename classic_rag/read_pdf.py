from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain_core.documents import Document


#pdf_path = "./wellsFargoStatments/012524WellsFargo.pdf"
total_words = []

def pdf_loader(src_path):
    print("...inside read_pdf.pdf_loader method...");
    src_loader = PyPDFDirectoryLoader(src_path)
    src_pages = src_loader.load()
    print_doc_content(src_pages)
    print("...returning pdf loader method...")
    return src_pages


def print_doc_content(content :list[Document]): 
    pages = content #pdf_loader(pdf_path)


    print('pages length : ', len(pages))
    if(len(pages) <= 0):
        print('no pages to print')
        raise SystemExit(1)
    print('first page meta data : ', pages[0].metadata)

    first_page = pages[0].page_content.split()

    for page in pages:
        words = page.page_content.split()
        print('current page ', page.metadata['page'])
        print('number of words in ', page.metadata['page'], ' : ', len(words))
        for word in words:
            word = word.strip()
            if(len(word)> 0):
                total_words.append(word);

    '''count2 = 1
    for word in first_page:
        print(word)
        if(count2 == 500):
            print('completed first 500 words')
            break;
        count2 = count2 + 1

    count = 1
    for word in total_words:
        #print(word)
        if(count == 500):
            print('completed first 500 words')
            break;
        count = count + 1'''