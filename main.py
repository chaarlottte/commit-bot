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
    for x in range(10):
        editFile()
        commit()
        time.sleep(1)
    os.system("git push")