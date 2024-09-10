import asyncio
import sys
import streamlit as st
from langchain.document_loaders import SitemapLoader
from langchain.document_transformers import Html2TextTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS 
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


answers_prompt = ChatPromptTemplate.from_template("""
    Using ONLY the following context answer the user's question. If you can't just say you don't know, don't make anything up.
                                                  
    Then, give a score to the answer between 0 and 5. 0 being not helpful to the user and 5 being helpful to the user.
    Make sure to include the answer's score.

    Context: {context}
                                                  
    Examples:
                                                  
    Question: How far away is the moon?
    Answer: The moon is 384,400 km away.
    Score: 5
                                                  
    Question: How far away is the sun?
    Answer: I don't know
    Score: 0
                                                  
    Your turn!
  
    Question: {question}
""")

def get_answers(inputs):
  docs = inputs['docs']
  question = inputs['question']
  answers_chain = answers_prompt | llm
  # answers = []
  # for doc in docs:
  #   result = answers_chain.invoke({
  #     "question":question,
  #     "context":doc.page_content
  #   })
  #   answers.append(result.content)
  return {
        "question": question,
        "answers": [
            {
                "answer": answers_chain.invoke(
                    {"question": question, "context": doc.page_content}
                ).content,
                "source": doc.metadata["source"],
                "date": doc.metadata["lastmod"],
            }
            for doc in docs
        ],
    }

choose_prompt=ChatPromptTemplate.from_messages(
  [
    (
      "system",
      """
      Use ONLY the following pre-existing answers to answer the user's question.

      Use the answers that have the highest score (more helpful) and favor the most recent ones.

      Cite sources and return the sources of the answers as they are, do not change them.

      Answers: {answers}
      """
    ),
    ("human","{question}"),
  ]
)

def choose_answer(inputs):
    answers = inputs["answers"]
    question = inputs["question"]
    choose_chain = choose_prompt | llm
    condensed = "\n\n".join(
      f"Answer:{answer['answer']}\nSource:{answer['source']}\nDate:{answer['date']}\n"
      for answer in answers
    )
    return choose_chain.invoke({
      "question": question,
      "answers": condensed,
    })

def parse_page(soup): #포함시킼고 싶은 text를 반환하는 함수.
    header = soup.find("header")
    footer = soup.find("footer")
    if header:
        header.decompose()
        print("header deleted")
        #text = header.get_text()
    if footer:
        footer.decompose()
        print("footer deleted")
    else:
        print("No header!")
        #document 의 전체 HTML을 가진 beautiful soup object 값이 바로 soup
    return (
      str(soup.get_text())
      .replace("\n"," ")
      .replace("\xa0"," ")
      .replace("CloseSearch Submit Blog"," ")
    )  

 #load_website가 한 번 실행된 후, 같은 url로 다시 호출되면 아무일도 안하도록 설정
@st.cache_data(show_spinner="Loading website...")
def load_website(url):
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
      chunk_size=1000,
      chunk_overlap=200,
    )
    loader = SitemapLoader(
      url,
      parsing_function=parse_page,
      )      
    loader.requests_per_second = 1  # 차단 방지를 위해 1초에 한번 request 보내도록 강제
    docs = loader.load_and_split(text_splitter=splitter) 
    vector_store = FAISS.from_documents(docs, embedding=OpenAIEmbeddings(openai_api_key=key))
    #cache 할 수 있음. 그러나 각각의 URL 마다 별도로 cache를 만들어야함.
    return vector_store.as_retriever() #vector_store 생성하고 retriever로 변환한 것


st.set_page_config(
    page_title="SiteGPT",
    page_icon="😎",
)
html2text_transformer = Html2TextTransformer()

st.markdown(
    """
    # SiteGPT
            
    Ask questions about the content of a website.
            
    Start by writing the URL of the website on the sidebar.
"""
)

if "win32" in sys.platform:
  # Windows specific event-loop policy & cmd
  asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
  cmds = [['C:/Windows/system32/HOSTNAME.EXE']]
else:
  # Unix default event-loop policy & cmds
  cmds = [
      ['du', '-sh', '/Users/fredrik/Desktop'],
      ['du', '-sh', '/Users/fredrik'],
      ['du', '-sh', '/Users/fredrik/Pictures']
  ]

url = st.text_input("Write down a URL", placeholder="http://example.com")
if url:
  if ".xml" not in url:
    with st.sidebar:
      st.error("Sitemap URL을 입력해주세요")
  else:
    with st.sidebar:
      key = st.text_input("Enter your Open your API KEY")   
    if key:
      llm = ChatOpenAI(
        temperature=0.1,
        openai_api_key=key,
      )
      retriever = load_website(url)
      query = st.text_input("Ask a question to the website.")
      if query:
        chain = {
          "docs": retriever,
          "question":RunnablePassthrough()
          } | RunnableLambda(get_answers) | RunnableLambda(choose_answer)

        result = chain.invoke(query)
        st.write(result.content.replace("$","\$")) #$를 이상한 문자로 인식하는 streamlit 오류수정
    else:
      with st.sidebar:
        st.error("You need apikey.")



