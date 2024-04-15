import sys
import os
import json
import yaml

if len(sys.argv) > 1:  # do we have more than 1 argument?
    if os.path.exists(sys.argv[1]):  # is the filename passed actually present?
        with open(sys.argv[1], "r") as file:
            try:
                data = json.load(file)  # Load JSON data
                print("JSON is valid!")
                yaml_data = yaml.dump(data, default_flow_style=False)  # Convert JSON to YAML
                with open("output.yaml", "w") as yaml_file:  # Write YAML data to a file
                    yaml_file.write(yaml_data)
                print("YAML file 'output.yaml' has been created.")
            except json.JSONDecodeError:
                print("Error: Invalid JSON format.")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: python check_json.py <file>")