from pathlib import Path
import sys

import streamlit as st

qapp_root = str(Path(__file__).resolve().parents[1])
if qapp_root not in sys.path:
    sys.path.insert(0, qapp_root)

from Backend.qa_service import answer_question
 
st.title("QApp - Simple Docker Demo")
question = st.text_input("Ask a question")
 
if st.button("Ask") and question.strip():
    st.success(answer_question(question))
