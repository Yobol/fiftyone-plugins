import fiftyone as fo

# import fiftyone.zoo as foz

# dataset = foz.load_zoo_dataset("quickstart", persistent=True)
# session = fo.launch_app(dataset, address='0.0.0.0', port=5151)

session = fo.launch_app(address='0.0.0.0', port=5151)
session.wait()
