#!/bin/bash

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found. Please install it to run this script."
    exit 1
fi

# Set the counter for converted files
COUNT=0

# Loop through all files in the current directory ending with .flac (case-insensitive)
for file in *.[fF][lL][aA][cC]; do
    # Check if a file was found (in case no .flac files exist)
    if [ -e "$file" ]; then
        # Construct the output filename by replacing the extension
        output_file="${file%.flac}.wav"
        
        # Display the action
        echo "Converting: \"$file\" -> \"$output_file\""
        
        # Run the conversion using ffmpeg
        # -i: input file
        # -y: overwrite output file without asking (optional, can be removed)
        # -acodec pcm_s16le: specifies the WAV codec (16-bit PCM, standard for high-quality WAV)
        ffmpeg -i "$file" -y -acodec pcm_s16le "$output_file"
        
        # Check if the conversion was successful
        if [ $? -eq 0 ]; then
            COUNT=$((COUNT + 1))
        else
            echo "❗️ Error converting \"$file\"."
        fi
    fi
done

# Final status message
if [ $COUNT -eq 0 ]; then
    echo "✅ Conversion complete. No .flac files found or converted."
else
    echo "🎉 Conversion complete! $COUNT file(s) converted from FLAC to WAV."
fi