import requests

base_url = ""

max_segments = 1000
segment_files = []

for i in range(202, max_segments + 1):
    url = base_url.format(i)
    print(f"Downloading the segment {i}...")

    r = requests.get(url)
    if r.status_code != 200 or len(r.content) < 1000:
        print("Segment not found or empty, halting download.")
        break

    filename = f"downloads/segment_{i}.ts"
    with open(filename, "wb") as f:
        f.write(r.content)
    segment_files.append(filename)

print(f"{len(segment_files)} segments downloaded.")

with open("video_completo.ts", "wb") as outfile:
    for fname in segment_files:
        with open(fname, "rb") as infile:
            outfile.write(infile.read())

print("All the segments have been merged into the ’full_video.ts’ file.")
