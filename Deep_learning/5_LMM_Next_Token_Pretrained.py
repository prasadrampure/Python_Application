import torch 

from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

# pretrained model name
model_name = "distilgpt2"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load pretranied language model
model = AutoModelForCausalLM.from_pretrained(model_name)

# Input Prompt
prompt = "I Love"

# Convert input into token ids
inputs = tokenizer(
    prompt,
    return_tensors = "pt"
)

# Enable evaluation mode
model.eval()

# perform inference without gradient calculations
with torch.no_grad():
    outputs = model(**inputs)

# Extract logits for final input position
logits = outputs.logits[0,-1,:]

# convert logits into probablities
probablities = torch.softmax(
    logits,
    dim=-1
)

# select five highest probablity tokens
values, indices = torch.topk(
    probablities,
    5
)

print("Input :",prompt)

for value,index in zip(values,indices):
    token = tokenizer.decode([index.item()])
    print(repr(token), round(value.item(), 4))