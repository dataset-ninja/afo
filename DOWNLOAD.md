Dataset **AFO** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/p/8/ui/j907Z5xqOxYcsEQxF6DZZ7SmIogKPhUpHy37fkbsTPvAhUtQJDl7cxM9PFxzGg5Q3Zqu4YmeZIDWoQn79UAZFWF90EI6WgOzMiIeUjkeFy5aykrIBvqh235Zp8Ec.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='AFO', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/jangsienicajzkowy/afo-aerial-dataset-of-floating-objects/download?datasetVersionNumber=1).