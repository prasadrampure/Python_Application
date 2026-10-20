from transformers import pipeline

# load pretrained text generation pipeline
generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

# input prompt
prompt = "Artificial intelligence is"

# generate text
result = generator(
    prompt,
    max_new_tokens = 30,
    do_sample = False,
    pad_token_id = generator.tokenizer.eos_token_id
)

print("Generated text :")
print(result[0]["generated_text"])