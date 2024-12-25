import fiftyone.operators as foo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart")

ctx = {
    "view": dataset.take(10),
    "params": dict(
        export_type="LABELS_ONLY",
        # export_type="MEDIA_AND_LABELS",
        dataset_type="COCO",
        labels_path=dict(absolute_path="/tmp/coco/labels.json"),
        label_field="ground_truth",
    )
}

foo.execute_operator("@voxel51/io/export_samples", ctx)
