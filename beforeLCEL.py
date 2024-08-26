{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'What is the distance between Mexico and Russia'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from langchain.chat_models import ChatOpenAI\n",
    "from langchain.prompts import PromptTemplate, ChatPromptTemplate\n",
    "\n",
    "chat = ChatOpenAI(temperature=0.1)\n",
    "template = PromptTemplate.from_template(\n",
    "  \"What is the distance between {country_a} and {country_b}\",\n",
    ")\n",
    "prompt = template.format(country_a=\"Mexico\", country_b=\"Russia\")\n",
    "\n",
    "chat.predict(prompt)\n",
    "\n",
    "\n",
    "\n",
    "#b = chat.predict(\"How many planets are there?\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "AIMessage(content='Γεια σας! Το όνομά μου είναι Σωκράτης. Η απόσταση μεταξύ του Μεξικού και της Ταϊλάνδης είναι περίπου 16.000 χιλιόμετρα.')"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from langchain.schema import HumanMessage, AIMessage, SystemMessage\n",
    "\n",
    "template = ChatPromptTemplate.from_messages(\n",
    "  [\n",
    "    (\"system\", \"You are a geography export. And you only reply in {language}.\"),\n",
    "    (\"ai\",\"Ciao, mi chiamo {name}!\"),\n",
    "    (\"human\",\"What is the distance between {country_a} and {country_b}. Also, What is your name?\"),\n",
    "  ]\n",
    ")\n",
    "\n",
    "prompt = template.format_messages(\n",
    "  language=\"Greek\",\n",
    "  name=\"Socrates\",\n",
    "  country_a=\"Mexico\",\n",
    "  country_b=\"Thailand\",\n",
    ")\n",
    "chat.predict_messages(prompt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from Langchain.schema import BaseOutputParser\n",
    "\n",
    "class CommaOutputParser(BaseOutputParser):\n",
    "  def parse(self, text):\n",
    "    items =  text.strip().split(\",\")  # strip : text 앞뒤 공백을 잘라냄\n",
    "    return list(map(str.strip, items))\n",
    "\n",
    "p = CommaOutputParser()\n",
    "\n",
    "p.parse(\"Hello, how, are, you\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "env",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
