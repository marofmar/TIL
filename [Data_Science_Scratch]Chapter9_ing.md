# Data Science from Scratch
# Chapter 9
# Getting Data

> In order to be a data scientist you need data. 
> In fact, as a data scientists you will spend an embarrasingly large fraction of your time acquring, clearning, and transforming data. 
> In a pinch, ou can always tyep the data in yourself (or if you have minions make them do it), but usually this is not a good use of your time. 
> In this chapter, we'll look at different ways of getting data into Python and into the right format.

## stdin and stdout

* *Pipe* data through the Python commmand line, using 'sys.stdin' and 'sys.stdout'.

~~~
import sys, re

# sys. argv is the list of command-line arguments
# sys.argv[0] is the name of the program itself
# sys.argv[1] will be the regex specified at the command line
regex = sys.argv[1]

# for every line passed into the script
for line in sys.stdin:
    # if it matches the regex, write it to stdout
    if re.search(regex, line):
        sys.stdout.write(line)
~~~

* The | is the pipe character, which means "use the output of the left command as the input of the right command."

* The one that counts the lines it receives and then writes out the count

```import sys
        count = 0
        for line in sys.stdin:
            count += 1

    print count
```

* In Windows,
~~~
type SomeFile.txt | python egrep.py "[0-9]" | python line_count.py
~~~

~~~
```# most_common_words.py
import sys
from collection import Counter
```
```# pass in number of ords as first argument
try:
    num_words = int(sys.argv[1])
except:
    print "usage: most_common_words.py num_words"
    sys.exit(1) # non-zero exit code indicates error
    
counter = Counter(word.lower()
                  for line in sys.stdin
                  for word in line.strip().split()
                  if word)

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.wrtie("\t")
    sys.stdout.wrtie(word)
    sys.stdout.write("\n")
    
    

## Reading Files
> You can also explicitly read from and write to files directly in your code. Python makes working with files pretty simple.

## The Basics of Text Files
* THe first step, to obtain a *fiel object* using ```open```:
    file_for_reading = open('reading_file.txt', 'r')
    file_for_writing = open('writing_file.text', 'w')
    file_for_appending = open('appending_file.txt', 'a')
    
    file_for_writing.close()
    
* Since it is easy to forget to close the file, it is recommended to use them in a ```with``` block, at the end of which they will be closed automatically.
    with open(filename, 'r') as f:
        data = function_that_gets_data_from(f)
    process(data)
    

> If you need to read a whole text file, you can just iterate over the lines of the file using ```for```

    starts_with_hash = 0
    with open('input.txt','r'r) as f:
        for line in file:
            if re.match("^#", line):
                starts_with_hash += 1
                
> Every line you get this way ends in a newline character, so you will often want to ```strip()``` it before doing anything with it.

    def get_domain(email_address):
        """ split on '@' and retrun the last piece"""
        return email_address.lower().split("S")[-1]
    
    with open('email_addresses.txt', 'r') as f:
        domain_counts = Counter(get_domain(line.strip())
                                for line  in f
                                if "@" in line)
                                

## Delimited Files

> The hypothetical email addresses file that we just processed had one address per line. More frequently you'll work with files with lots of data on each line. These files are very often either *comma-separated* or *tab-separated*. 
> Each line has several fields, with a comma (or a tab) indicating where one filed ends and the next field starts.

> This starts to get complicated when you have filed with commas and tabs and newlines in them (which you inevitably do). 
> For this reason, it's pretty much always a mistake to try to parse them yourself. Instead, you should use Python's ```csv``` moduel (or the ```pandas``` library).

> For technical reasons that you should feel free to blame on Microsoft, you should always work with ```csv``` files in *binary* mode by including a *b* after the *r* or *w*.

* If the file has no headers ( which means you probably want each row as a ```list```, and which places the burden on you to know what's in each column), you can use ```csv.reader``` to iterate over the rows, each of which will be an appropriately split list.
POJ
    import csv
    with oepn('tab_delimited_stock_prices.txt', 'rb') as f:
        reader = csv.reader(f, delimiter = '\t')
        for row in reader:
            data = row[0]
            symbol = row[1]
            closing_price = float(row[2])
            process(data, symbol, closing_price)
            
   with open('colon_delimited_stock_prices.txt', 'rb') as f:
       for row in reader:
           data = row["date"]
           symbol = row["symbol"]
           closing_price = float(row["closing_price"])
           process(date, symbol, closing_price)
           
* Even if your file doens't have headers you can still use ```DictReader``` by passing it the keys as a ```filednames``` parameter.



## Scraping the Web
> Anothe rway to get data is by scraping it from web pages. Fetching web pages, it turns out, is pretty easy; getting meaningful structured infromation out of them less so.

## HTML and the Prsing Thereof

* Pages on the WEb are wrtten in HTML, in which text is (ideally) marked up into elements and their attributes.

* To get data out of HTML, we will use the *BeautifulSoup library*, which builds a tree out of the various elements on a web page and provides a simple interface for accessing them. 

    pip install beautifulsoup4
    
* We will also using the *requests library (```pip install requests```), which is a much nicer way of making HTTP request than anything that's built into Python.

*  Python's built-in HTML parser is not that lenient, which means that it doesn't always cope well with HTML that's not perfectly formed. 

* For that reason, we will use a different parser, which we need to install 

    pip install html5lib
    
* To use Beautiful Soup, we will need to pass some HTML into the ```BeautifulSoup()``` function. 

    from bs4 import BeautifulSoup
    import requests
    html = requests.get("http://www.example.com").text
    soup = BeautifulSoup(html, 'html5lib')
    
* We will typically work with ```Tag``` objects, which correspond to the tags representing the structure of an HTML page.


* For example, to fine the first <p> tag ( and its contents) you can use:
    first_paragraph = soup.find('p')    # or just soup.p
    
* You can get the text contents of a Tag using its text property:
    first_paragraph_text = soup.p.text
    first_praragraph_words = soup.p.text.split()
    
* And you can extract a tag's attributes by treating it like a dict:
    first_paragraph_id = soup.p['id']
    first_paragaph_id2 = soup.p.get('id') 
    
* You can get multiple tags at onece:
    all_paragraphs = soup.find_all('p')
    praragraphs_with_ids = [p for p in soup('p) if p.get('id')]
    
* Frequently you'll want to find tags with a specific class:
    important_paragraphs = soup('p', {'class': 'important'})
    important_paragraphs2 = soup('p', 'important')
    important_paragraphs3 = [p for p in soup('p')
                             if 'important' in p.get('calss', [])]
                             

## Example: O'Reilly Books About Data

* Check some sort of *access policy*
* Check for a *robosts.txt* file that tells webcrawlers how to behave.

    Crawl-dealy: 30
    Request-rate: 1/30
    > The first teslls us that we should wait 30 seconds between requests. 
    > The second that we should only request one page every 30 seconds. 
        
> To figure out how to extract the data,let's download one of thoses pages and feed it to Beautiful Sou:

    # you don't have to split the url like this unless it need to fit in a book
    url = "http://shop.oreilly.com/category/browse-subjects/" + "data.do?sortby=publicationsDate&page=1"
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')
    
    
    
    