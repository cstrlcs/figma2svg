# figma2svg

<p align="center">
    <em>Download and process SVG Icons from a Figma page into a spritesheet and JSON list</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/cstrlcs/figma2svg?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/cstrlcs/figma2svg?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/cstrlcs/figma2svg?style=flat&color=0080ff" alt="repo-top-language">
<p>
<hr>

## Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [Running figma2svg](#-running-figma2svg)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)

---

## Overview 📖

The **figma2svg** script automates the extraction of SVG icons from a Figma project, converting them into a spritesheet and JSON list.

The project's primary goal is to streamline the process of integrating custom icons from Figma designs into web development projects.

---

## Features 🌟

- Fetch SVG icons from a Figma document.
- Process icons to ensure "**currentColor**" on both fill and stroke.
- Generate a single SVG spritesheet for all icons.
- Produce a JSON list of icons for easy reference and integration.

---

## Getting Started 🚀

**_Requirements_**

Ensure you have the following dependencies installed on your system:

- **Python**: `version 3.6+`

You will also need a Figma access token to use the API (**file key** and **personal access token**). You can obtain these by following the instructions [here](https://www.figma.com/developers/api#access-tokens).

### Installation

1. Clone the figma2svg repository:

```sh
git clone https://github.com/cstrlcs/figma2svg
```

2. Change to the project directory:

```sh
cd figma2svg
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

### Running `figma2svg`

Use the following command to run figma2svg:

```sh
python main.py
```

This will fetch the icons from your Figma file, process them into SVG format, compile them into a spritesheet, and generate a JSON list of the icons for integration into your web projects.

It may take a while, since we don't want to overload Figma's servers with too many requests.

---

## Project Roadmap 🛣️

- [ ] `► Add more CLI options to customize the output.`
- [ ] `► Option to recovery from failed downloads.`
- [ ] `► Option to update missing icons.`

---

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or ideas.

---

## License 📝

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
