import os
from llama_index import SimpleDirectoryReader,LLMPredictor,ServiceContext,GPTVectorStoreIndex
from langchain import OpenAI

os.environ["OPENAI_API_KEY"] = ''

class LLma:
    def __init__(self):
        self.llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003",max_tokens=1800))
        self.service_context = ServiceContext.from_defaults(llm_predictor=self.llm_predictor)


    def query_index(self,prompt,index_path="./index.json"):
        #local_index = GPTVectorStoreIndex.
        pass

    def create_index(self,dir_path="./data"):
        document = SimpleDirectoryReader(dir_path).load_data()
        index = GPTVectorStoreIndex.from_documents(document,service_context=self.service_context)
        print(document)
        query_engine = index.as_query_engine()
        res = query_engine.query("讲一下美女蛇的故事")
        print(res)
        index.storage_context.persist()

if __name__ == "__main__":
    llm = LLma()
    llm.create_index()


