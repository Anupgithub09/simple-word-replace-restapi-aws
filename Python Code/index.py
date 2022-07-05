import json

def lambda_handler(event, context):
    try:
     input_string=event['string']
     output_string="There is no word to replace in the input string"
     replace_word_list=['Oracle','Google','Microsoft','Amazon','Deloitte']
     for word in replace_word_list:
         if word in input_string:
            word_replacement=word+u"\u00A9"
            input_string=input_string.replace(word, word_replacement)
            output_string=input_string
            print(output_string)
    except KeyError:
     output_string="API error : Please ensure input string is provided in json format with the correct key"
    except:
     output_string="API error : Please check the backend Lambda function logs"
     
    return output_string