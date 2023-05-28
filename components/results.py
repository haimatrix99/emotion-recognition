import itertools
import streamlit as st

from PIL import Image
import numpy as np
from deepface import DeepFace

emotion_mapping = {
    'angry': 'Tức giận',
    'disgust': 'Ghê tởm',
    'fear': 'Sợ hãi',
    'happy': 'Hạnh phúc',
    'sad': 'Buồn bã',
    'surprise': 'Ngạc nhiên',
    'neutral': 'Bình thường'
}

star_emotion = {
    'angry': '⭐',
    'disgust': '⭐',
    'fear': '⭐',
    'happy': '⭐⭐⭐⭐⭐',
    'sad': '⭐⭐',
    'surprise': '⭐⭐⭐',
    'neutral': '⭐⭐⭐⭐',
}

def get_results(img_file_buffer):
    if img_file_buffer is not None:
        img = Image.open(img_file_buffer)
        img_array = np.array(img)
        results = DeepFace.analyze(img_path = img_array, 
            actions = ['emotion']
            )
        return results[0]['emotion']
    else:
        return None

def show_results(results):
    st.markdown('## Kết quả')
    if results is not None:
        results_sorted = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)}
        thirth_results_sorted = dict(itertools.islice(results_sorted.items(), 3))
        st.markdown("### Cảm xúc của khách hàng có thể là:")
        for emotion, score in thirth_results_sorted.items():
            st.write(f"{emotion_mapping[emotion]} - Phần trăm: {score:.02f}%")
        st.markdown("### Khách hàng có thể đánh giá: {}".format(star_emotion[list(results_sorted.keys())[0]]))
    else:
        st.info("Ấn nút 'Take Photo' để lấy kết quả")