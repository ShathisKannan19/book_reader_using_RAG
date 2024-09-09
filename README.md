# RAG Application for using the Book reader

Book Reading Friend using RAG(Retrieval Argumented Generation)

Python Version

```
Python 3.12
```

## Tech Stack

**Client:** Streamlit

**Server:** Python, FastAPI, AI(langchain, huggingface, Groq, Chroma DB)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

- Create the API from the [GROQ API](https://console.groq.com/keys) `GROQ_API_KEY`

And also you must add verify frontend.env is in root folder of the project.

- API for Chat `API_URI`
- API for delete `API_URI_DELETE`


## Deployment

To deploy this project run

```bash
git clone https://github.com/ShathisKannan19/book_reader_using_RAG.git
```

Then, you go to install the packages you need to run

```bash
cd frontend
poetry install
```
and run the code using below line
```bash
streamlit run main.py
```

open another terminal for install the backend packages

```bash
cd backend
poetry install
```

then run the code after installing
```bash
uvicorn main:app --reload
```



## Authors

- [@ShathisKannan19](https://www.github.com/ShathisKannan19)


> [!NOTE]  
> It was a Good application you must try this for a personal friend as well, It will be imporve in this repo.

> [!TIP]
> You use this as Book reader and also you must know about that book, Like which Joner or Key part of the Book.

> [!IMPORTANT]  
> You must give the context in your question, I have not maintained the messages as History.