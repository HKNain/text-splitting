from langchain_text_splitters import MarkdownHeaderTextSplitter

text = """
# Introduction
LangChain is a framework for LLM applications.

## Document Loading
It loads data from different sources.

## Text Splitting
It divides large documents into smaller chunks.

# Conclusion
LangChain simplifies LLM development.
"""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2")
]

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

documents = splitter.split_text(text)

for doc in documents:
    print(doc.page_content)
    print(doc.metadata)