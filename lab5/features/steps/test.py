from ast import Try
from behave import *
import sys
sys.path.append("../../")
from lab1 import get_roots


@given(u'{given_a} coef a, coef b is {given_b} and c is {given_c}')
def step_impl(context, given_a, given_b, given_c):
    global a
    global b
    global c
    a = int(given_a)
    b = int(given_b)
    c = int(given_c)
    return True


@When("starting function")
def step_impl(context):
    global result
    result = get_roots(a, b, c)
    # return True
    if type(a) == int:
        return True

@Then("we shoud see {given_result}")
def step_impl(context, given_result):
    try:
        assert(result == given_result)
        return True
    except:
        return False
