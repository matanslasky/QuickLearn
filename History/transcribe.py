# create a program that requests an input file in format of mp3 or mp4 and feeds it to the whisper api in order to create a transcription and saves the results in a new file
import os
import whisper
import ffmpeg

def transcribe_audio(input_file, output_file):
    # Load the Whisper model
    model = whisper.load_model("base")

    # Load the input audio file
    audio = whisper.load_audio(input_file)

    # Transcribe the audio
    result = model.transcribe(audio)

    # Save the transcription results to a new file
    with open(output_file, "w") as f:
        f.write(result["text"])

    print(f"Transcription saved to: {output_file}")

def main(path):
    # Get the input file from the user
    input_file = path
  #  input_file = input("Enter the path to the input audio file (MP3 or MP4): ")

    # Check the file extension and convert to WAV if necessary
    if input_file.endswith(".mp3"):
        wav_file = os.path.splitext(input_file)[0] + ".wav"
        (
            ffmpeg
            .input(input_file)
            .output(wav_file)
            .run()
        )
        input_file = wav_file
    elif input_file.endswith(".mp4"):
        wav_file = os.path.splitext(input_file)[0] + ".wav"
        (
            ffmpeg
            .input(input_file)
            .output(wav_file)
            .run()
        )
        input_file = wav_file

    # Get the output file name
    output_file = os.path.splitext(input_file)[0] + "_transcription.txt"
    print(output_file)
    # Transcribe the audio and save the results
    transcribe_audio(input_file, output_file)

if __name__ == "__main__":
    main()
