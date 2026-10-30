from langchain_text_splitters import CharacterTextSplitter

text = """
LangChain is a framework for building applications
using Large Language Models. It provides tools
for document loading, splitting and retrieval.
"""

splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=50,
    chunk_overlap=10
)

chunks = splitter.split_text(text)

for chunk in chunks:
    print(chunk)
    print("----------")