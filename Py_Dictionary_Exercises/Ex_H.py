# __Challenge__

# Print the value of key ‘history’ from nested dict.

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

result = sampleDict["class"]["student"]["marks"]["history"]

print(result)