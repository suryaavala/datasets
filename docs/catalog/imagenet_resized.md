<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagenet_resized" />
  <meta itemprop="description" content="This dataset consists of the ImageNet dataset resized to fixed size.&#10;The images here are the ones provided by Chrabaszcz et. al. using the box resize method.&#10;&#10;For [downsampled ImageNet](http://image-net.org/small/download.php) for unsupervised learning see `downsampled_imagenet`.&#10;&#10;WARNING: The integer labels used are defined by the authors and do not match&#10;those from the other ImageNet datasets provided by Tensorflow datasets.&#10;See the original [label list](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts/blob/master/map_clsloc.txt),&#10;and the [labels used by this dataset](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/image_classification/imagenet_resized_labels.txt).&#10;Additionally, the original authors 1 index there labels which we convert to&#10;0 indexed by subtracting one.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagenet_resized&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/imagenet_resized-8x8-0.1.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet_resized" />
  <meta itemprop="sameAs" content="https://patrykchrabaszcz.github.io/Imagenet32/" />
  <meta itemprop="citation" content="@article{chrabaszcz2017downsampled,&#10;  title={A downsampled variant of imagenet as an alternative to the cifar datasets},&#10;  author={Chrabaszcz, Patryk and Loshchilov, Ilya and Hutter, Frank},&#10;  journal={arXiv preprint arXiv:1707.08819},&#10;  year={2017}&#10;}" />
</div>

# `imagenet_resized`

*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=imagenet_resized">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

This dataset consists of the ImageNet dataset resized to fixed size. The images
here are the ones provided by Chrabaszcz et. al. using the box resize method.

For [downsampled ImageNet](http://image-net.org/small/download.php) for
unsupervised learning see `downsampled_imagenet`.

WARNING: The integer labels used are defined by the authors and do not match
those from the other ImageNet datasets provided by Tensorflow datasets. See the
original
[label list](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts/blob/master/map_clsloc.txt),
and the
[labels used by this dataset](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/image_classification/imagenet_resized_labels.txt).
Additionally, the original authors 1 index there labels which we convert to 0
indexed by subtracting one.

*   **Homepage**:
    [https://patrykchrabaszcz.github.io/Imagenet32/](https://patrykchrabaszcz.github.io/Imagenet32/)

*   **Source code**:
    [`tfds.image_classification.ImagenetResized`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/imagenet_resized.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split          | Examples
:------------- | --------:
`'train'`      | 1,281,167
`'validation'` | 50,000

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Citation**:

```
@article{chrabaszcz2017downsampled,
  title={A downsampled variant of imagenet as an alternative to the cifar datasets},
  author={Chrabaszcz, Patryk and Loshchilov, Ilya and Hutter, Frank},
  journal={arXiv preprint arXiv:1707.08819},
  year={2017}
}
```

## imagenet_resized/8x8 (default config)

*   **Config description**: Images resized to 8x8

*   **Download size**: `237.11 MiB`

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(8, 8, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet_resized-8x8-0.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagenet_resized-8x8-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## imagenet_resized/16x16

*   **Config description**: Images resized to 16x16

*   **Download size**: `923.34 MiB`

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(16, 16, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet_resized-16x16-0.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagenet_resized-16x16-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## imagenet_resized/32x32

*   **Config description**: Images resized to 32x32

*   **Download size**: `3.46 GiB`

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(32, 32, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet_resized-32x32-0.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagenet_resized-32x32-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

## imagenet_resized/64x64

*   **Config description**: Images resized to 64x64

*   **Download size**: `13.13 GiB`

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(64, 64, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet_resized-64x64-0.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagenet_resized-64x64-0.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->