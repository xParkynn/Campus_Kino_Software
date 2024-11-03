from Program.backend_json import BackEnd


def main():
    backend = BackEnd()
    while True:
        print("Enter 'a' for adding a new product, 'm' for modifying a product, 'r' to remove a product, 'q' to quit:")
        input_str = input("Input: ")
        if input_str == 'q':
            break
        elif input_str == 'a':
            prod_input = input("Which product do you want to add: ")
            amount_input = input("Amount of stock: ")
            price_input = input("Selling price: ")
            buying_input = input("Money spent per product: ")
            backend.add_entry(name=prod_input, init_amount=amount_input, price=price_input, buying_price=buying_input)
            continue
        #elif input_str == 'm':



if __name__ == "__main__":
    main()