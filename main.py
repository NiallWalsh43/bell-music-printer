import yaml

with open("demo.yaml", 'r') as stream:
    music = yaml.safe_load(stream)

music0 = {

    "title": "Twinkle Twinkle Little Star",


    "bars": [
      ["C1", "C1", "G5", "G5"], ["A6", "A6", "G5", "rest"],
      ["F4", "F4", "E3", "E3"],  ["D2", "D2", "C1", "rest"],
      ["G5", "G5", "F4", "F4"], ["E3", "E3", "D2", "rest"],
      ["G5", "G5", "F4", "F4"], ["E3", "E3", "D2", "rest"],
      ["C1", "C1", "G5", "G5"], ["A6", "A6", "G5", "rest"],
      ["F4", "F4", "E3", "E3"], ["D2", "D2", "C1", "C8"],
    ]
}


def print_page_header():
    print("""
    <html>
    <head>
<style>


h2 {
  text-align: center;
}


table {
  border-collapse: separate;  
  border-spacing:0 50px;
  align: center;
  margin-left: auto;
  margin-right: auto;
}

td {
  background-image: linear-gradient(.25turn, lightgray 10%, white);
  border-bottom: solid 1px black;
  border-top: solid 1px black;

  padding: 10px;
  font-size: 30px; 
}

td:nth-child(1) {
  border-left: solid 2px black;
}

td:nth-child(5) {
  border-left: solid 2px black;
}

td:nth-child(8) {
  border-right: solid 2px black;
  
.shapes-wrapper { 
  position:absolute;
  top: 50px;
  left: 50px;
  width: 200px;
  height: 200px;
  background-color: yellow;
}
  
}
.note_C1{
  background-color:#b71c1c;
  display:block;
  height:10px;
  width:10px;
  border-radius:50%;
  border:3px solid #000;
  margin:auto;
  color:#000;
  line-height:50px;
  text-align:center
  
}

.note_D2{
  background-color:#dc7633;
  display:block;
  height:10px;
  width:10px;
  border-radius:50%;
  border:3px solid #000;
  margin:auto;
  line-height:50px;
  text-align:center
  
}

.note_E3{
  background-color:#f1c40f;
  display:block;
  height:10px;
  width:10px;
  border-radius:50%;
  border:3px solid #000;
  margin:auto;
  color:#000;
  line-height:50px;
  text-align:center  
}


.note_F4{
  background-color:#558b2f;
  display:block;
  height:10px;
  width:10px;
  border-radius:50%;
  border:3px solid #000;
  margin:auto;
  color:#000;
  line-height:50px;
  text-align:center  
}

.note_G5{
  background-color:#1abc9c;
  display:block;
  height:10px;
  width:10px;
  border-radius:50%;
  border:3px solid #000;
  margin:auto;
  color:#0;
  line-height:50px;
  text-align:center
  
}
.note_A6{
  background-color:#1f618d ;
  display:block;
  height:10px;
  width:10px;
  border-radius:50%;
  border:3px solid #000;
  margin:auto;
  color:#0;
  line-height:50px;
  text-align:center
  
}

.note_B7{
  background-color:#6c3483 ;
  display:block;
  height:10px;
  width:10px;
  border-radius:50%;
  border:3px solid #000;
  margin:auto;
  color:#0;
  line-height:50px;
  text-align:center
 
 }
  
.note_C8{
  background-color: #b71c1c;
  display:block;
  height:10px;
  width:10px;
  border-radius:50%;
  border:3px solid #000;
  margin:auto;
  color:#0;
  line-height:50px;
  text-align:center
  
}
.note_rest{
  background-color:lightgray;
  display:block;
  height:50px;
  width:50px;
  border-radius:50%;
  border:3px solid lightgray;
  margin:auto;
  color:gray;
  line-height:50px;
  text-align:center
  
}


</style>
</head>
    <body>
    """)


def print_page_footer():
    print("</body>\n </html> ")


def print_title(title):
    print(f"<h2>{title} </h2>")


def cell_header():
    print("<td>")


def cell_footer():
    print("</td>")


def table_header():
    print("<table border=1>")


def table_footer():
    print("</table>")


def row_header():
    print("<tr>")


def row_footer():
    print("</tr>")


def print_bar(bar):
    for note in bar:
        cell_header()
        if type(note) == str:
            print("<span class =\"note_"+note+"\">"+note+"</span>")

        else:
            for item in note:
                print("<span class = \"note_"+item+"\">"+item+"</span>")

        cell_footer()


def print_table(bars):
    bar_num = 0
    table_header()

    for bar in bars:
        if bar_num % 2 == 0:
            row_header()
        print_bar(bar)
        if bar_num % 2 != 0:
            row_footer()
        bar_num += 1

    table_footer()


print_page_header()
print_title(music["title"])
print_table(music["bars"])

print_page_footer()
