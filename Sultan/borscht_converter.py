import base64
import re
from glob import glob
from time import sleep
import os
import zipfile
import PIL
from PIL import Image

link = "300x250.mp4"
f = "300x250.html"


def zip(src="fb-300x250.html", dst="archive.zip"):
    import shutil

    zipOutputName = dst
    fileType = "zip"
    path = "./"
    fileName = src

    shutil.make_archive(zipOutputName, fileType, path, fileName)


def resize_image(link):
    baseheight = 113
    img = Image.open(link)
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    img.save(link)


def get_base64(link, form="gif"):
    print(link)
    try:
        with open(link, "rb") as f:
            if form == "png":
                return (b"data:image/png;base64," + base64.b64encode(f.read())).decode("utf-8")
            elif form == "jpg":
                return (b"data:image/jpg;base64," + base64.b64encode(f.read())).decode("utf-8")
            elif form == "gif":
                return (b"data:image/gif;base64," + base64.b64encode(f.read())).decode("utf-8")
            elif form == "mp4":
                return (b"data:video/mp4;base64," + base64.b64encode(f.read())).decode("utf-8")
            elif form == "svg":
                return (b"data:image/svg+xml;base64," + base64.b64encode(f.read())).decode("utf-8")
            else:
                return b"".decode("utf-8")
    except FileNotFoundError:
        return ""



def change_files_by_format(text, f):

    file_content = text

    def replace(m):
        return m.group()[0] + get_base64(m.group().strip("\"\'"), f) + m.group()[0]

    template = '"([\./]*[^\"\.]+\.'+ f.lower() +')"'
    file_content = re.sub(template, replace, file_content)

    template = "\'([\./]*[^\']+" + f.lower() + ")\'"
    file_content = re.sub(template, replace, file_content)

    return file_content
    

def include_external_files(text):
    def get_file_content(link):
        with open(link, encoding="utf-8") as f:
            return "\n"+f.read()+"\n"

    def replace_js(m):
        return "<script>"+get_file_content( re.findall("\"[^\"]+\"", m.group())[0].strip("\"\'") )+"</script>"

    def replace_css(m):
        return "<style>"+get_file_content( re.findall("href=(\"[^\"]+\")", m.group())[0].strip("\"\'") )+"</style>"

    text = re.sub("<script src=\"(.+)\"></script>", replace_js, text)
    return re.sub("<link[^>]*href=\"(.*)\"[^>]*>", replace_css, text)


def get_fb(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read()

    text = include_external_files(text)

    for f in ["png", "gif", "jpg", "mp4", "svg"]:
        text = change_files_by_format(text, f)

    with open(os.path.dirname(__file__)+"-borscht-"+filename, "w", encoding="utf-8") as f:
        f.write(text)
    # zip("g-"+filename, "g-"+filename)



if __name__ == "__main__":
    # pass
    get_fb("index.html")
    # start()

