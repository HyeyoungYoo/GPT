{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain.chat_models import ChatOpenAI\n",
    "from langchain.prompts import PromptTemplate, ChatPromptTemplate\n",
    "from langchain.callbacks import StreamingStdOutCallbackHandler\n",
    "\n",
    "chat = ChatOpenAI(\n",
    "  temperature=0.1,\n",
    "  streaming=True,\n",
    "  callbacks=[StreamingStdOutCallbackHandler()]\n",
    ")\n",
    "\n",
    "chef_prompt = ChatPromptTemplate.from_messages([\n",
    "  (\"system\",\"You are a world-class international chef. You create easy to follow recipies for any type of cuisine with easy to find ingredients\"),\n",
    "  (\"human\",\"I want to cook {cuisine} food.\"),\n",
    "])\n",
    "\n",
    "chef_chain = chef_prompt | chat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Great choice! Indian cuisine is known for its bold flavors and aromatic spices. Let's start with a classic and popular dish - Chicken Tikka Masala. Here's a simple recipe for you to try at home:\n",
      "\n",
      "Ingredients:\n",
      "- 1 lb boneless, skinless chicken breasts, cut into bite-sized pieces\n",
      "- 1 cup plain yogurt\n",
      "- 2 tablespoons lemon juice\n",
      "- 2 tablespoons vegetable oil\n",
      "- 1 onion, finely chopped\n",
      "- 3 cloves garlic, minced\n",
      "- 1 tablespoon ginger, minced\n",
      "- 1 can (14 oz) tomato sauce\n",
      "- 1 tablespoon garam masala\n",
      "- 1 teaspoon ground cumin\n",
      "- 1 teaspoon ground coriander\n",
      "- 1 teaspoon paprika\n",
      "- 1/2 teaspoon turmeric\n",
      "- 1/2 teaspoon cayenne pepper (adjust to taste)\n",
      "- Salt and pepper to taste\n",
      "- Fresh cilantro, chopped for garnish\n",
      "\n",
      "Instructions:\n",
      "1. In a bowl, mix together the yogurt, lemon juice, 1 tablespoon of vegetable oil, half of the minced garlic, half of the minced ginger, and a pinch of salt. Add the chicken pieces and coat them well with the marinade. Cover and refrigerate for at least 1 hour, or overnight for best results.\n",
      "\n",
      "2. Preheat the oven to 400°F (200°C). Thread the marinated chicken pieces onto skewers and place them on a baking sheet. Bake for about 20-25 minutes or until the chicken is cooked through.\n",
      "\n",
      "3. In a large skillet, heat the remaining tablespoon of vegetable oil over medium heat. Add the chopped onion and cook until softened, about 5 minutes. Add the remaining garlic and ginger, and cook for another minute.\n",
      "\n",
      "4. Stir in the tomato sauce, garam masala, cumin, coriander, paprika, turmeric, cayenne pepper, salt, and pepper. Simmer for about 10 minutes, stirring occasionally.\n",
      "\n",
      "5. Add the cooked chicken tikka pieces to the sauce and simmer for an additional 5-10 minutes to allow the flavors to meld together.\n",
      "\n",
      "6. Serve the Chicken Tikka Masala over steamed rice or with naan bread. Garnish with fresh cilantro before serving.\n",
      "\n",
      "Enjoy your homemade Chicken Tikka Masala! Feel free to adjust the spice levels to suit your taste preferences.For a vegetarian version of Chicken Tikka Masala, you can easily substitute the chicken with a plant-based alternative such as tofu or paneer. Here's how you can prepare these alternatives:\n",
      "\n",
      "1. **Tofu**: \n",
      "   - Use firm or extra-firm tofu for this recipe. Press the tofu to remove excess water by wrapping it in a clean kitchen towel and placing a heavy object on top for about 15-20 minutes.\n",
      "   - Cut the tofu into bite-sized cubes and follow the same marinating process as you would with chicken. Tofu absorbs flavors well, so marinating it for a longer time can enhance the taste.\n",
      "   - Instead of baking, you can pan-fry the marinated tofu in a bit of oil until it's golden brown and slightly crispy.\n",
      "\n",
      "2. **Paneer**:\n",
      "   - Paneer is a traditional Indian cheese that holds its shape well when cooked. You can find it in Indian grocery stores or make it at home by curdling hot milk with lemon juice or vinegar.\n",
      "   - Cut the paneer into cubes and lightly pan-fry them until they develop a golden crust. You can also marinate the paneer cubes before frying for added flavor.\n",
      "   \n",
      "Follow the rest of the recipe as it is, substituting the chicken with your chosen alternative. The tofu or paneer will absorb the flavors of the aromatic spices and creamy tomato sauce, giving you a delicious vegetarian version of Chicken Tikka Masala. Enjoy your meal!"
     ]
    },
    {
     "data": {
      "text/plain": [
       "AIMessageChunk(content=\"For a vegetarian version of Chicken Tikka Masala, you can easily substitute the chicken with a plant-based alternative such as tofu or paneer. Here's how you can prepare these alternatives:\\n\\n1. **Tofu**: \\n   - Use firm or extra-firm tofu for this recipe. Press the tofu to remove excess water by wrapping it in a clean kitchen towel and placing a heavy object on top for about 15-20 minutes.\\n   - Cut the tofu into bite-sized cubes and follow the same marinating process as you would with chicken. Tofu absorbs flavors well, so marinating it for a longer time can enhance the taste.\\n   - Instead of baking, you can pan-fry the marinated tofu in a bit of oil until it's golden brown and slightly crispy.\\n\\n2. **Paneer**:\\n   - Paneer is a traditional Indian cheese that holds its shape well when cooked. You can find it in Indian grocery stores or make it at home by curdling hot milk with lemon juice or vinegar.\\n   - Cut the paneer into cubes and lightly pan-fry them until they develop a golden crust. You can also marinate the paneer cubes before frying for added flavor.\\n   \\nFollow the rest of the recipe as it is, substituting the chicken with your chosen alternative. The tofu or paneer will absorb the flavors of the aromatic spices and creamy tomato sauce, giving you a delicious vegetarian version of Chicken Tikka Masala. Enjoy your meal!\")"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "veg_chef_prompt = ChatPromptTemplate.from_messages([\n",
    "  (\"system\",\"You are a vegetarian chef specialized on making traditional recipies vegetarian. You find alternative ingredients and explain their preparation. you don't radically modify the recipe. If there is no alternative for a food just say you don't know how to replace it.\"),\n",
    "  (\"human\",\"{recipe}\"),\n",
    "])\n",
    "\n",
    "veg_chain = veg_chef_prompt | chat\n",
    "\n",
    "final_chain = {\"recipe\": chef_chain} | veg_chain\n",
    "\n",
    "final_chain.invoke({\n",
    "  \"cuisine\":\"indian\",\n",
    "})"
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
