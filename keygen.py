from algosdk import account, mnemonic

def generate_algorand_account():

    # Generate a new Algorand account (private key and address)
    private_key, address = account.generate_account()

    # Generate the mnemonic phrase (recovery phrase) from the private key
    mnemonic_phrase = mnemonic.from_private_key(private_key)

    # Create a filename for saving the account details
    filename = "algorand_account_info.txt"

    # Display the account information
    print("=============================================")
    print("         Your New Algorand Wallet            ")
    print("=============================================")
    print(f"Wallet Address: {address}")
    print("---------------------------------------------")

    # Display private key and mnemonic with warnings
    print("WARNING: The following is highly sensitive information!")
    print("DO NOT share it publicly. Store it securely.")
    print("---------------------------------------------")
    print(f"Private Key: {private_key}")
    print(f"Mnemonic Phrase (Recovery Phrase): {mnemonic_phrase}")
    print("---------------------------------------------")
    print(f"Account details saved to: {filename}")
    print("Make sure to store this information securely.")
    print("You will need it to recover your account in the future.")
    print("=============================================")

    # Save the account details to a text file
    with open(filename, "w") as file:
        file.write("=============================================\n")
        file.write("         Your New Algorand Wallet            \n")
        file.write("=============================================\n")
        file.write(f"Wallet Address: {address}\n")
        file.write("---------------------------------------------\n")
        file.write("WARNING: The following is highly sensitive information!\n")
        file.write("DO NOT share it publicly. Store it securely.\n")
        file.write("---------------------------------------------\n")
        file.write(f"Private Key: {private_key}\n")
        file.write(f"Mnemonic Phrase (Recovery Phrase): {mnemonic_phrase}\n")
        file.write("---------------------------------------------\n")
        file.write("Make sure to store this information securely.\n")
        file.write("You will need it to recover your account in the future.\n")
        file.write("=============================================\n")

# Call the function to generate and save the account
generate_algorand_account()
