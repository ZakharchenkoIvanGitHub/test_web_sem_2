import yaml

from module import Site


with open("testdata.yaml") as f:
    data = yaml.safe_load(f)

site = Site(data["address"])


