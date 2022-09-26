name = input( 'Enter ur name => ')
email= input( 'enter ur email =>')
mobile = input( 'enter ur mobile =>' )
city =  input( 'enter name of city =>')

# nested if- else 
if len(name) > 1:
    if '@' in email and len(email) > 11:
        if len(mobile) == 10 and mobile. isnumeric():
            if city in ['lucknow','delhi','noida']:
                print("Your data is save ,thanku")
            else:
                print(' we are not in your city')
        else:
            print('invalid mobile number')
    else:
        print('invalid email address')
else:
    print('who are u ? ')