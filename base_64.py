import base64
sample_string = input("\tEnter a text for base64 Encoded: \n\t=> ")
sample_string_bytes = sample_string.encode("ascii")

base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")
print(f" \tYour Encoded Value: \n\t=> {base64_string}")

# Decode for base64 
print("\n")
base64_string =input("\tEnter Text Decode for base64: \n\t=> ")
base64_bytes = base64_string.encode("ascii") 

sample_string_bytes = base64.b64decode(base64_bytes) 
sample_string = sample_string_bytes.decode("ascii") 

print(f"\tYour Decoded Value: \n\t=> {sample_string}") 
