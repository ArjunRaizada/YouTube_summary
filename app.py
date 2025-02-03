import streamlit as st
import validators
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.schema import Document
from langchain_groq import ChatGroq
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from langchain.text_splitter import RecursiveCharacterTextSplitter

st.set_page_config(page_title="YouTube Summarizer", page_icon="🦜")
st.title("Content Digest: YouTube")

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", type="password", help="Enter your Groq API key here.")


def get_video_id(url):
    if "youtube.com" in url:
        return url.split("v=")[-1].split("&")[0]
    if "youtu.be" in url:
        return url.split("/")[-1]
    return None

youtube_url = st.text_input("Enter YouTube URL:")

if st.button("Summarize"):
    if not groq_api_key.strip() or not youtube_url.strip():
        st.error("Please fill in all fields.")
    elif not validators.url(youtube_url) or ("youtube.com" not in youtube_url and "youtu.be" not in youtube_url):
        st.error("Enter a valid YouTube URL.")
    else:
        try:
            with st.spinner("Processing..."):
                llm = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)
                video_id = get_video_id(youtube_url)
                if not video_id:
                    st.error("Invalid YouTube URL.")
                try:
                    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                    try:
                        transcript = transcript_list.find_transcript(['en']).fetch()
                    except Exception:
                        available_langs = list(transcript_list._transcripts.keys())
                        transcript = transcript_list.find_transcript([available_langs[0]]).fetch()
                    text = " ".join([entry['text'] for entry in transcript])
                    docs = [Document(page_content=text)]
                except TranscriptsDisabled:
                    st.error("Transcripts are disabled for this video.")
                    docs = []
                except NoTranscriptFound:
                    st.error("No transcript available for this video.")
                    docs = []
                except Exception as e:
                    st.error(f"Error: {e}")
                    docs = []

                if docs:
                    final_docs = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100).split_documents(docs)
                    
                    map_prompt = PromptTemplate(
                        input_variables=["text"],
                        template="Summarize the following extract in 150 words:\n\nText: {text}\n\nSummary:"
                    )
                    combine_prompt = PromptTemplate(
                        input_variables=["text"],
                        template="Provide the final summary with a title and introduction:\n\nText: {text}"
                    )
                    
                    summary_chain = load_summarize_chain(
                        llm=llm,
                        chain_type="map_reduce",
                        map_prompt=map_prompt,
                        combine_prompt=combine_prompt,
                        verbose=True
                    )
                    output_summary = summary_chain.run(final_docs)
                    st.success(output_summary)
        except Exception as e:
            st.exception(f"Exception: {e}")