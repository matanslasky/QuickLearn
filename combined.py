import os
import whisper
import ffmpeg
import tkinter as tk
from tkinter import filedialog, messagebox
from transformers import pipeline

def transcribe_audio(input_file, output_file):
    # Load the Whisper model
    model = whisper.load_model("base")

    # Load the input audio file
    audio = whisper.load_audio(input_file)

    # Transcribe the audio
    result = model.transcribe(audio)

    # Save the transcription results to a new file
    with open(output_file, "w", encoding='utf-8') as f:
        f.write(result["text"])

    print(f"Transcription saved to: {output_file}")

def summarize_text(input_file, output_file):
    # Load the summarization pipeline
    summarizer = pipeline("summarization")

    # Read the input text file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Summarize the text
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)

    # Write the summary to the output text file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(summary[0]['summary_text'])

def process_file(file_path):
    # Check the file extension and convert to WAV if necessary
    if file_path.endswith(".mp3") or file_path.endswith(".mp4"):
        wav_file = os.path.splitext(file_path)[0] + ".wav"
        (
            ffmpeg
            .input(file_path)
            .output(wav_file)
            .run()
        )
        file_path = wav_file
    
    # Output file for transcription
    transcription_file = os.path.splitext(file_path)[0] + "_transcription.txt"
    
    # Transcribe the audio and save the results
    transcribe_audio(file_path, transcription_file)
    
    return transcription_file

def run_transcribe_and_summarize():
    # Get the file path from the entry field
    file_path = file_entry.get()
    if file_path:
        try:
            # Step 1: Transcribe the audio file
            transcription_file = process_file(file_path)
            
            # Step 2: Summarize the transcription
            summary_file = 'summary.txt'
            summarize_text(transcription_file, summary_file)
            
            # Step 3: Display the summary
            with open(summary_file, 'r', encoding='utf-8') as f:
                summary_text = f.read()

            output_text.delete(1.0, tk.END)  # Clear the text box
            output_text.insert(tk.END, summary_text)  # Display the summary

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please select a file first.")

def select_file():
    # Open a file dialog and allow the user to select a file
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        file_entry.delete(0, tk.END)  # Clear the entry field
        file_entry.insert(0, file_path)  # Insert the selected file path into the entry field

def show_contact_info():
    # Create a new top-level window for the Contact Us information
    contact_window = tk.Toplevel()
    contact_window.title("Contact Us")
    contact_window.geometry("400x300")
    contact_window.configure(bg="#ECEFF4")

    # Display the information about the creators
    info_label = tk.Label(contact_window, text="About the Creators", font=("Helvetica", 16, "bold"), bg="#ECEFF4", fg="#2E3440")
    info_label.pack(pady=20)

    creator_info = """
    Creator 1: Yonatan Rahamim
      - Developer
      - yonatan.rahamim@gmail.com
    
    Creator 2: Matan Slasky
      - Developer
      - matanslasky@gmail.com
    """
    info_text = tk.Label(contact_window, text=creator_info, font=("Helvetica", 12), bg="#ECEFF4", fg="#4C566A", justify="left")
    info_text.pack(pady=10, padx=20)

    # Close button
    close_button = tk.Button(contact_window, text="Close", command=contact_window.destroy, font=("Helvetica", 12), bg="#81A1C1", fg="white", relief="flat", cursor="hand2")
    close_button.pack(pady=20)

def confirm_exit():
    # Show a confirmation dialog
    response = messagebox.askyesno("Exit", "Are you sure you want to leave?")
    if response:
        root.quit()  # Terminate the program if the user confirms

def create_gui():
    global root, file_entry, output_text
    # Initialize the main window
    root = tk.Tk()
    root.title("File Summarizer")
    root.geometry("800x500")
    root.configure(bg="#2E3440")

    # Sidebar frame
    sidebar = tk.Frame(root, width=200, bg="#4C566A")
    sidebar.pack(expand=False, fill="y", side="left", anchor="nw")

    # Sidebar content
    logo_label = tk.Label(sidebar, text="File Summarizer", bg="#4C566A", fg="white", font=("Helvetica", 16, "bold"))
    logo_label.pack(pady=20)

    file_button = tk.Button(sidebar, text="Select File", font=("Helvetica", 14), bg="#81A1C1", fg="white", bd=0, relief="flat", cursor="hand2", height=2, command=select_file)
    file_button.pack(pady=10, fill="x", padx=20)

    summarize_button = tk.Button(sidebar, text="Summarize", font=("Helvetica", 14), bg="#81A1C1", fg="white", bd=0, relief="flat", cursor="hand2", height=2, command=run_transcribe_and_summarize)
    summarize_button.pack(pady=10, fill="x", padx=20)

    contact_button = tk.Button(sidebar, text="Contact Us", font=("Helvetica", 14), bg="#A3BE8C", fg="white", bd=0, relief="flat", cursor="hand2", height=2, command=show_contact_info)
    contact_button.pack(pady=10, fill="x", padx=20)

    exit_button = tk.Button(sidebar, text="Exit", font=("Helvetica", 14), bg="#BF616A", fg="white", bd=0, relief="flat", cursor="hand2", height=2, command=confirm_exit)
    exit_button.pack(pady=10, fill="x", padx=20)

    # Main content area
    main_area = tk.Frame(root, bg="#D8DEE9", bd=10)
    main_area.pack(expand=True, fill="both", side="right")

    # Main content: Title and input fields
    title_label = tk.Label(main_area, text="Summarize Your File", bg="#D8DEE9", fg="#2E3440", font=("Helvetica", 24, "bold"))
    title_label.pack(pady=20)

    file_label = tk.Label(main_area, text="Selected File:", bg="#D8DEE9", fg="#2E3440", font=("Helvetica", 14))
    file_label.pack(pady=10)

    file_entry = tk.Entry(main_area, font=("Helvetica", 14), width=50, bd=2, relief="solid")
    file_entry.pack(pady=10)

    output_label = tk.Label(main_area, text="Summary:", bg="#D8DEE9", fg="#2E3440", font=("Helvetica", 14))
    output_label.pack(pady=10)

    output_text = tk.Text(main_area, height=10, font=("Helvetica", 14), wrap="word", bd=2, relief="solid")
    output_text.pack(pady=10, fill="both", padx=20)

    # Placeholder for output
    summary_placeholder = tk.Label(main_area, text="Summary will appear here after processing.", bg="#D8DEE9", fg="#4C566A", font=("Helvetica", 14, "italic"))
    summary_placeholder.pack(pady=20)

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
