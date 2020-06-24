from key_generator import generate
from tqdm.auto import tqdm

##key1 = generate(5, '-', 3, 3, type_of_value = 'hex', capital = 'none', extras = ['%', '&', '^'], seed = 42).get_key()
##key2 = generate(2, '-', 3, 10, type_of_value = 'char', seed = 42).get_key()
##key3 = generate(seed = 101)
##print(key1)
##print(key2)
##print(key3.get_key())

print("Checking test cases...")
test_num = 0
test_passed = 0
test_failed = 0
h_total = 100
extras_test = ['^', '%', '&', '#', '!', '@', '$']
pbar = tqdm(total = h_total)

for h in range(h_total):
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(j, 10):
                for l in ['hex', 'char', 'int']:
                    for m in ['none', 'all', 'mix']:
                        key = generate(i, '-', j, k, seed = h, type_of_value = l, capital = m).get_key()
                        
                        flag_check = 0
                        if(len(key.split('-')) == i):
                            flag_check += 1
                        len_atoms = [len(x) for x in key.split('-')]
                        if(min(len_atoms) >= j and max(len_atoms) <= k):
                            flag_check += 1
                        is_in = 0
                        if(l == 'hex' and m == 'none'):
                            for _ in ''.join(key.split('-')):
                                if(_ not in [str(x) for x in list(range(0, 10))] + [chr(x) for x in list(range(ord('a'), ord('f') + 1))] + extras_test):
                                    is_in += 1
                        if(l == 'hex' and m == 'all'):
                            for _ in ''.join(key.split('-')):
                                if(_ not in [str(x) for x in list(range(0, 10))] + [chr(x) for x in list(range(ord('A'), ord('F') + 1))] + extras_test):
                                    is_in += 1
                        if(l == 'hex' and m == 'mix'):
                            for _ in ''.join(key.split('-')):
                                if(_ not in [str(x) for x in list(range(0, 10))] + [chr(x) for x in list(range(ord('a'), ord('f') + 1))] + [chr(x) for x in list(range(ord('A'), ord('F') + 1))] + extras_test):
                                    is_in += 1
                        if(l == 'char' and m == 'none'):
                            for _ in ''.join(key.split('-')):
                                if(_ not in [chr(x) for x in list(range(ord('a'), ord('z') + 1))] + extras_test):
                                    is_in += 1
                        if(l == 'char' and m == 'all'):
                            for _ in ''.join(key.split('-')):
                                if(_ not in [chr(x) for x in list(range(ord('A'), ord('Z') + 1))] + extras_test):
                                    is_in += 1
                        if(l == 'char' and m == 'mix'):
                            for _ in ''.join(key.split('-')):
                                if(_ not in [chr(x) for x in list(range(ord('a'), ord('z') + 1)) + list(range(ord('A'), ord('Z') + 1))] + extras_test):
                                    is_in += 1
                        if(l == 'int'):
                            for _ in ''.join(key.split('-')):
                                if(_ not in [str(x) for x in list(range(0, 10))] + extras_test):
                                    is_in += 1
                        
                        if(is_in == 0):
                            flag_check += 1
                        
                        if(flag_check == 3):
                            test_passed += 1
                        else:
                            test_failed += 1
                        test_num += 1
    pbar.update(1)
pbar.close()
print()
print("Total Test Cases: " + str(test_num))
print("Test Passed: " + str(test_passed))
print("Test Failed: " + str(test_failed))
input('Press ENTER to exit')
