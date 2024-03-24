# Password Generator

## Overview

This Python script provides a secure way to generate a random password of a specified length. The generated password ensures a mix of uppercase letters, lowercase letters, digits, and special characters, making it robust for securing accounts.

## Features

- **Customizable Length**: Specify the desired length for the password, with a minimum length of 4 characters to ensure the inclusion of all character types.
- **Character Diversity**: Each password contains at least one uppercase letter, one lowercase letter, one digit, and one special character.
- **Randomness**: The characters in the password are shuffled to enhance security by increasing randomness.

## Requirements

The script uses the `random` and `string` modules from the Python Standard Library, hence it does not require external dependencies.

## Usage

To generate a password, simply run the `generate_password` function with the desired password length as its argument. The default length is set to 12 characters.

### Example

```python
from your_script_name import generate_password

# Generate a 12-character long password
password = generate_password(12)
print(password)
