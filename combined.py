import os
import whisper
import ffmpeg
import tkinter as tk
from tkinter import filedialog, messagebox
from transformers import pipeline

# BackEnd class
class BackEnd:
    def __init__(self):
        # Load Whisper and summarization models
        self.model = whisper.load_model("base")
        self.summarizer = pipeline("summarization")

    def transcribe_audio(self, input_file, output_file):
        # Load the input audio file
        audio = whisper.load_audio(input_file)

        # Transcribe the audio
        result = self.model.transcribe(audio)

        # Save the transcription results to a new file
        with open(output_file, "w", encoding='utf-8') as f:
            f.write(result["text"])

        return output_file

    def summarize_text(self, input_file, output_file):
        # Read the input text file
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Summarize the text
        summary = self.summarizer(text, max_length=150, min_length=30, do_sample=False)

        # Write the summary to the output text file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(summary[0]['summary_text'])

        return output_file

    def convert_file(self, file_path):
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
        self.transcribe_audio(file_path, transcription_file)
        
        return transcription_file

# FrontEnd class
class FrontEnd:
    def __init__(self, root):
        self.processor = BackEnd()  

        self.root = root
        self.root.title("File Summarizer")
        self.root.geometry("800x500")
        self.root.configure(bg="#2E3440")

        self.create_gui()

    def create_gui(self):
        # Sidebar frame
        sidebar = tk.Frame(self.root, width=200, bg="#4C566A")
        sidebar.pack(expand=False, fill="y", side="left", anchor="nw")

        # Sidebar content
        logo_label = tk.Label(sidebar, text="File Summarizer", bg="#4C566A", fg="white", font=("Helvetica", 16, "bold"))
        logo_label.pack(pady=20)

        file_button = tk.Button(sidebar, text="Select File", font=("Helvetica", 14), bg="#81A1C1", fg="white", bd=0, relief="flat", cursor="hand2", height=2, command=self.select_file)
        file_button.pack(pady=10, fill="x", padx=20)

        summarize_button = tk.Button(sidebar, text="Summarize", font=("Helvetica", 14), bg="#81A1C1", fg="white", bd=0, relief="flat", cursor="hand2", height=2, command=self.run_transcribe_and_summarize)
        summarize_button.pack(pady=10, fill="x", padx=20)

        contact_button = tk.Button(sidebar, text="Contact Us", font=("Helvetica", 14), bg="#A3BE8C", fg="white", bd=0, relief="flat", cursor="hand2", height=2, command=self.show_contact_info)
        contact_button.pack(pady=10, fill="x", padx=20)

        exit_button = tk.Button(sidebar, text="Exit", font=("Helvetica", 14), bg="#BF616A", fg="white", bd=0, relief="flat", cursor="hand2", height=2, command=self.confirm_exit)
        exit_button.pack(pady=10, fill="x", padx=20)

        # Main content area
        main_area = tk.Frame(self.root, bg="#D8DEE9", bd=10)
        main_area.pack(expand=True, fill="both", side="right")

        # Main content: Title and input fields
        title_label = tk.Label(main_area, text="Summarize Your File", bg="#D8DEE9", fg="#2E3440", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=20)

        file_label = tk.Label(main_area, text="Selected File:", bg="#D8DEE9", fg="#2E3440", font=("Helvetica", 14))
        file_label.pack(pady=10)

        self.file_entry = tk.Entry(main_area, font=("Helvetica", 14), width=50, bd=2, relief="solid")
        self.file_entry.pack(pady=10)

        output_label = tk.Label(main_area, text="Summary:", bg="#D8DEE9", fg="#2E3440", font=("Helvetica", 14))
        output_label.pack(pady=10)

        self.output_text = tk.Text(main_area, height=10, font=("Helvetica", 14), wrap="word", bd=2, relief="solid")
        self.output_text.pack(pady=10, fill="both", padx=20)

    def run_transcribe_and_summarize(self):
        file_path = self.file_entry.get()
        if file_path:
            try:
                # Step 1: Transcribe the audio file
                transcription_file = self.processor.convert_file(file_path)
                
                # Step 2: Summarize the transcription
                summary_file = 'summary.txt'
                self.processor.summarize_text(transcription_file, summary_file)
                
                # Step 3: Display the summary
                with open(summary_file, 'r', encoding='utf-8') as f:
                    summary_text = f.read()

                self.output_text.delete(1.0, tk.END)  # Clear the text box
                self.output_text.insert(tk.END, summary_text)  # Display the summary

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Please select a file first.")

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select a file")
        if file_path:
            self.file_entry.delete(0, tk.END)  # Clear the entry field
            self.file_entry.insert(0, file_path)  # Insert the selected file path into the entry field

    def show_contact_info(self):
        contact_window = tk.Toplevel()
        contact_window.title("Contact Us")
        contact_window.geometry("400x300")
        contact_window.configure(bg="#ECEFF4")

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

        close_button = tk.Button(contact_window, text="Close", command=contact_window.destroy, font=("Helvetica", 12), bg="#81A1C1", fg="white", relief="flat", cursor="hand2")
        close_button.pack(pady=20)

    def confirm_exit(self):
        response = messagebox.askyesno("Exit", "Are you sure you want to leave?")
        if response:
            self.root.quit()  # Terminate the program if the user confirms


if __name__ == "__main__":
    root = tk.Tk()
    app = FrontEnd(root)
    root.mainloop()
