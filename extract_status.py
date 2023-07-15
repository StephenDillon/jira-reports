import json
from time_formatter import format_time

def parse_json(json_data):
    parsed_data = {}
    
    # Load JSON data
    data = json.loads(json_data)
    
    # Iterate over each item in the JSON array
    for item in data:
        key = item['key']
        
        # Initialize the time spent dictionary for the key
        time_spent = {}

        # Sort the histories based on the created timestamp in ascending order
        histories = sorted(item['changelog']['histories'], key=lambda x: x['created'])
        
        
        # Iterate over each history item in the changelog
        for history in histories:
            # Get the created timestamp
            created = history['created']
            
            # Iterate over each item in the history
            for item in history['items']:
                if item['field'] == 'status':
                    from_status = item['fromString']
                    to_status = item['toString']
                    
                   # Calculate the time spent in the status
                    time_spent[from_status] = time_spent.get(from_status, 0) + 1
                    time_spent[to_status] = time_spent.get(to_status, 0) - 1
        
        # Format the time spent dictionary values
        formatted_time_spent = {status: format_time(duration) for status, duration in time_spent.items()}
        
        # Add the formatted time spent dictionary to the parsed data for the key
        parsed_data[key] = formatted_time_spent
    
    return parsed_data