import time

def loading_animation():
    while True:
        for i in range(4):
            suffix = '.' * i if i < 3 else '...'
            print("Loading Program" + suffix, end='\r', flush=True)
            time.sleep(0.5)

loading_animation()