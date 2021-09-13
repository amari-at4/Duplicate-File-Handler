args = sys.argv

# further code of the script "add_four_numbers.py"
addition = sum([float(arg) for arg in sys.argv[1:]])

print(int(addition))
