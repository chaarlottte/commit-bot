import os, datetime, time

fileContent = """
# Commit Bot by chaarlottte

Last commit: """

fileName = "README.md"

def editFile():
    datetimeStr = datetime.datetime.now().strftime("%c")
    with open(fileName, "w") as f:
        f.write(fileContent + datetimeStr)
        f.close()

def commit():
    datetimeStr = datetime.datetime.now().strftime("%c")
    os.system("git add .")
    os.system(f"git commit -m \"{datetimeStr}\"")

def main():
    x: int = 0
    while True:
        editFile()
        commit()
        if x % 100 == 0: os.system("git push")
        # time.sleep(1)
        x += 1

if __name__ == "__main__":
    main()