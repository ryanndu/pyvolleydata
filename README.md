# pyvolleydata <img src="https://github.com/ryanndu/pyvolleydata/raw/main/assets/images/pyvolleydata-logo.png" align="right" width="100" height="100"/>

--- 

## Overview

**[pyvolleydata](https://github.com/ryanndu/ceblpy)** is a Python package designed for accessing and working with data from the Pro Volleyball Federation (PVF) league and the League One Volleyball (LOVB) league.

---

## Installation

You can install **[pyvolleydata](https://github.com/ryanndu/ceblpy)** package with:

```bash
$ pip install pyvolleydata
```

---

## Usage

To retrieve the PVF points_log for a given season (e.g, 2024), use the load_pvf_points_log() function:

```
from pyvolleydata.pvf import load_pvf_points_log

# Load the 2024 PVF season points log
points_log = load_pvf_points_log(2024)

# Preview the data
print(points_log.head())
```

---

## Contributing

Found a bug? Have an idea to make pyvolleydata better? We'd love to hear from you!
- **Open an issue** on our **[GitHub Issues](https://github.com/ryanndu/pyvolleydata/issues)** page
- **Email Me** directly at **[ryandu343@gmail.com](mailto:ryandu343@gmail.com)**

All suggestions and contributions are welcome!

---

## License

`pyvolleydata` was created by Ryan Du and David Awosoga. It is licensed under the terms of the MIT license.

---

## Credits

`pyvolleydata` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).