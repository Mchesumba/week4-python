def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        # Read from the input file
        with open(filename, 'r') as file:
            content = file.read()
            print("\n✅ File read successfully!")

        # Modify the content (example: make it uppercase)
        modified_content = content.upper()

        # Define the output filename
        new_filename = "modified_" + filename

        # Write to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"✅ Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except IOError:
        print("❌ Error: Could not read or write the file.")

# Run the function
read_and_modify_file()
