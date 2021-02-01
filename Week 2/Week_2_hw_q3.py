import random

random.seed(0)
class MyPerfTime:
    elapsed_time=0
    @staticmethod
    def time():
        number=random.randrange(1, 10)
        MyPerfTime.elapsed_time+=number
        return MyPerfTime.elapsed_time-number



# Create the decorator here
def timer(func):
    def wrapper():
        time_elapsed = MyPerfTime()
        print(f"Testing the performance of '{func.__name__}'")
        start_time = time_elapsed.time()
        result = func()
        end_time = time_elapsed.time()
        print(f"Finished '{func.__name__}' in {float(end_time - start_time):.4f}")
        return result
    return wrapper


@timer
def function_to_be_tested():
    res=[]
    for i in range(8):
        res.append(str(i))
    return ' '.join(res)

@timer
def second_function_to_be_tested():
    res=[]
    for i in range(12):
        res.append(str(i))
    return ' '.join(res)

print(function_to_be_tested())
print(second_function_to_be_tested())

