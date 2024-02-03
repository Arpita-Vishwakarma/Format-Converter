from pydub import AudioSegment
import os

def convert_aac_to_aiff(input_file):
    # Generate output file path
    output_file = os.path.splitext(input_file)[0] + "_converted.aiff"

    # Load AAC file using pydub
    audio = AudioSegment.from_file(input_file, format="aac")

    # Convert audio to AIFF
    audio.export(output_file, format="aiff")

    print(f"Conversion complete. Output file: {output_file}")

if __name__ == "__main__":
    # Provide the path to your AAC file
    input_aac_file = r"sample1.aac"

    # Check if the file exists before conversion
    if os.path.exists(input_aac_file):
        # Convert AAC to AIFF
        convert_aac_to_aiff(input_aac_file)
    else:
        print("Error: File not found -", input_aac_file)
