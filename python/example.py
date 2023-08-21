def my_function():
    print("This is a function inside the module.")

print("Module name:", __name__)

if __name__ == "__main__":
    print("This code is executed only when the script is run directly.")
    my_function()
