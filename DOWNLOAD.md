Dataset **AFO** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/P/a/st/tPEapD6aRt5maGLZjcLgra9sspta0wc1DwoQhC9EahocdYlK2GfsX24h0i9MCaiXe8wD1RsRETvJ6oQiPh03naqhBXSjdTAqKSSYFddomge8thSMzesVxtTAj8MW.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='AFO', dst_path='~/dtools/datasets/AFO.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/jangsienicajzkowy/afo-aerial-dataset-of-floating-objects/download?datasetVersionNumber=1)