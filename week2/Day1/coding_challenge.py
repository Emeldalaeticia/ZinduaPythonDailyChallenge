import re 

def extract_phone_number(string):
    phone_pattern = r"\d{3}\D{0,3}\d{3}\D{0,3}\d{4}"
    phone_numbers = re.findall(phone_pattern,string)
    return phone_numbers

def extract_email_addresses(string):
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_addresses = re.findall(email_pattern, string)
    return email_addresses

def replace_email_addresses(string, replacement):
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    replaced_string = re.sub(email_pattern, replacement, string)
    return replaced_string

string = "Sunset Sweet Cupcakes is a cloud bakiery. You can reach them on their number is (111) 713-5805 and their email - sunsetsweetcupcakes@gmail.com"

print(extract_phone_number(string))
print(extract_email_addresses(string))
print(replace_email_addresses(string, "sunsetsweet@gmail.com"))