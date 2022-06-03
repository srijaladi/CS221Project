import numpy
import torch
import numpy as np

# Import generic wrappers
from transformers import AutoModel, AutoTokenizer

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Insert reviews manually here
reviews = []
reviews.append("Be prepared with this huge workload class.")
reviews.append("Very well organized course. Nick is a good lecturer and the course videos are very helpful. The assignments are fun and the exams were quite reasonable. Overall, I definitely learned a lot.")
reviews.append("Rewarding class, but budget out plenty of time to work on assignments - esp. the last two.")
reviews.append("Find friends and start assignments early. It’s fun if you make it less stressful for yourself")
reviews.append("Do not combine it with other intensive courses like cs103.")
#reviews.append("")

sum = 0
for review in reviews:
    inputs = tokenizer(review, return_tensors="pt")
    outputs = model(**inputs)
    sum += outputs[0][0][0][0].item()
average = sum / len(reviews)

print(average)