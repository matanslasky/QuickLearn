from transformers import pipeline
import tkinter as tk



def summarize_text(input_file, output_file):
    # Load the summarization pipeline
    summarizer = pipeline("summarization")

    # Read the input text file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    

    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)

    # Write the summary to the output text file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(summary[0]['summary_text'])

def main(path):
    input_file = path  # Replace with your input file path
    output_file = 'summary.txt'  # Replace with your output file path
    summarize_text(input_file, output_file)


if __name__ == "__main__":
    main()
