import psycopg

def handle_input_1(conn):
    input_speed = input("\nPlease specify a speed: ")
    
    with conn.cursor() as cur:
        cur.execute(
            """SELECT model FROM laptop
                WHERE speed >= %s 
                UNION ALL
                SELECT model FROM pc
                WHERE speed >= %s""", 
                (input_speed, input_speed))
        
        fast_computers = cur.fetchall()

        print(f"\nComputers with a speed of at least {input_speed}", end=": ")
        for row in fast_computers:
            print(*row, end=" ")

    print()
    
def handle_input_2(conn):
    input_maker = input("\nPlease specify a manufacturer (A-H): ")

    with conn.cursor() as cur:
        cur.execute(
                """SELECT model, 'laptop' AS type FROM laptop
                    WHERE maker = %s 
                    UNION ALL
                    SELECT model, 'pc' AS type FROM pc
                    WHERE maker = %s
                    UNION ALL
                    SELECT model, 'printer' AS type FROM printer
                    WHERE maker = %s""", 
                    (input_maker, input_maker, input_maker))
        
        products_from_maker = cur.fetchall()
        valid_models = [row[0] for row in products_from_maker]
        
        print(f"\nProducts from manufacturer {input_maker}", end=": ")
        for row in products_from_maker:
            print(f"Model: {row[0]}, Type: {row[1]}")

        input_model = int(input("\nSelect a model from the list to view its price: "))

        if input_model not in valid_models:
            print("Please enter a model found above")
        else:
            cur.execute(
                    """SELECT price FROM laptop
                        WHERE model = %s 
                        UNION ALL
                        SELECT price FROM pc
                        WHERE model = %s
                        UNION ALL
                        SELECT price FROM printer
                        WHERE model = %s""", 
                        (input_model, input_model, input_model))
            
            model_price = cur.fetchone()
            if model_price:
                print(f"\nModel number {input_model} costs ${model_price[0]}")


def main():
    with psycopg.connect("dbname=ethanclaire port=9999") as conn:
        print("\nWould you like to" \
        "\n1: Specify a speed and see what Laptop and PC models " \
        "have a speed of at least that speed" \
        "\n2: Specify a manufacturer and find the model number and type" \
        " of all products made by that manufacturer? ")

        while True: # thank you python for not having do-while
            user_input = input("\nPlease type 1, 2, or q to quit " \
            "\nType 'help' if you would like to see the options again: ")
            if(user_input == '1'):
                handle_input_1(conn)
            elif(user_input == '2'):
                handle_input_2(conn)
            elif(user_input == 'help'):
                print("Would you like to" \
                "\n1: Specify a speed and see what Laptop and PC models " \
                "have a speed of at least that speed" \
                "\n2: Specify a manufacturer and find the model number and type" \
                " of all products made by that manufacturer? ")
            elif(user_input == 'q'):
                break  

if __name__ == "__main__":
    main()