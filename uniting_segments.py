import os

output_file = "downloads/full_video.ts"
segment_count = 260

with open(output_file, "wb") as outfile:
    for i in range(1, segment_count + 1):
        segment_file = f"downloads/segment_{i}.ts"
        if os.path.exists(segment_file):
            with open(segment_file, "rb") as infile:
                outfile.write(infile.read())
        else:
            print(f"Warning: {segment_file} not found, skipping...")

print(f"All segments joined in {output_file}")
