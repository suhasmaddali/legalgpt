import streamlit as st
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Title and description
st.title("Audio Analysis Application")
st.write("Upload a `.wav` audio file to analyze its properties and get insights.")

# File uploader
audio_file = st.file_uploader("Upload Audio File", type=["wav"])

if audio_file is not None:
    # Read audio file
    try:
        sample_rate, audio_data = wavfile.read(audio_file)
        st.success("Audio file uploaded successfully!")
        
        # Ensure the data is mono
        if len(audio_data.shape) == 2:
            st.warning("Stereo detected. Using only one channel for analysis.")
            audio_data = audio_data[:, 0]

        # Insights
        duration = len(audio_data) / sample_rate
        st.write(f"**Sampling Rate:** {sample_rate} Hz")
        st.write(f"**Duration:** {duration:.2f} seconds")
        st.write(f"**Number of Samples:** {len(audio_data)}")
        st.write(f"**Amplitude Range:** {audio_data.min()} to {audio_data.max()}")

        # Plot the waveform
        st.subheader("Waveform")
        time_axis = np.linspace(0, duration, num=len(audio_data))
        plt.figure(figsize=(10, 4))
        plt.plot(time_axis, audio_data, label="Waveform")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Amplitude")
        plt.title("Audio Waveform")
        plt.legend()
        st.pyplot(plt)

        # Frequency spectrum
        st.subheader("Frequency Spectrum")
        freq_axis = np.fft.rfftfreq(len(audio_data), 1 / sample_rate)
        fft_magnitude = np.abs(np.fft.rfft(audio_data))
        plt.figure(figsize=(10, 4))
        plt.plot(freq_axis, fft_magnitude, label="Frequency Spectrum")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")
        plt.title("Frequency Spectrum")
        plt.legend()
        st.pyplot(plt)

    except Exception as e:
        st.error(f"An error occurred while processing the audio file: {e}")
