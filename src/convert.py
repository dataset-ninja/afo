# https://www.kaggle.com/datasets/teddevrieslentsch/morado-5may

import ast
import csv
import os
import xml.etree.ElementTree as ET

import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)

# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


# project_name = "Airbus Aircraft Detection"
dataset_path = "./APP_DATA/PART_1"
images_dir = "./APP_DATA/PART_1/images"
batch_size = 30
ds_names = ["train", "test", "validation"]

# images_folder = "images"
# annotations_folder = "annotations"
ann_ext = ".txt"


def create_ann(image_path):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_width = image_np.shape[1]

    for version in ["1category", "2categories", "6categories"]:
        ann_path = os.path.join(dataset_path, version, get_file_name(image_path) + ann_ext)

        if file_exists(ann_path):
            with open(ann_path) as f:
                content = f.read().split("\n")

                for curr_data in content:
                    if len(curr_data) != 0:
                        curr_data = list(map(float, curr_data.split(" ")))
                        obj_class = idx_to_class[version][int(curr_data[0])]

                        left = int((curr_data[1] - curr_data[3] / 2) * img_width)
                        right = int((curr_data[1] + curr_data[3] / 2) * img_width)
                        top = int((curr_data[2] - curr_data[4] / 2) * img_height)
                        bottom = int((curr_data[2] + curr_data[4] / 2) * img_height)
                        rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                        label = sly.Label(rectangle, obj_class)
                        labels.append(label)

    return sly.Annotation(img_size=(img_height, img_width), labels=labels)


obj_classes_6cat = [
    sly.ObjClass("human", sly.Rectangle),
    sly.ObjClass("wind/sup-board", sly.Rectangle),
    sly.ObjClass("boat", sly.Rectangle),
    sly.ObjClass("bouy", sly.Rectangle),
    sly.ObjClass("sailboat", sly.Rectangle),
    sly.ObjClass("kayak", sly.Rectangle),
]
obj_classes_2cat = [
    sly.ObjClass("small_obj", sly.Rectangle),
    sly.ObjClass("large_obj", sly.Rectangle),
]
obj_classes_1cat = [
    sly.ObjClass("object", sly.Rectangle),
]

idx_to_class = {}

idx_to_class["6categories"] = {idx: cls for idx, cls in zip(range(6), obj_classes_6cat)}
idx_to_class["2categories"] = {idx: cls for idx, cls in zip(range(2), obj_classes_2cat)}
idx_to_class["1category"] = {0: obj_classes_1cat[0]}


# images_path = os.path.join(dataset_path, images_folder)
# anns_path = os.path.join(dataset_path, annotations_folder)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_classes_6cat + obj_classes_2cat + obj_classes_1cat)
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in ds_names:
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        with open(os.path.join(dataset_path, f"{ds_name}.txt")) as f:
            images_names = f.read().split("\n")

        # images_path = os.path.join(dataset_path, ds_name)
        # images_names = os.listdir(images_path)

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

        for images_names_batch in sly.batched(images_names, batch_size=batch_size):
            img_pathes_batch = [
                os.path.join(images_dir, image_name) for image_name in images_names_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)

            # if ds_name == "images":
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(images_names_batch))

    return project
