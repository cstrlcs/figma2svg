# Figma2SVG

Download and process SVG Icons from a Figma page into a spritesheet and JSON list.

## Features

- Fetch SVG icons from a Figma document.
- Process icons to ensure "currentColor" on both fill and stroke.
- Generate a single SVG spritesheet for all icons.
- Produce a JSON list of icons for easy reference and integration.

### Prerequisites

- Ensure Python 3.6+ is installed on your system.
- Obtain your Figma API credentials (file key and personal access token).

### Installation

1. Clone this repository or download the source code.
2. Install required dependencies:

```bash
pip install requests
```

## Preparation

1. Ensure all your icons are designed at exactly 24x24 pixels to maintain uniformity and compatibility.
2. Icons must be either components or instances of a component within your Figma project.
3. The name assigned to each icon in Figma will be used as its identifier in the JSON list and as the filename in the spritesheet.
4. Set your Figma API credentials in your environment variables for secure access. This requires setting up FIGMA_FILE_KEY and FIGMA_PERSONAL_ACCESS_TOKEN in your environment.

```bash
export FIGMA_FILE_KEY='your_figma_file_key'
export FIGMA_PERSONAL_ACCESS_TOKEN='your_figma_personal_access_token'
```

## Usage

After setting up your environment and Figma project according to the guidelines provided, run the figma2svg script to start the download and processing of your SVG icons:

```bash
python main.py
```

This will fetch the icons from your Figma file, process them into SVG format, compile them into a spritesheet, and generate a JSON list of the icons for integration into your web projects.

It may take a while, since we don't want to overload Figma's servers with too many requests.
