# TopK

## Plan
- &#x2611; Implement file change detection
- &#x2611; Implement read of highest K in file
- &#x2611; Implement store of result
- &#x2611; Use results to calculate input K
- &#x2611; Create a web server to handle input K and return the result
- &#x2610; Asynchronous web response with loading spinner when K processing
- &#x2610; Give access to all K result
- &#x2610; Detect what are the changes in input file to only procces them
- &#x2610; Unit test

## Implementations Choice
- Python to handle file processing as python as ready module to do it and it .Flask to provide a small web server (Flask can be review as i use it only to provide a way for entering K)
- Use of heapq help to improve memory performance as it does not increase the memory needs when the number of k or the size of input file increase

## Limitations
- the first processes of K can take time so if there is regular change the implementation will have poor performance as it will always process the input file
- It only works with a file accesible locally

## Improvements needed
- A better background proccess of the input file
- Provide solution to access a file not stored locally
- Implements unit test
- Better coverage of errors

## Run locally to test
```
pip install -r requirements.txt
python file_generation/create_unsorted_file.py
python server.py
```

## Deploy
- Create a Dockerfile with python:alpine3.11 and copy templates folder, requirements.txt, server.py and topk.py. Install requirements with pip install and launch server.py




