# header files
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os
from api import api

# defining API
os.environ["GOOGLE_API_KEY"] = api

# initializing model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    temperature=0.7
)

# ✅ correct method: from_template
prompt = ChatPromptTemplate.from_template("List 3 fun facts about {animal} like I am {age}.")

# linking prompt and model
chain = prompt | llm

# taking input
u_animal = input("Enter the animal you want to learn fun facts about: ")
u_age = input("Enter your age: ")

# response
response = chain.invoke({"animal": u_animal, "age": u_age})

print("\nHere are some fun facts:")
print(response.content)
