# DevOps case study

This case study should take approximately 3 hours to complete.
Please do not publish your code and answer online - we intend to reuse this test.

You may submit your answers in any format, so long as it is easy for us to view, understand and evaluate your responses

## Dockerfile improvement

You are asked to review a Dockerfile from one of your teammates. This person is new to Docker and would be happy to learn from your expertise and feedback.
Look at the content of the docker build folder below and provide a corrected Dockerfile, suggestions and explanations on how to improve it further.

## Top K exercise

### Context

You’re a superstar Dev and Ops at SomeCompany.
At the end of the day, you will leave the office for a long vacation, and your colleagues won’t be able to reach you.

2 ½ hours  before you have to leave the office (and you can’t miss your flight!) you are informed that your company has an urgent requirement for a new application “topK”. This is business critical, and you are the only one who can work on it today. Even if not perfect, something has to be delivered in production today. You can do it in the language of your choice.

Tomorrow another Dev and Ops will come back and will continue to work on it. He is a superstar as well, but perhaps slightly less than you. 

### Program specification

Given a number K and an arbitrarily large file containing individual numbers on each line (e.g. 200Gb file), output the largest K numbers, highest first.

File is provided online. The app has to detect updates and do the analysis.
Then everyone at the company should have access to all results.

This application is going to evolve to include frequent new requirements and as it is critical, it's important to ensure there is no regression. 


### Deliverable

So, in 2 ½ hours, you have to do your best to : 
- Provide a program that best meets the need;
- Ensure to provide all instructions or tooling needed to deliver it (a junior ops can do it after you leave today)
- Write down all information needed for your teammate to continue to work on it. Be sure to explain: 
  - Your implementation choice
  - Run / time complexity
  - Limitation of current solution
  - Improvement needed for a real production solution

You likely **won’t have time** to do everything perfectly in 2 ½ hours. Planning what you can do, and leaving good instructions for your coworker for the rest, is part of the test. 

### Answer

- [Dockerfile](docker/README.md)
- [TopK](topk/README.md)