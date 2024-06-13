import glob
import os
import toml

# 获取目录中所有的.toml文件
toml_files = glob.glob('./mainnet/validators/*.toml')

all_vldtrs = []
addrs = []
for file in toml_files:
    if file.endswith('example.toml'):
        continue
    with open(file, 'r') as f:
        content = toml.load(f)

    address = content.get('Address', '')
    url = content.get('URL', '')
    if url == "":
        url = content.get('RPC', '')

    vldtr = f'[[Eth.Miner.Mev.Validators]]\nAddress = "{address}"\nURL = "{url}"\n'
    all_vldtrs.append(vldtr)
    addrs.append(f'"{address}",')

print("\n".join(all_vldtrs))
print("===================================")
print("\n".join(addrs))
