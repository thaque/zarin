def process_data(input_data):
    result = ""
    for line in input_data.split("\n"):
        if line != "":
            numbers = [float(n) for n in line.split(", ")]
            result += str(sum(numbers))
        result += "\n"
    return result

input_filename = input("Enter the input filename: ")
output_filename = input("Enter the output filename: ")

with open(input_filename, "r") as input_file:
    input_data = input_file.read()

with open(output_filename, "w") as output_file:
    output_file.write(process_data(input_data))

