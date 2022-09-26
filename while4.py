
even = 0
odds = 0

while True:
    num = input('Enter a number')
    if not num:
        break
    if not num.isnumeric():
        continue
    num = int(num)
    if num % 2 == 0:
         even +=num
    else:
        odds += num
print(f"even values added => {even}")
print(f"odd values added => {odds}")
