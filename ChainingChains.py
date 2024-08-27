#!/usr/bin/env python
# coding: utf-8

# In[6]:


#8_26 숙제 
#프로그래밍 언어에 대한 시를 쓰는 데 특화된 체인과 시를 설명하는 데 특화된 체인을 만드세요.
#LCEL을 사용해 두 체인을 서로 연결합니다.
#최종 체인은 프로그래밍 언어의 이름을 받고 시와 그 설명으로 응답해야 합니다.
#모델로는 "gpt-3.5-turbo"를 사용하고 프롬프트에는 ChatPromptTemplate을 사용하세요.

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler

chat = ChatOpenAI(
  temperature=0.1,
  streaming=True,
  callbacks=[StreamingStdOutCallbackHandler()]
)

poet_prompt = ChatPromptTemplate.from_messages([
  ("system","you are a poet In particular, I have a deep understanding of programming languages, so I specialize in writing poetry about programming languages."),
  ("human","Write a poem about {language}."),
])

poet_chain = poet_prompt | chat


# In[7]:


commentor_prompt = ChatPromptTemplate.from_messages([
  ("system","You are an excellent poetry commentator. You can interpret the literary meaning of each verse of poetry. If you don't know, don't force meaning, just say you don't know."),
  ("human","{Poetry}"),
])

commentor_chain = commentor_prompt | chat

final_chain = {"Poetry": poet_chain} | commentor_chain

final_chain.invoke({
  "language":"python",
})

