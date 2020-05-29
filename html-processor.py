import re

with open("C:/Users/Harrys/Desktop/Lab/Metaglvthstes/E2/testpage.txt", "r", encoding="utf-8") as fd0:
    text = fd0.read()

    #1 - Eksagwgh kai ektiposh tou Title
    repx = re.compile(r"<title>(.+?)</title>")
    m = repx.search(text)
    print(m.group(1))

    #2 - Apalhfh twn sxoliwn
    repx2 = re.compile(r"<!.+?>")
    text_01 = repx2.sub("", text)

    #3 - Apalhfh <script> </style>
    repx3 = re.compile(r"(<script.+?</script>)|(<style.+?</style>)")
    text_02 = repx3.sub("",text_01)

    #4 - Eksagwgh kai print tou <a>
    repx4 = re.compile(r"<a(.+?)</a>")
    for m in repx4.finditer(text_02):
      print(m.group(1))

    #5 - Apalhfh twn tags
    repx5 = re.compile(r"<.+?>")
    text_03 = repx5.sub("", text_02)

    #Entities
    HTMLentities = {"&amp;": "&", "&gt;": ">", "&lt;": "<", "&nbsp;": " "}

    #6 - Callback function gia thn metatroph twn html Entities
    def rep1(m):
        if m.group(1) == "&amp;":
            return HTMLentities[m.group(1)]
        elif m.group(1) == "&gt;":
            return HTMLentities[m.group(1)]
        elif m.group(1) == "&lt;":
            return HTMLentities[m.group(1)]
        elif m.group(1) == "&nbsp;":
            return HTMLentities[m.group(1)]


    repx6 = re.compile(r"(&amp;|&gt;|&lt;|&nbsp;)")
    new_text4 = repx6.sub(rep1,text_03)

    #7 - Metatroph whitespace se keno
    repx7 = re.compile(r"\s+")
    new_text5 = repx7.sub(" ",new_text4)

    #8 - print keimenou
    print(new_text5)
