# chestrays
Chestrays, like xrays but for chests


## Software setup

We use conda to setup dependencies:

`conda env create -f environment.yml`

To use the shared kaggle account run the following command in the directory
of this README:

```
export KAGGLE_CONFIG_DIR=`pwd`/secrets
```

To check if worked run `kaggle kernels list -m`. It should list some kernels
and not print any warnings or errors.


## Tools

There are currently two tools in this package: `krun` and `kfetch`.

`krun` takes a notebook (with existing metadata file) and runs it as a kaggle
kernel. Optionally waiting for it to complete and downloading the output.

`kfetch` takes a notebook (with existing metadata file) and waits for it to
complete running, then fetches the output.

To initially fetch a notebook from a kernel and have the metadata created use:
`kaggle kernels pull -p kernels/create-dataturks-nih chestrays/create-pneumonia-dataturks-dataset`
This will fetch the kernel called `chestrays/create-pneumonia-dataturks-dataset`
and put it in the `kernels/create-dataturks-nih` subdirectory.


## Secrets

To get access to the secrets stored in `secrets/` install git-crypt and contact
one of the people who have the key:

* Tim Head
