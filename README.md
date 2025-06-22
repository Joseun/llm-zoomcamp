# LLM Zoomcamp - RAG Demo

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline using LLMs, Elasticsearch, Qdrant, and embedding models. It is based on the [DataTalksClub LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) course.

## Features

- Loads course FAQ documents from a remote JSON source
- Indexes documents in Elasticsearch and Qdrant
- Performs semantic and keyword search over course FAQs
- Builds prompts for LLMs using search results
- Calls Llama-3.3-70B-Versatile via Groq API for answers
- Calculates token usage and cost for each query
- Example notebooks for both Elasticsearch and Qdrant vector search

## Requirements

- Python 3.8+
- Elasticsearch (running locally on port 9200)
- Qdrant (running locally on port 6333)
- See [requirements.txt](requirements.txt) for Python dependencies

## Installation

```sh
pip install -r requirements.txt
```

## Usage

### 1. Start Elasticsearch and Qdrant locally

**Elasticsearch:**
```sh
docker run -d -p 9200:9200 -e "discovery.type=single-node" elasticsearch:8.4.3
```

**Qdrant:**
```sh
docker run -d -p 6333:6333 qdrant/qdrant
```

### 2. Set your Groq API key in a `.env` file

```
API-KEY=your_groq_api_key_here
```

### 3. Open and run the notebooks

- [rag-intro.ipynb](rag-intro.ipynb): RAG pipeline with Elasticsearch and Groq LLM
- [vector-search.ipynb](vector-search.ipynb): Vector search with Qdrant and fastembed

The notebooks will:
- Download and index FAQ documents
- Run search and RAG queries
- Show example prompts, answers, and cost calculations

## Example Query

```python
query = "How do I copy a file to a Docker container?"
rag(query, "machine-learning-zoomcamp", 3, 3)
```

## Project Structure

```
.
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── rag-intro.ipynb
├── vector-search.ipynb
└── qdrant_storage/
```

## License

MIT License

## Credits

- [DataTalksClub LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp)
- [Groq](https://groq.com/)
- [Qdrant](https://qdrant.tech/)
- [Elasticsearch](https://www.elastic.co/)
