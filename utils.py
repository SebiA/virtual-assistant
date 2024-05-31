from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


def get_embeddings():
    hf = HuggingFaceEmbeddings(
        model_name="intfloat/e5-small-v2",
        model_kwargs={'device': 'cpu'}
    )
    return hf


def load_db():
    hf = get_embeddings()
    db = FAISS.load_local("data", hf, allow_dangerous_deserialization=True)
    return db


def get_llm_response(user_input):
    db = load_db()
    retriever = db.as_retriever()
    with open('prompt.txt', 'r') as file:
        prompt = file.read().replace('\n', '')

    llm = ChatOpenAI(temperature=0)

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", prompt),
            ("human", "{context}"),
        ]
    )
    
    question_answer_chain = create_stuff_documents_chain(llm, prompt_template)
    chain = create_retrieval_chain(retriever, question_answer_chain)
    response = chain.invoke({"input": user_input})
    return response["answer"]

