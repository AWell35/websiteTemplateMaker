import os
from os import path
def main():
    project = input("Enter your project name: ")
    location = input("Enter your projects file location(e.g C:file/file/file): ")

    projectDir = f"{location}/{project}"
    try:
      if os.path.exists(projectDir):
          print("This project file exisits! Try a different name or location")
      else:
        os.makedirs(projectDir)
        os.chdir(projectDir)
        os.makedirs("pages")
        os.makedirs("css")
        os.makedirs("images")
        os.makedirs("scripts")
        stylesheet = open("css/stylesheet.css", "x")
        stylesheet.close()
        script = open("scripts/script.js","x")
        script.close()
        index = open("index.html", "x")    
        index.write(f"{getTemplate(project)}")
        index.close()
        
    except:
      print("invalid input")

def getTemplate(projectName):
  indexInfo = f"""
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>{projectName}</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <script src="index.js"></script>
  </body>
</html>
"""
  return indexInfo

if __name__ == "__main__":
    main()