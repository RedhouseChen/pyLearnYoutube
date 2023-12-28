# ex_args_kwargs.py
# *args: collects tuple arguments 
# **kwargs: collects keyword arguments
def invite_friends(host_name, *friends):
    print(host_name)
    print(friends)

def plan_party(host_name, **party_details):
    print(host_name)
    print(party_details)
#
invite_friends('Alice','John','Max','David')
plan_party('Alice', music='Jazz', food='Pizza', decorations='Balloons')