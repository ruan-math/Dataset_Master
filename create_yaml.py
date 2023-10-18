import yaml

data_yaml = dict(
    train = '60m/train',
    val = '60m/val',
    test = '60m/test',
    nc = 5,
    names = ['car', 'person', 'motorcycle', 'truck', 'animal']
)

with open('data.yaml', 'w') as outfile:
    yaml.dump(data_yaml, outfile, default_flow_style=True)
