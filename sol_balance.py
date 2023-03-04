import subprocess

account_address = input("Enter wallet address: ")
process = subprocess.Popen(['solana', 'balance', account_address], stdout=subprocess.PIPE)
output = process.communicate()[0]
balance = output.decode('utf-8').strip()
print(f"Wallet balance: {balance}")