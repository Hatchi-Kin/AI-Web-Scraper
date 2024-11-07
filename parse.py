from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the template for the prompt that will be used to extract information
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the OllamaLLM model with the specified version
model = OllamaLLM(model="llama3.2")

def parse_with_ollama(dom_chunks, parse_description):
    # Create a prompt using the defined template
    prompt = ChatPromptTemplate.from_template(template)
    
    # Create a chain by combining the prompt and the model
    chain = prompt | model


    parsed_results = []

    # Iterate over the chunks of DOM content
    for i, chunk in enumerate(dom_chunks, start=1):
        # Invoke the chain with the current chunk and parse description
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)