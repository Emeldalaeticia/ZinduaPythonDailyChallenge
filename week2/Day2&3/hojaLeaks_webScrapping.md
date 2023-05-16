Web Scraping from Hojaleaks

This code demonstrates web scraping from the website "https://hojaleaks.com/" using the BeautifulSoup library. The extracted data is then saved into a CSV file named "data.csv".

The code imports the necessary libraries: BeautifulSoup for parsing HTML, requests for making HTTP requests, and csv for writing data to a CSV file.

The url variable is set to "https://hojaleaks.com/".

The result variable uses the requests.get() method to send an HTTP GET request to the specified URL and retrieve the web page's content.

The doc variable creates a BeautifulSoup object by parsing the HTML content of the web page using "html.parser" as the parser.

The headings variable uses the find_all() method to extract all <h1> elements from the parsed document.

The summaries variable uses the find_all() method to extract all <p> elements with the class name "css-ko0c54" from the parsed document.

The code iterates over each heading in headings and prints the text of each heading.

Similarly, the code iterates over each summary in summaries and prints the text of each summary.

The code then opens the file "data.csv" in write mode using the open() function and creates a csv.writer object.

The first row of the CSV file is written with the column headers 'Heading' and 'Summary' using the writer.writerow() method.

Using a for loop and the zip() function, the code iterates over corresponding elements of headings and summaries simultaneously. It writes each heading and summary as a row in the CSV file using the writer.writerow() method.

This code showcases how to scrape data from the Hojaleaks website, printing the extracted headings and summaries, and storing them in a CSV file for further analysis or processing