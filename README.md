# pyvolleydata <img src="https://github.com/ryanndu/pyvolleydata/raw/main/assets/images/pyvolleydata-logo.svg" align="right" width="150" height="150"/>

--- 

## Overview

**[pyvolleydata](https://github.com/ryanndu/pyvolleydata)** is a Python package to access, process, and analyze volleyball data from multiple professional leagues, including:
- **Major League Volleyball (MLV)**
- **League One Volleyball (LOVB)**
- **Athlete Unlimited Pro Volleyball (AUPVB)**

---

## Installation

Install the latest release of the **[pyvolleydata](https://github.com/ryanndu/pyvolleydata)** package with:

```bash
$ pip install pyvolleydata
```

---

## Quick Start

To retrieve the MLV player boxscore data for a given season (e.g, 2024), use the load_mlv_player_boxscore() function:

```
from pyvolleydata.mlv import load_pvf_player_boxscore()

# Load the 2024 MLV season player boxscore
player_boxscore = load_mlv_player_boxscore(2024)

# Preview the data
print(player_boxscore.head())
```

---

## Contributing

Contributions are welcome!
- **Open an issue** on our **[GitHub Issues](https://github.com/ryanndu/pyvolleydata/issues)** page
- **Email Me** directly at **[ryandu343@gmail.com](mailto:ryandu343@gmail.com)**

---

## License

`pyvolleydata` was created by Ryan Du and David Awosoga. It is licensed under the terms of the MIT license.

---

## Credits

`pyvolleydata` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

A big thanks to [Rebecca Lai](https://www.rebeccalai.net) for the awesome logo design!
