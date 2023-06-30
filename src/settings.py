from typing import Dict, List, Optional, Union

from dataset_tools.templates import AnnotationType, CVTask, Industry, License

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "AFO"
PROJECT_NAME_FULL: str = "AFO: Aerial Dataset of Floating Objects"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_SA_3_0_IGO()
INDUSTRIES: List[Industry] = [Industry.SearchAndRescue()]
CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_YEAR: int = 2021
HOMEPAGE_URL: str = (
    "https://www.kaggle.com/datasets/jangsienicajzkowy/afo-aerial-dataset-of-floating-objects"
)
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 884176
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/afo"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.kaggle.com/datasets/jangsienicajzkowy/afo-aerial-dataset-of-floating-objects/download?datasetVersionNumber=1"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "object": [192, 192, 192],
    "small_obj": [255, 0, 0],
    "large_obj": [0, 0, 255],
    "human": [255, 0, 255],
    "wind/sup-board": [0, 255, 255],
    "boat": [255, 165, 0],
    "bouy": [128, 0, 128],
    "sailboat": [255, 192, 203],
    "kayak": [0, 255, 0],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[
    str
] = "https://content.iospress.com/articles/integrated-computer-aided-engineering/ica210649"
CITATION_URL: Optional[
    str
] = "https://www.kaggle.com/datasets/jangsienicajzkowy/afo-aerial-dataset-of-floating-objects"
ORGANIZATION_NAME: Optional[
    Union[str, List[str]]
] = "AGH University of Science and Technology, Poland"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.agh.edu.pl/en/"
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "industries": INDUSTRIES,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["tags"] = TAGS if TAGS is not None else []

    return settings
