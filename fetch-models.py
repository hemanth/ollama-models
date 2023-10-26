import datasets

def prompt2file(prompt, filename):
  modelTemplate = """# Run `ollama create {filename} -f ./{filename}` and then `ollama run {filename}`
FROM llama2
PARAMETER temperature 1
SYSTEM \"""
{prompt}
\"""
"""
  modelTemplate = modelTemplate.format(prompt=prompt, filename=filename)

  with open(filename, "w") as f:
    f.write(modelTemplate)

def capitalizeWords(act):
  return ''.join(c for c in act if c.isalnum())

if __name__ == "__main__":
  # Load the dataset.
  dataset = datasets.load_dataset("fka/awesome-chatgpt-prompts")

  # Loop over the prompts in the dataset.
  for i in range(0,len(dataset["train"])):
    [act, prompt] = dataset["train"][i]["act"], dataset["train"][i]["prompt"]
    prompt2file(prompt,capitalizeWords(act))