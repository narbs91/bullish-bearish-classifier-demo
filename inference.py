import os
import json
from transformers import pipeline

def main():
    # Take in the statement to classify as a env variable
    statement = os.getenv('STATEMENT', 'DEFAULT_STATEMENT')

    # initialize the model
    pipe = pipeline("text2text-generation",
                      model="./local-flan-t5-small")
    
    classification_labels = ['positive', 'negative']
    
    # Construct a query we can supply to the model from the input the user gives us
    input = f'Statement: ${statement}. Is the statement positive or negative?'
    
    # Generate the text response from the output
    output = pipe(input, max_new_tokens=20)
    
    # Grab the generated text
    classification = output[0]['generated_text']
    
    # Create the directory to write our response to
    output_path = f'/outputs/response.json'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Output whether the classification was bullish (i.e positive) or bearish (i.e. negative)
    if classification == classification_labels[0]:
        data = {"data" : "bullish"}
    else:
        data = {"data" : "bearish"}
    
    # Write the result to /outputs/response.json    
    with open(output_path, 'w') as file:
            json.dump(data, file, indent=4)

    print(data)
if __name__ == '__main__':
    main()