import chromadb
from pdf_loader import load_pdf,load_all_pdfs
from chunking import faq_chunking, policy_chunking
from dotenv import load_dotenv
import os
from google import genai

#Gemini Client

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
        
gemini_client = genai.Client(
    api_key = api_key
)

#Choroma Client 

chroma_client = chromadb.PersistentClient(path="./chroma_db")

#Chroma Collection 

collection = chroma_client.get_or_create_collection(
        name="pdf_collection"
        )


def build_vector_db():
    all_chunks = []
    
    # Loading PDFs

    print("Loading PDFs...")
    faq_doc = load_pdf("./docs/Acko_Insurance_FAQs.pdf")
    health_policy_doc= load_pdf("./docs/Acko_Health_Insurance_Policy_TC.pdf")
    motor_policy_doc = load_pdf("./docs/Acko_Motor_Insurance_Policy_TC.pdf")

    #Converting List of Documents into Texts

    faq_text = "\n".join([doc.page_content for doc in faq_doc])
    health_policy_text = "\n".join([doc.page_content for doc in health_policy_doc])
    motor_policy_text = "\n".join([doc.page_content for doc in motor_policy_doc])
   
    # Chunking PDFs

    print("Chunking PDFs...")
    faq_chunks = faq_chunking(faq_text)
    health_policy_chunks= policy_chunking(health_policy_text,pdf_name="health_policy")
    motor_policy_chunks = policy_chunking(motor_policy_text,pdf_name="motor_policy")

    # Combine Chunks

    all_chunks = faq_chunks+health_policy_chunks+motor_policy_chunks
    print(f"Total chunks: {len(all_chunks)}")
    
    # Create Embedding Vectors using gemini-embedding-2

    print("Generating embeddings...")
    all_embeddings = []
    for idx, chunk in enumerate(all_chunks):
        print(f"Embedding chunk {idx+1}/{len(all_chunks)}")
        result = gemini_client.models.embed_content(
            model='gemini-embedding-2',
            contents=chunk['text']
            )
        embedding = result.embeddings[0].values

        #Storing in chromaDB

        collection.add(
            ids=[chunk["id"]],
            embeddings=[embedding],
            documents=[chunk["text"]],
            metadatas=[chunk["metadata"]]
        )


if __name__ == "__main__":
    build_vector_db()