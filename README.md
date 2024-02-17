<p align="center">
 <img src="logo.png" alt="Figma2SVG"/>
</p>

Download and process SVG Icons from a Figma page into a spritesheet and JSON list.

## Features 🌟

- Fetch SVG icons from a Figma document.
- Process icons to ensure "**currentColor**" on both fill and stroke.
- Generate a single SVG spritesheet for all icons.
- Produce a JSON list of icons for easy reference and integration.

## Getting Started 🚀

### Prerequisites

Ensure you have **Python 3.6+** installed on your machine. You will also need a Figma access token to use the API (**file key** and **personal access token**).

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/cstrlcs/figma2svg.git
   ```
2. Navigate into the project directory:
   ```bash
   cd figma2svg
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Setup

Copy the `.env.example` file to `.env` and fill in your Figma API token:

```plaintext
FIGMA_TOKEN=your_figma_token_here
DOCUMENT_KEY=your_document_key_here
```

## Preparation

1. Ensure all your icons are designed at exactly **24x24 pixels** to maintain uniformity and compatibility.
2. Icons must be either components or instances of a component within your Figma project.
3. The name assigned to each icon in Figma will be used as its identifier in the JSON list and as the filename in the spritesheet.
4. Set your Figma API credentials in your environment variables for secure access. This requires setting up **FIGMA_FILE_KEY** and **FIGMA_PERSONAL_ACCESS_TOKEN** in your `.env` file.

## Usage 🛠

To convert a Figma design to SVG, run:

```bash
python main.py
```

This will fetch the icons from your Figma file, process them into SVG format, compile them into a spritesheet, and generate a JSON list of the icons for integration into your web projects.

It may take a while, since we don't want to overload Figma's servers with too many requests.

## Contributing 🤝

Feel free to contribute to this project. Any help is greatly appreciated.

## License 📄

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
