import yaml

data_yaml = dict(
    train = 'Dataset/train',
    val = 'Dataset/val',
    test = 'Dataset/test',
    nc = 5,
    names = ['car', 'person', 'motorcycle', 'truck', 'animal']
)

with open('data.yaml', 'w') as outfile:
    yaml.dump(data_yaml, outfile, default_flow_style=True)