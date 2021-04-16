def convert(number):
    if number % 3 == 0:
        output = "Pling"
        if number % 5 == 0:
            output = "PlingPlang"
        return output

output = ""
convert(15)
