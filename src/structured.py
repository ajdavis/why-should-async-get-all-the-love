from concurrent.futures import ThreadPoolExecutor, as_completed

def listen_to_podcast():
    print("Listening to podcast")

def heat_water():
    return "heated water"

def grind_coffee():
    return "ground coffee"

def brew(future1, future2):
    for future in as_completed([future1, future2]):
        print(f"Adding {future.result()} to French press")

with ThreadPoolExecutor() as main_exec:
    main_exec.submit(listen_to_podcast)

    with ThreadPoolExecutor() as coffee_exec:
        heated_future = coffee_exec.submit(heat_water)
        ground_future = coffee_exec.submit(grind_coffee)
        brew(heated_future, ground_future)
        print("Drinking coffee")

    with ThreadPoolExecutor() as chores_exec:
        ...
