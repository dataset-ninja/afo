Dataset **AFO** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/S/X/Gt/3SWRFg7UDJTVaXM1LVB18mFpPJ1JyTiOzapmjJWPoO1OSCiyhqzjLmNjRBA0N1OdcNX0QrTS0hXhTRnxLbn2xwcuViF68a9tTZxYYGpkIqj4ZizRgnOBzsLpygzP.tar)

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