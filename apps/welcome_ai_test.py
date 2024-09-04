import os
import openai
from openai import AzureOpenAI

# Set up Azure OpenAI service
openai.api_key = os.getenv("OPEN_AI_KEY")
openai_endpoint = os.getenv("OPEN_AI_URL")

client = AzureOpenAI(
    api_key=os.getenv("OPEN_AI_KEY"),
    api_version="2024-06-01",
    azure_endpoint=os.getenv("OPEN_AI_URL")
)


# Define a function to generate OpenAPI spec using GPT-4
def generate_openapi_spec(description):
    # Define the prompt to generate OpenAPI spec
    prompt = f"Convert the following API description into an OpenAPI 3.0 specification in YAML format:\n\n{description}\n\nOpenAPI spec:"
    deployment_name = 'gpt-35-turbo'
    response = client.completions.create(model=deployment_name, prompt=prompt, max_tokens=300)

    # Get the generated OpenAPI spec from the response
    openapi_spec = response.choices[0].text.strip()
    return openapi_spec


# Main execution
if __name__ == "__main__":
    # Example input description
    api_description = """
    Give me an API for CRUD operations for a book store api
    """

    # Generate OpenAPI spec
    openapi_spec = generate_openapi_spec(api_description)
    print("Generated OpenAPI Specification:")
    print(openapi_spec)