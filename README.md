# YouTube Summarizer

A Streamlit app that generates a summary of a YouTube video using its transcript. It leverages LangChain, Groq's LLM, and the YouTube Transcript API.

## Features

- **Transcript Extraction:** Retrieves video transcripts (preferring English) using the YouTube Transcript API.
- **Text Splitting:** Uses LangChain's `RecursiveCharacterTextSplitter` to break transcripts into manageable chunks.
- **Summarization:** Summarizes chunks with a map-reduce chain and combines them into a final summary with a title and introduction.
- **User-Friendly Interface:** Simple input fields and sidebar for Groq API key.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.7 or higher
- A valid Groq API Key
- YouTube video URL with an available transcript

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/youtube-summarizer.git
   cd youtube-summarizer
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required packages:**

   ```bash
   pip install streamlit validators langchain youtube_transcript_api langchain_groq
   ```

## Usage

1. **Run the app:**

   ```bash
   streamlit run app.py
   ```

2. **Interface Instructions:**
   - **Groq API Key:** Enter your Groq API key in the sidebar.
   - **YouTube URL:** Input the URL of the YouTube video you want to summarize.
   - Click on **Summarize** to process the video and display the summary.

## Code Structure

- **Imports:** Libraries for Streamlit UI, URL validation, transcript retrieval, text splitting, and summarization are imported.
- **UI Setup:** Configures the Streamlit page and collects user inputs (Groq API key and YouTube URL).
- **Video ID Extraction:** Extracts the video ID from a YouTube URL, handling both standard and shortened URLs.
- **Transcript Retrieval:** Uses YouTubeTranscriptApi to fetch the video transcript. If English is unavailable, it fetches the first available language.
- **Text Processing:** Combines transcript entries and splits the text into smaller documents for summarization.
- **Summarization Chain:** Defines map and combine prompt templates for summarizing text chunks using LangChain’s map-reduce chain.
- **Output:** Displays the final summary with a title and introduction in the app.

## Error Handling

- Validates URL format and YouTube domain.
- Catches exceptions for disabled transcripts, missing transcripts, or other errors and displays appropriate error messages.

---

Current date: Monday, February 03, 2025, 1 PM IST

Citations:
[1] https://stackoverflow.com/questions/76856230/how-to-extract-youtube-video-transcripts-using-youtube-api-on-python
[2] https://github.com/DevRico003/youtube_summarizer
[3] https://pypi.org/project/youtube-transcript-api/
[4] https://github.com/gopiashokan/YouTube-Video-Transcript-Summarizer-with-GenAI
[5] https://python.langchain.com/docs/integrations/document_loaders/youtube_transcript/
[6] https://www.youtube.com/watch?v=kjmsd-1coZo
[7] https://github.com/jdepoix/youtube-transcript-api/blob/master/youtube_transcript_api/_transcripts.py
[8] https://www.youtube.com/watch?v=HFfXvfFe9F8

---
Answer from Perplexity: pplx.ai/share