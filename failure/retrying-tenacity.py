import tenacity
import random

def do_something():
    if random.randint(0, 1) == 0:
        print("Failure")
        raise RuntimeError
    print("Success")
    return True

# Just retrying
tenacity.Retrying()(do_something)

# Retrying with fixed 1 sec delay
@tenacity.retry(wait=tenacity.wait_fixed(1))
def do_something_and_retry():
    return do_something()

do_something_and_retry()


# Retrying with fixed 1 sec delay
@tenacity.retry(
    wait=tenacity.wait_exponential(
        multiplier=0.5, 
        max=30, 
        exp_base=2
    ),
    retry=(
        tenacity.retry_if_exception_type(RuntimeError) |
        tenacity.retry_if_result(lambda result: result is None)
    )
)
def do_something_and_retry1():
    return do_something()

do_something_and_retry1()