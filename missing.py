import glob

# Get all the files in the current directory
files = glob.glob("*.jpg")

img_set = set()
missing = []

# Loop through the files
for file in files:
    num = file.split("-")[0]
    num = int(num)

    img_set.add(num)

for i in range(1, 1682):
    if i not in img_set:
        missing.append(i)

# save the missing into a file
with open("missing.txt", "w") as f:
    for num in missing:
        f.write(str(num) + "\n")
