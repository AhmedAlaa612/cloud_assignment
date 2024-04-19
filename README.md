
# Word frequency counter

A Python script that does the following 

- Read the contents of the "paragraphs.txt" file.
- Remove stop words from the text using NLTK library.
- Count the frequency of each word in the processed text.
- Display the top 100 frequent words and their frequencies.


The application is containerized using a Dockerfile for easy deployment and execution.





## Usage

1. build the container 
```javascript
docker build -t cloud_assignment:1.0 .
```
2. run the container
```javascript
docker run cloud_assignment:1.0
```

