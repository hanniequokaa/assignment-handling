# File Handling and Exception Handling Assignment

def file_read_write():
    try:
        # Read from an existing file
        with open("input.txt", "r") as infile:
            content = infile.read()

        # Modify content (example: make everything uppercase)
        modified_content = content.upper()

        # Write to a new file
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("File read and modified successfully! Check 'output.txt'.")

    except FileNotFoundError:
        print("input.txt file not found. Please make sure it exists.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Error Handling Lab 
def error_handling_lab():
    filename = input("Enter the filename you want to read: ")

    try:
        with open(filename, "r") as file:
            print("File content:")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# --- Run Programs ---
if __name__ == "__main__":
    print("=== File Handling Challenge ===")
    file_read_write()

    print("\n=== Error Handling Lab ===")
    error_handling_lab()
