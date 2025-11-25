from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

openai_client = OpenAI()

# Vector Enbeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="langchain_rag_docs",
)

# Take user query
user_query = input("Ask something: ")

# Relevant chunks from the vector database
search_results = vector_db.similarity_search(query=user_query) 

context = "\n\n\n".join([
    f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
    for result in search_results
])


SYSTEM_PROMPT = f"""
You are a helpful AI assistant who answers user queries based on the available
context retrieved from a PDF file along with page_content and page number.

You should only provide answers the user based on the following context and navigate the
user to open the right page number to know more.SystemError

Context:
{{context}}
"""

response = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT.format(context=context)},
        {"role": "user", "content": user_query},
    ],
)

print(f"🤖: {response.choices[0].message.content}")