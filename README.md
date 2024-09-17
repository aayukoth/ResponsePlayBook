1. Download python from https://www.python.org/downloads/
2. Set environment variables for python
3. Run a terminal in the project directory
4. Get the azure openai api key from a enterprise or personal subscription using https://portal.azure.com/. Steps to create a resource and get the key can be found at https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal
 - Deploy 2 models from the openai resource
    - A LLM model like GPT-4o
    - A text embeddings model like text-embedding-ada
5. To get the API key for the openai resource, go to the resource created in the azure portal and click on the keys and endpoint tab.
6. Update the .env file with the required values
7. Run the below command to setup a virtual environment
```
python -m venv venv
python -m venv <env_name>
```
8. Activate the virtual environment
```
venv\Scripts\activate (Windows)
<env_name>\Scripts\activate
source venv/bin/activate (Linux)
```
9. Install the required packages
```
pip install -r requirements.txt
```
