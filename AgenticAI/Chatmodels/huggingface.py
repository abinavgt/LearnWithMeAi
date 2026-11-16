from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="" # model name 
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Why do parrots talk?")

print(response.content)


