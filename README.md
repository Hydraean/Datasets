![](banner.png)

## Datasets

> Open Datasets for generated from the Hydraean Project, free for everyone.

You can referrence and download files from this repository. Available both in CSV and JSON Formats.

### Usage

Install Requirements

> Requires Python 3 to run the generator script.

```sh
pip install -r requirements.txt
```

This repository has a JSON file that you can use to get a mapping of the all the dataset files within this repository.

```sh
./hydraean-datasets.json
```

### Access Index file:

> The JSON Index file contains all the dataset files available in this repository.

You can access the raw JSON index file here, hosted by Github, directly from this public repository:
https://raw.githubusercontent.com/Hydraean/Datasets/main/hydraean-datasets.json

you can access this json file via fetch API or an HTTP Client like Axios.

### Generating dataset index file

`Python3` is required to run the python scripts within this repository.

1.) Generate Index File: `hydraean-datasets.json`

> Contains correlated details about the different dataset files.

```sh
python index_datasets.py
```

### Project Documentation

Learn more about the Hydraean project here.
https://docs.google.com/document/d/1VAzPgcHkQzpFGsWYFbtD30mHLsKFCtGIDXEkEEOoKLA/edit?usp=sharing

### Credits:

Credits to the sources of the datasets in this repository

- Karagatan Patrol : https://www.karagatanpatrol.org/
- WDPA - https://www.protectedplanet.net/en/thematic-areas/wdpa?tab=WDPA
- Marine Regions (Exclusive Economic Zones) - https://www.marineregions.org/eez.php
