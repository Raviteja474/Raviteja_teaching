import re

# sample_string = "7898564321" 7898564321 is a valid mobile number
# sample_string = "+917898564321" +917898564321 is a valid mobile number
# sample_string = "0898564321"  Not a valid mobile number
# sample_string = "6898564321" 6898564321 is a valid mobile number
# sample_string = "+916898564321" +916898564321 is a valid mobile number
# sample_string = "+913898564321" Not a valid mobile number
sample_string = "+916898564321"

# mobile_number_pattern = "^[0-9]{10}$"
# mobile_number_pattern = "^\+91[0-9]{10}$"
# mobile_number_pattern = "^[\+91]*[0-9]{10}$"

# mobile_number_pattern = "^(\+91)*[0-9]{10}$"

mobile_number_pattern = "^(\+91)*[6-9][0-9]{9}$"

mobile_number_match = re.search(mobile_number_pattern, sample_string)

if mobile_number_match:
    print(f"{mobile_number_match.group()} is a valid mobile number")
else:
    print("Not a valid mobile number")