# key-generator
A simple python package to generate customizable keys.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install key_generator.

```bash
pip install key-generator
```

## Usage

```python
from key_generator.key_generator import generate

key = generate(seed = 101)
print(key.get_key())  # be1679-6ae28652eb-fa7cd6-de96-a8cc

key_custom = generate(5, '-', 3, 3, type_of_value = 'hex', capital = 'none', extras = ['%', '&', '^'], seed = 42).get_key()
print(key_custom)  # ^54-10e-fa&-%34-e3e

key_custom_2 = key_generator.generate(2, ['-', ':'], 3, 10, type_of_value = 'char', capital = 'mix', seed = 17).get_key()
print(key_custom_2)  # ZLFdHXIUe-ekwJCu
```

## Parameters
| parameter     | type        | optional | default | description                                                                                                                                                                                                                                                                                               |
|---------------|-------------|----------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| num_of_atom   | int         | yes      | 5       | Number of parts/atoms of the key to be generated.                                                                                                                                                                                                                                                         |
| separator     | string,list | yes      | '-'     | Separates the parts/atoms by separator is given a string.<br>If given a list, randomly chooses separators in between the atoms.                                                                                                                                                                           |
| min_atom_len  | int         | yes      | 3       | Minimum length of each part/atom.                                                                                                                                                                                                                                                                         |
| max_atom_len  | int         | yes      | 10      | Maximum length of each part/atom.                                                                                                                                                                                                                                                                         |
| type_of_value | string      | yes      | 'hex'   | Can be one of the following 3 options: `hex`, `char`, `int`.<br><br>`hex` -> key can have values only from 0-9, a-f, or A-F(depending on `capital` parameter).<br>`char` -> key can have values only from a-z or A-Z(depending on `capital` parameter).<br>`int` -> key can have values only between 0-9. |
| capital       | string      | yes      | 'none'  | Can be one of the following 3 options: `none`, `all`, `mix`.<br><br>`none` -> All the values in the generated key will be lowercase.<br>`all` -> All the values in the generated key will be uppercase.<br>`mix` -> A mix of both upper and lower case randomly.                                          |
| extras        | list        | yes      | []      | List of extra symbols or characters that you want to include in each part/atom.<br>Adds these symbols to the bucket to randomly choose characters in the atom.                                                                                                                                            |
| seed          | int         | yes      | None    | Choose a seed value for the random key generated.<br>Returns the same pseudo-random value every time for a given seed value.                                                                                                                                                                              |

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure all the tests in the tests directory pass.

## License
[MIT](https://github.com/Sahith02/key-generator/blob/master/LICENSE)