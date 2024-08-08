## Introduction
This is a Python project developed within LabSonar/LPS to analyze stationarity in acoustic signals, aiming to define metrics for future developments in generative models with AI.

## Authors
- **Developer**: [Fábio Oliveira](https://github.com/obs-fabio)
- **Developer**: [Gabriel Lisboa](https://github.com/gabrielhblisboa)
- **Advisor**: [Natanael Junior](https://github.com/natmourajr/natmourajr)

## Usage

### Code Standard
To ensure code maintainability, it is recommended that all developed code uses typing annotations and check the code with pylint before committing.
Typing helps in defining the expected data types of variables and functions, which improves code readability and helps catch errors early.
Pylint is a tool that checks for errors in Python code, enforces a coding standard, and looks for code smells.


### Managing Multiple Libraries
This project provides a shell script `manager` to help manage multiple Python libraries. The libraries must be listed in the `Projects.txt` file.

- **install/deploy**: Commands to install (developer mode) and deploy (production mode) all libraries.
- **clone/status/pull/push/log/branch**: Execute git commands for all libraries.
- **todo**: List all TODO comments in the libraries.
- **pack**: Compress all libraries into a .tar.gz file.
- **count**: List the number of lines in each library.

#### Libraries
Currently this project depends on libraries as git submodules
- [utils](https://github.com/labsonar/utils.git)
- [signal_processing](https://github.com/labsonar/signal_processing.git)
- [acoustic_synthesis](https://github.com/labsonar/acoustic_synthesis.git)

### Installing

The project must specify which Docker environment to use or how to prepare it.

```bash
./manager check_libs
./manager install
```

## Repository Structure

The following directory structure is recommended for project development:

- **apps/:** Contains the Python scripts that leverage one or more libraries. These scripts can be designed as command-line applications for practical use.
- **notebooks/:** If desired, this directory can be added to include Jupyter Notebooks to showcase demonstrations, tutorials, and interactive code examples.


## Docker
This project was develop to run in the docker available at [docker hub](https://hub.docker.com/r/labsonar/processing)


## License

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) license. You are free to use, modify, and distribute the code for non-commercial purposes, with the condition that you provide attribution to the authors and distribute any derivative works under the same license. For more details, please refer to the license file (LICENSE.md) included in this repository.
