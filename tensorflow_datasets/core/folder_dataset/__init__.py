# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Custom Datasets APIs."""

from tensorflow_datasets.core import registered

# Custom datasets cannot be instanciated through `tfds.load`
with registered.skip_registration():
  # pylint: disable=g-import-not-at-top
  from tensorflow_datasets.core.folder_dataset.image_folder import ImageFolder
  from tensorflow_datasets.core.folder_dataset.translate_folder import TranslateFolder
  # pylint: enable=g-import-not-at-top

__all__ = [
    "ImageFolder",
    "TranslateFolder",
]
