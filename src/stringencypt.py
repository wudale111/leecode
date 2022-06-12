# 不难，就是理解起来有点费劲。其实就是对key中的字符进行去重得到newkey，newkey中的字符从字母表中干掉，然后保持字符的相对顺序：
# newkey中的字符在前，字母表剩余的字符在后，拼接起来得到值列表。原来26个字母的列表对应为其键列表，根据键值对的映射关系来对明文进行翻译。
# 要想保持原来的大小写，我们可以只建立大写字母的映射关系，在对明文进行逐字符翻译时将明文的字符转换成大写去映射中查找其对应的密文，
# 此时查找到的对应密文是个大写字符，如果明文字符是个小写字符，把这个对应到的密文转换成小写就行了。
alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()

while True:
    try:
        key, plaintext = input().strip(), input().strip()
        mem = set()  # 用于去重key的字符
        # 构建值列表
        k, v = list(alphabet), []
        for c in key.upper():
            if c not in mem:
                mem.add(c)
                v.append(c)
                k.remove(c)
        v.extend(k)
        # 构建映射关系
        mp = dict(zip(alphabet, v))
        # 加密
        ciphertext = []
        for c in plaintext:
            if ord(c) >= 97 and ord(c) <= 122:
                # 由于mp中的key为大写字母，所有明文中字符为小写字母时转换为大写字母来进行翻译
                ciphertext.append(mp[c.upper()].lower())
            else:
                ciphertext.append(mp[c])
        print(''.join(ciphertext))
    except:
        break