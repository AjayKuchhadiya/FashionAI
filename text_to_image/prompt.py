from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
# from langchain_openai.chat_models import ChatOpenAI
# from langchain.memory import ConversationSummaryBufferMemory
from langchain_groq import ChatGroq
import time

from dotenv import load_dotenv

load_dotenv()

sample_1 = "A Blue floral skirt."
sample_1_output =  "yes"

sample_2 =  "A black color car."
sample_2_output = "no"

image_template = f"""

  **Task:** You are an experienced fashion designer. Your goal is to analyze given text delimited by ####.\
  Please identify whether the input text is a description of a fashion-related product or not.\
  Please return only `1`, if it is related to fashion-related product else return `2`.\

  **Expected Behavior:**
  - Please accurately determine whether the input text is a description of a fashion-related product.

  **Sample transcript and Expected Output:** Learn from below samples for Sample conversation, Expected Output:-
  Sample 1 conversation: {sample_1}
  Expected 1 Output: {sample_1_output}

  Sample 2 conversation: {sample_2}
  Expected 2 Output: {sample_2_output}


  **Points to consider**
  1. Make an effort again to confirm adherence to all instructions for providing your response.
  2. Please make sure that the output is parsable by python's int().
  3. Please do not provide any explaination to your response. 


  ####
  {{Text_prompt}}
  ####
  """

# pip install langchain-groq

llm = ChatGroq(temperature=0.0, model_name="Llama3-8b-8192")
prompt = PromptTemplate(template=image_template, input_variables=["Text_prompt"])

chain = LLMChain(prompt=prompt, llm=llm)

def refine_prompt(input_prompt): 
  
  new_prompt = chain.invoke({"Text_prompt": input_prompt})
  # print(new_prompt)
  return new_prompt

s = time.time()

# input = 'A Blue floral skirt'
# input = 'A porche car'
input = input('\n\nPlease provide the description for image generation : ')
x = refine_prompt(input)

# print('\n\nThe new prompt : ', x['text'])

if int(x['text']) == 1: 
  print('\n\nThe description is related to fashion product')

if int(x['text']) == 2: 
  print('\n\nThe description is not related to fashion product')
e = time.time()
# print('diff : ', e-s)