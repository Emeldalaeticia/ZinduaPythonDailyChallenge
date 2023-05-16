Web Scraping from The New York Times

This code illustrates web scraping from the website "https://www.nytimes.com/" using the BeautifulSoup library. The extracted data, including article titles and descriptions, is then saved into a CSV file named "nytimes.csv".

The code imports the necessary libraries: requests for making HTTP requests, BeautifulSoup for parsing HTML, and csv for writing data to a CSV file.

The url variable is set to 'https://www.nytimes.com/'.

The response variable uses the requests.get() method to send an HTTP GET request to the specified URL and retrieve the web page's content.

The soup variable creates a BeautifulSoup object by parsing the HTML content of the web page using "html.parser" as the parser.

The articles variable uses the find_all() method to extract all <div> elements with the class name "css-xdandi" from the parsed document, representing the articles on the page.

An empty list named data is created to store the extracted article information.

The code opens the file "nytimes.csv" in write mode using the open() function and creates a csv.writer object named csv_writer.

The first row of the CSV file is written with the column headers 'title' and 'description' using the csv_writer.writerow() method.

Using a for loop, the code iterates over the first 10 articles in the articles list.

For each article, it finds the title using the find() method and the class name "css-on971e", and the description using the find() method and the class name "css-9lwb1u".

If both the title and description are found, a dictionary with the 'title' and 'description' as keys and their corresponding values is appended to the data list.

The article is printed using the print() function.

The title and description of each article are written as a row in the CSV file using the csv_writer.writerow() method.

This code demonstrates how to scrape data from The New York Times website, extracting article titles and descriptions, and storing them in a CSV file for further analysis or processing