import random
import string

def generate_password(length=12):
    if length < 4:  # 确保密码长度足以包含所有类型的字符
        raise ValueError("Password length must be at least 4 characters.")
    
    # 字符集
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    
    # 确保密码包含所有类型的字符
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # 填充剩余的长度
    remaining_length = length - 4
    all_chars = uppercase_letters + lowercase_letters + digits + special_chars
    password += [random.choice(all_chars) for _ in range(remaining_length)]
    
    # 打乱密码中的字符以增加随机性
    random.shuffle(password)
    
    # 将密码列表转换为字符串
    return ''.join(password)

# 生成一个12位长的密码
print(generate_password(12))
