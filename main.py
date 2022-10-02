import yaml

with open("demo.yaml", 'r') as stream:
    music = yaml.safe_load(stream)

# border-spacing:0 50px;
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
  border: none;
  
  align: center;
  margin-left: auto;
  margin-right: auto;
  width:1024px;
  grid-row-gap: 20px;
  row-gap: 20px;
}

tr {
  grid-row-gap: 20px;
  row-gap: 20px;
}
td {
  background-image: linear-gradient(45deg, lightblue, white);
  

  padding: none;
  font-size: 18px; 
  
}

td:nth-child(1) {
  border-left: solid 2px black;
  border-bottom: solid 2px black;
  border-top: solid 2px black;
}
td:nth-child(2) {  
  border-bottom: solid 2px black;
  border-top: solid 2px black;
}

td:nth-child(3) {  
  border-bottom: solid 2px black;
  border-top: solid 2px black;
}

td:nth-child(4) {  
  border-bottom: solid 2px black;
  border-top: solid 2px black;
  border-right: solid 2px black;
}

td:nth-child(5) {
  border-left: solid 2px black;
  border-bottom: solid 2px black;
  border-top: solid 2px black;
}
td:nth-child(6) {  
  border-bottom: solid 2px black;
  border-top: solid 2px black;
}

td:nth-child(7) {  
  border-bottom: solid 2px black;
  border-top: solid 2px black;
}

td:nth-child(8) {  
  border-bottom: solid 2px black;
  border-top: solid 2px black;
  border-right: solid 2px black;
}

.container{
  width: 11%;
  height: 200px;
  position: relative;
  margin: none;
  padding:none;
  
  
  
  
}

.note_C1{
  background-color:#b71c1c;
  border:1px solid #000;
  border-radius:45%;    
  color:#ffffff;
  display: inline-block;  
  height:10%;  
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;  
  text-align: center;
  top: 85%;
  width:80%;      
}

.note_D2{
  background-color:#b5490b;
  border:1px solid #000;
  border-radius:45%;
  color:#ffffff;
  display: inline-block;
  height:10%;  
  margin-left: 8%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 75%;
  width:80%;
}

.note_E3{
  background-color: #b5b50b; 
  border:1px solid #000;
  border-radius:45%;  
  color:#ffffff;
  display: inline-block;
  height:10%;  
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 65%;
  width:80%;    
}

.note_F4{
  background-color: #12d10f;
  border:1px solid #000;
  border-radius:45%;
  color:#ffffff;
  display: inline-block;
  height:10%;
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 55%;  
  width:80%;
}

.note_G5{
  background-color:#0bb5af;
  border:1px solid #000;
  border-radius:45%;
  color:#ffffff;
  display: inline-block;
  height:10%;
  margin-left: 10%;
  padding-bottom: 1%;
  text-align: center;
  top: 45%;   
  width:80%;
  position: absolute;
}

.note_A6{
  background-color: #0b30b5;
  border:1px solid #000;
  border-radius:45%;
  color:#ffffff;
  display: inline-block;
  height:10%;
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 35%;       
  width:80%;
}

.note_B7{
  background-color:#b50bb2;  
  border:1px solid #000;    
  border-radius:45%;
  color:#ffffff;  
  display: inline-block;
  height:10%;
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 25%;   
  width:80%;         
 }
  
.note_C8{
  background-color: #b71c1c;
  border:1px solid #000;  
  border-radius:40%;
  color:#ffffff;    
  display: inline-block;  
  margin-left: 10%;
  height:10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;  
  top: 15%;   
  width:80%;    
  
}

.note_rest{
  background-color:lightgray;
  border:1px solid lightgray;
  border-radius:45%;
  color:gray;    
  display:block;
  height:10%;      
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;    
  text-align: center;
  width:80%;
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
    print("<td class=\"container\">")


def cell_footer():
    print("</td>")


def table_header():
    print("<table>")


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
