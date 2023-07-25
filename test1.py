# from train.match import MatchAnswer
#
# if __name__ == "__main__":
#     answer = MatchAnswer("钟离")
#     matchs = answer.match("早安")
#     print(matchs)
def number_to_letter(number):
    if not 1 <= number <= 100:
        raise ValueError("Number must be between 1 and 100")

    if number <= 26:
        # Convert the number to a letter using the same method as before
        letter = chr(number + 64)
    else:
        # For numbers between 27 and 100, convert the tens and ones digits separately
        tens_digit = (number - 1) // 26
        ones_digit = (number - 1) % 26
        tens_letter = chr(tens_digit + 65) if tens_digit > 0 else ""
        ones_letter = chr(ones_digit + 65)
        letter = f"{tens_letter}{ones_letter}"

    return letter


ii = 74
for i in range(ii):
    if i < 9:
        print(f"""import {number_to_letter(i + 1)}Avatar from \"../assets/1000{i + 1}.webp\";""")
    else:
        print(f"""import {number_to_letter(i + 1)}Avatar from \"../assets/100{i + 1}.webp\";""")

for i in range(ii):
    print(f"""export const {number_to_letter(i + 1)}Model = {{
    name: "{number_to_letter(i + 1)}",
    avatar: {number_to_letter(i + 1)}Avatar
}};
    """)

print("export const users = [")

for i in range(ii):
    print(f"""{number_to_letter(i + 1)}Model,""")
print("];")
