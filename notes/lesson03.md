#Lesson 2: Data Wrangling

Welcome to the second lesson of Introduction to Data Science
In the first lesson, we discussed data science at a high level
So we talked about the skills that a data scientist usually has, and also some of the problems that you can solve using data science
One of the most important skills that a data scientist can have, is the ability to extract and clean data
This is usually referred to as data wrangling or data munching
Believe it or not, some data scientists say that they can spend up to 70% of their time data wrangling
This may sound crazy to you, but it's not hard to imagine this happening
Let's say you have some really cool analysis project that you want to do
Say, look at a variety of factors, and figure out why the life expectancy in City A is higher than City B
Well okay, let's say that all this data lives on a website
So, you write some scripts to go and pull this data from the website
Great, but then you need somewhere to store the data, so you're going to need a database
So okay, we, we use a database, we store all the data there
And then you look at the data and you realize, oh wait, there are a bunch of missing values, or a bunch of this data looks weird
So you need to develop some, some method to take all this data and clean it up
This is data munching
And all of this is necessary if we want to answer our original really cool question
Why is the life expectancy in city A, higher than the life expectancy in city B? In this lesson, we'll discuss data munching basics using 3 data sets
One containing information on a bunch of baseball players, called the Lawmen baseball database
Another containing information on enrollments in an Indian identification program called Aadhar, and also data from the last FM API
Using these 3 data sets, we're going to discuss the formats that data can come in, how you can acquire data from these various data sources, and also how to inspects the data and see if it might have any missing or erroneous values
Alright, well let's get started


## Nick: Introduction

Hello, my name is Nick Gustafson, and I'm a data scientist at Udacity
 My background is I did my undergrad in neurobiology and I went on in graduate school to continue studying neurobiology, and neuroscience in particular, and kind of, computational neuroscience and looking at algorithmic And all mechanisms of learning and decision making
 And while towards that, hm, tail end of my graduate work I, eventually kind of realized I did not want to stay in academia, however I still have this kind of strong passion for analyzing data, modeling data, understanding You know, patterns within it, and kind of, you know, applying scientific methods, and data science just, just felt like a natural progression from there

## What is Data Wrangling?

--------------------------------
| Playa | Position | L/R | Avg |
--------------------------------

You may ask yourself, what is data munching? Let's work through an example and demonstrate the concept to you
 Imagine we're trying to figure out if right handed or left handed baseball players have a higher batting average and we're given this table of data to answer the question
 Let's look at the table
 Look, this value is incorrect
 You can't have a batting average greater than 1,000
 Also, it looks like we don't have any left or right-handedness for Ichiro Suzuki
 Data wrangling is the art of dealing with and or converting missing or ill-formatted data into a format that more easily lends itself to analysis
 But before we can do that analysis, we first have to get the data that we want to analyze
 Three of the most common sources from which can get data are from files, from a database, or from websites through web APIs
 We'll cover all three of these in this lesson


## Analyzing Messy Data 1

Before diving into the nitty-gritty details of data munching, I want to ask if
you've ever had to analyze really messy or unorganized data? Even if you're not
a data scientist, you've probably dealt with unwieldy data at some point in
your life
 Maybe you had trouble reading the receipts from a bake sale you organized, or
 you tried to keep track of your personal budget in an Excel spreadsheet
  What methods or tools did you use to make your life easier? Please share your
  experience with the class by typing your answer in the forum
   I've added a link to the discussion thread for you in the instructor
   comments


## Analyzing Messy Data 2
By now you've realized that data is often messy and unorganized
 Because of that, a large amount of a data scientist's time is spent extracting and cleaning the data that they will use to perform analyses or make visualizations
 Let's get our feet wet and first discuss the various ways that we might load our data
 If we want to programmatically process and analyze our data, it's very important to understand the structure of the data itself


# Nick's Experience with Data Wrangling

The did it, that also will, depend on the project &gt;&gt; Say that one more time
 &gt;&gt; On average, over 50% of the time it's just kind of
 Well, maybe be spent like, combing through the data and like just, figuring out maybe idiosyncrasies in it
 And You know
 You quickly apply an algorithm, you look at it
 You don't get the results you expect, so you dig in a little closer and like see that there are these weird little kind of edge cases that are, are ending up more prominent in your data than you previously expected
 So, you have to go back and scrape and comb through it again, and it's just this iterative back-and-forth process

## Acquiring Data

Often acquiring data to do analysis doesn't require any particularly fancy methodology
 It's just a matter of finding the right file somewhere on the internet and downloading it
 A lot of the data that exists out there, particularly on government websites, is stored in text files
 For example, let's say we wanted to get a database of all major league baseball statistics
 I kind find this data at http://www
SeanLahman
com/baseballarchives/statistics
 If I visit this website, I can see that the data I want is available in a variety of formats
 A comma delimited or CSV version, but also a Microsoft Access version, and a SQL version

## Common Data Formats

Three of the most common data formats are CSV, XML, and JSON
 I want to quickly discuss what one record in the Lahman Baseball Database would look like in each of these different formats
 It just so happens that the first row in this data set corresponds to a pretty famous baseball player
 Hank Aaron
 Let's first discuss what this data looks like in the format we originally downloaded it in, CSV
 In the CSV format we usually have a series of rows
 With each row corresponding to an entry
 There is a header row at the top of our file
 Where our comma separated values do not correspond to an entry but instead tell us what each entry means for the rest of the document
 In the case of this baseball document, our first row tells us that every row will have some identifiers, the Lahman ID
 The player ID, the manager ID, et cetera
 Then we'll see birth year, birth month, birth day and then a bunch of other statistics
 If we go and look at the entry for Hank Aaron
 We see all of these values, 1 for Lahman ID, aaronha01 for player ID, et cetera, separated by commas
 Note that if a particular player doesn't have a value for one field, for example Hank Aaron does not have a manager ID, we simply see two commas in a row
 In the case of an XML document, we end up with something that pretty closely resembles HTML
 We can have a document element, which is opened
 It can then have a series of tables, which are also opened, as we see here
 The table has a number of children, which correspond to the values that we just discussed in the CSV 1 for Lahman ID, aaronha01 for player Id, etc
 Note that when we're missing a value in XML, things are treated a bit differently
 For example, since Hank Aaron was not a manager, we just open the manager ID field and then put a slash at the end
 Finally, for a JSON document, we have a number of JSON objects indicated by these curly braces
 A JSON object looks a lot like a Python dictionary
 We have keys
 Which correspond to what we would see in the header row in a CSV file followed by values
 Note that in the case of a missing value, we simply open and close the quotation marks
 Oftentimes, the benefit of XML or JSON is that they support nested structures in a way that CSV documents cannot
 I don't want to go into this in great detail, but you can imagine that the value corresponding to a particular JSON key, say braves, could itself be another JSON object
 Here's what that might look like
 One final note, is to remember that when we talk about different formats that data can come in, it's not a matter of the file extension being 
CSV or being 
JSON
 A file format really has to do with how the data is organized inside of a file
 So we could easily have data that is formatted in JSON or CSV, but that comes in a file whose extension is 
txt
 Since the online MTA subway data comes in CSV format, in the weather underground API responds to requests with a JSON object
 We'll discuss how to load and process files in these two formats
 While we won't explicitly discuss loading and processing XML files, it isn't that different than the material will cover with regards to JSON and CSV
 If you'd like to learn more about dealing with XML data in particular
 I recommend you take the data wrangling class with Mongo DB taught here at Udacity
 For now, let's discuss how to work with CSV files

