#!/usr/bin/python3
import math
import string
import sys
import yaml
import argparse

import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isfile(input_path):
    print(f'The path specified ({input_path}) does not exist')
    sys.exit()
print(f"Load music file {input_path}")

def print_page_header():
    print("""
    <!DOCTYPE html>
    <html>
    <head>
<style>


h4 {
  text-align: center;
}


table {
  border-collapse: separate;  
  border: none;
  
  align: center;
  margin-left: auto;
  margin-right: auto;
  width:1024px;  
}

table.figure {
  align: center;
  margin-left: auto;
  margin-right: auto;
  width:1024px;  
  font-style: italic;
}

spacer_div {
  line-height: 40px;
  border: none;
}

td {
  background-image: linear-gradient(45deg, lightblue, white);
  

  padding: none;
  font-size: 18px; 
  margin: none;
  
}

.td_no_bg {
  background-image: none;
  align: left;
  width: 50%;
}


div.line_separator {  
  height: 50px;
}

.container{
  width: 11%;
  height: 200px;
  position: relative;
  margin: none;
  padding:none;
      
}

.note_C1{  
  background-color: #fc0505;
  border:1px solid #000;
  border-radius:10%;    
  color:#000;
  display: inline-block;  
  height:10%;  
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;  
  text-align: center;
  top: 85%;
  width:80%;
}

.note_C1a{
  background-color: #fc0505;
  border:1px solid #000;
  border-radius:10%;    
  color:#000;
  display: inline-block;  
  height:10%;  
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;  
  text-align: center;
  top: 85%;
  width:35%;      
}

.note_C1b{  
  background-color: #fc0505;
  border:1px solid #000;
  border-radius:10%;    
  color:#000;
  display: inline-block;  
  height:10%;  
  margin-left: 55%;
  padding-bottom: 1%;
  position: absolute;  
  text-align: center;
  top: 85%;
  width:35%;      
}


.note_D2{
  background-color:#ff8b38;
  background-color:#e39402;
  border:1px solid #000;
  border-radius:10%;  
  color:#000;
  display: inline-block;
  height:10%;  
  margin-left: 8%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 75%;
  width:80%;
}

.note_D2a{
  background-color:#ff8b38;
  background-color:#e39402;
  border:1px solid #000;
  border-radius:10%;  
  color:#000;
  display: inline-block;
  height:10%;  
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 75%;
  width:35%;
}
.note_D2b{
  background-color:#ff8b38;
  background-color:#e39402;
  border:1px solid #000;
  border-radius:10%;  
  color:#000;
  display: inline-block;
  height:10%;  
  margin-left: 55%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 75%;
  width:35%;
}
.note_E3{
  background-color: #e3d002;
  background-color: #cccc00;
  border:1px solid #000;
  border-radius:10%;    
  color:#000;
  display: inline-block;
  height:10%;  
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 65%;
  width:80%;    
}

.note_E3a{
  background-color: #e3d002;
  background-color: #cccc00;
  border:1px solid #000;
  border-radius:10%;    
  color:#000;
  display: inline-block;
  height:10%;  
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 65%;
  width:35%;    
}
.note_E3b{
  background-color: #e3d002;
  background-color: #cccc00;
  border:1px solid #000;
  border-radius:10%;    
  color:#000;
  display: inline-block;
  height:10%;  
  margin-left: 55%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 65%;
  width:35%;    
}
.note_F4{
  background-color: #12d10f;
  border:1px solid #000;
  border-radius:10%;  
  color:#000;
  display: inline-block;
  height:10%;
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 55%;  
  width:80%;
}
.note_F4a{
  background-color: #12d10f;
  border:1px solid #000;
  border-radius:10%;  
  color:#000;
  display: inline-block;
  height:10%;
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 55%;  
  width:35%;
}
.note_F4b{
  background-color: #12d10f;
  border:1px solid #000;
  border-radius:10%;  
  color:#000;
  display: inline-block;
  height:10%;
  margin-left: 55%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 55%;  
  width:35%;
}

.note_G5{
  background-color:#9df8fc;
  border:1px solid #000;
  border-radius:10%;  
  color:#000;
  display: inline-block;
  height:10%;
  margin-left: 10%;
  padding-bottom: 1%;
  text-align: center;
  top: 45%;   
  width:80%;
  position: absolute;
}

.note_G5a{
  background-color:#9df8fc;
  border:1px solid #000;
  border-radius:10%;
  color:#000;
  display: inline-block;
  height:10%;
  margin-left: 10%;
  padding-bottom: 1%;
  text-align: center;
  top: 45%;   
  width:35%;
  position: absolute;
}

.note_G5b{
  background-color:#9df8fc;
  border:1px solid #000;
  border-radius:10%;
  color:#000;
  display: inline-block;
  height:10%;
  margin-left: 55%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 45%;   
  width:35%;  
}

.note_A6{
  background-color: #0b30b5;
  border:1px solid #000;
  border-radius:10%;
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

.note_A6a{
  background-color: #0b30b5;
  border:1px solid #000;
  border-radius:10%;
  color:#ffffff;
  display: inline-block;
  height:10%;
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 35%;       
  width:35%;
}

.note_A6b{
  background-color: #0b30b5;
  border:1px solid #000;
  border-radius:10%;
  color:#ffffff;
  display: inline-block;
  height:10%;
  margin-left: 55%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 35%;       
  width:35%;
}

.note_B7{
  background-color:#c284f5;  
  border:1px solid #000;    
  border-radius:10%;
  color:#000;
  display: inline-block;
  height:10%;
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 25%;   
  width:80%;         
 }

.note_B7a{
  background-color:#8d05fc;  
  border:1px solid #000;    
  border-radius:10%;
  color:#000;
  display: inline-block;
  height:10%;
  margin-left: 10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 25%;   
  width:35%;         
 }  

 .note_B7b{
  background-color:#b50bb2;  
  border:1px solid #000;    
  border-radius:10%;
  color:#000;
  display: inline-block;
  height:10%;
  margin-left: 55%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;
  top: 25%;   
  width:35%;         
 }  
.note_C8{
  background-color: #fc0505;
  border:1px solid #000;  
  border-radius:10%;
  color:#000;
  display: inline-block;  
  margin-left: 10%;
  height:10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;  
  top: 15%;   
  width:80%;      
}

.note_C8a{  
  background-color: #fc0505;
  border:1px solid #000;  
  border-radius:10%;
  color:#000;
  display: inline-block;  
  margin-left: 10%;
  height:10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;  
  top: 15%;   
  width:35%;      
}
.note_C8b{  
  background-color: #fc0505;
  border:1px solid #000;  
  border-radius:10%;
  color:#000;
  display: inline-block;  
  margin-left: 55%;
  height:10%;
  padding-bottom: 1%;
  position: absolute;
  text-align: center;  
  top: 15%;   
  width:35%;      
}
.note_REST{
  background-color:lightgray;
  border:1px solid lightgray;
  border-radius:10%;
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

line_num = 1
num_lines = 0
beats_per_bar = 0
bar_num = 0

def print_page_footer():
    print("</body>\n </html> ")


def print_table_title(title):
    print(f"<h4>{title} </h4>")


def cell_header():
    print("<td class=\"container\">")


def cell_footer():
    print("</td>")

def table_header():
    print("<table>")


def table_footer(bar_num):
    print(f"</table>")
    print(f"<table class=\"figure\"><tr><td class=\"td_no_bg\">Bar: {bar_num}</td><td class=\"td_no_bg\">Bar: {bar_num+1}</td></tr></table>")


def row_header():
    print("<tr>")


def row_footer():
    print("</tr>")


def print_bar(bar):
    for note in bar:
        cell_header()
        if type(note) == str:
            
            print("<span class =\"note_"+note+"\">"+note.translate(lc_stripper)+"</span>")

        else:
            for item in note:
                print("<span class = \"note_"+item+"\">"+item.translate(lc_stripper)+"</span>")

        cell_footer()


def print_table(music, offset, n):
    global line_num
    global bar_num      
    
    table_header()    
    for bar in music["bars"][offset:offset+n]:        
        if bar_num % 2 == 0:            
            row_header()
        print_bar(bar)
        if bar_num % 2 != 0:
            row_footer()            
        bar_num += 1       
       
    table_footer(bar_num-1)

def print_page_of_music(music, page_size, page_num):
    global line_num
    global num_lines
    global beats_per_bar
    bar_offset = (page_num - 1) * page_size
    
    print_table_title(f"{music['title']} (page {page_num})")
    print_table(music, bar_offset, page_size//2)    
    line_num += 1

    if line_num < num_lines:    
      print('<div class="line_separator"></div>')
      print_table(music, bar_offset + page_size//2, page_size//2)        
      line_num += 1
  

lc_stripper = str.maketrans('', '', string.ascii_lowercase)

#with open("music-frere-jacques.poly.yaml", 'r') as stream:
#with open("music-happy-birthday.poly.yaml", 'r') as stream:
with open(input_path, 'r') as stream:
    music = yaml.safe_load(stream)    
    page_size = 4
    beats_per_bar =  len(music["bars"][0])
    num_pages = math.ceil((len(music["bars"]) + page_size - 1 ) / page_size)
    num_lines = math.ceil(len(music["bars"]) /2 )
    

    for page_num in range(1, num_pages+1):        
        with open(f"page-{page_num}.html", "w") as sys.stdout:            
            print_page_header()
            print_page_of_music(music, page_size, page_num)
            print_page_footer()
            


