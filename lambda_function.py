import json

def lambda_handler(event, context):
    print(f"DEBUG: Received event: {json.dumps(event)}")
    
    try:
        # 1. Extraction remains the same
        params = {p['name']: p['value'] for p in event.get('parameters', [])}
        n1 = float(params.get('num1', 0))
        n2 = float(params.get('num2', 0))
        result = n1 + n2
        
        # 2. The NEW "Text-Only" Envelope
        # We REMOVE 'application/json' and put the result directly in 'body'
        action_response = {
            'actionGroup': event.get('actionGroup'),
            'function': event.get('function'),
            'functionResponse': {
                'responseBody': {
                    'TEXT': {
                        'body': str(result)  # Must be a string
                    }
                }
            }
        }
        
        # Bedrock direct-invoke wrapper
        final_response = {
            'messageVersion': '1.0',
            'response': action_response
        }
        
        print(f"DEBUG: Sending Text Response: {json.dumps(final_response)}")
        return final_response

    except Exception as e:
        return {
            'messageVersion': '1.0',
            'response': {
                'actionGroup': event.get('actionGroup'),
                'function': event.get('function'),
                'functionResponse': {
                    'responseBody': {'TEXT': {'body': f"Error: {str(e)}"}}
                }
            }
        }
