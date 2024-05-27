def calc(ppu, ppn, maxRange):
    for i in range(maxRange):
        print(f"${i * ppu} which is {i} {ppn}")

def main():
    while True:
        try:
            ppu = float(input("Enter the price per unit: "))
            ppn = input("Enter the product name: ")
            maxRange = int(input("Enter the range: "))
            calc(ppu, ppn, maxRange)

            save = input("Do you want to save the output to a file? (yes/no): ").strip().lower()
            if save in ('yes', 'y'):
                filename = input("Enter the filename: ")
                with open(filename, 'w') as file:
                    for i in range(maxRange):
                        file.write(f"${i * ppu} which is {i} {ppn}\n")
                print(f"Output saved to {filename}")

            another = input("Do you want to calculate another product? (yes/no): ").strip().lower()
            if another not in ('yes', 'y'):
                break
        except ValueError:
            print("Invalid input. Please enter numerical values for price per unit and range.")

if __name__ == "__main__":
    main()
