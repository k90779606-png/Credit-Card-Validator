def validate_credit_card(card_number):
  card_number = card_number.replace(" ","").replace("-","")

  if not card_number.isdigit():
      return False
    
  digits = [int(d) for d in card_number]
  
  checksum = 0
  payload = digits[:-1][::-1]
  
  total_sum = checksum
  
  for i, digit in enumerate(payload):
      if i % 2 == 0:
          doubled = digit * 2
          if doubled > 9:
              doubled -= 9
          total_sum += doubled
      else:
          total_sum += digit
          
  return (total_sum * 9) % 10 == digits[-1]

test_card = input("Enter credit card number to validate: ")

if validate_credit_card(test_card):
    print("Valid credit card number.")
else:
    print("Invalid credit card number.")     
