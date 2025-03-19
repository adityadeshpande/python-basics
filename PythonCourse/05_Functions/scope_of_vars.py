global_var = "I am global"

def test_scope():
    local_var = "I am local"
    print(global_var)
    print(local_var)

print("apple")
# play here

test_scope()