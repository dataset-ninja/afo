**AFO: Aerial Dataset of Floating Objects** is a dataset for object detection tasks. It is used in the security industry.

The dataset consists of 3640 images with 119973 labeled objects belonging to 9 different classes including *object*, *small_obj*, *human*, and other: *large_obj*, *wind/sup-board*, *kayak*, *boat*, *bouy*, and *sailboat*.

Each class belongs to one of three dataset versions (depending on the goal of the CV task): **6categories** version (classes *human*, *wind/sup-board*, *kayak*, *boat*, *bouy*, *sailboat*) to check how accurately detectors can detect humans vs. other floating objects (_a large data imbalance_); **2categories** version (classes *small_obj*, *large_obj*) to the task of searching for missing people (small objects) and boats (large objects) (_slightly more balanced_); **1category** version (class *object*) which marks all bounding boxes as one class to reflect the fact that usually during search and rescue operations at the sea, finding any object of a human origin can be significant.

Images in the AFO dataset have bounding box annotations. There are 728 (20% of the total) unlabeled images (i.e. without annotations). There are 3 splits in the dataset: *test* (514 images), *train* (2787 images), and *validation* (339 images). The dataset was released in 2021 by the [AGH University of Science and Technology, Poland](https://www.agh.edu.pl/en/).

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/afo/raw/main/visualizations/horizontal_grid.png">
