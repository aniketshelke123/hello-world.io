def dump_config(config):
    names = config.keys()
    return ["=".join((i, str(config[i]))) for i in names]

config = answer = {'1': 'blue', '2': 'red', '3': 'red'}

#config = {'timeout': 1200, 'min_password_length': 8, 'mode': 'write'}
x = dump_config(config)
print(x)
#OR


# def dump_config(config):
#     names = config.items()
#     b = [f"{i}={config[i]}" for i in names]
#     #return "\n".join(b)
#     return b
#
# config = {'timeout': 1200, 'min_password_length': 8, 'mode': 'write'}
# print(dump_config(config))
