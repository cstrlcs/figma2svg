from utils import get_figma_image_svg
import pathlib
import re
import json

SVG_TEMPLATE = '<svg xmlns="http://www.w3.org/2000/svg"><defs>{paths}</defs></svg>'

def save_svg_icon(node, key, token, directory='./output'):
    """Fetch and save an SVG icon."""
    icon_id = node.get("id")
    icon_name = node.get("name").replace('/', '_')
    
    print(f'Fetching icon: {icon_name}')
    svg_content = get_figma_image_svg(icon_id, key, token)
    
    if svg_content:
        file_path = pathlib.Path(directory) / f'{icon_name}.svg'
        file_path.write_text(svg_content)
    else:
        print(f"Failed to fetch icon '{icon_name}'.")

def export_svgs(nodes, key, token):
    """Export SVG files for each node."""
    for idx, node in enumerate(nodes, start=1):
        print(f'Fetching icon {idx}/{len(nodes)}: {node.get("name")}')
        save_svg_icon(node, key, token)

def process_svg_for_spritesheet(svg_file):
    """Process an SVG file to fit into a spritesheet."""
    svg_content = svg_file.read_text()

    # Extract and modify SVG contents for the spritesheet.
    inner_svg = re.findall(r'<svg[^>]*>(.*?)<\/svg>', svg_content, re.DOTALL)[0]
    inner_svg = re.sub(r'(stroke=")(.*?)(")', r'\1currentColor\3', inner_svg)
    inner_svg = re.sub(r'(fill=")(.*?)(")', r'\1currentColor\3', inner_svg)
    return re.sub(r'\s+', ' ', inner_svg).strip()

def export_assets(directory='./output'):
    """Create a spritesheet and list from SVG icons."""
    svg_files = list(pathlib.Path(directory).glob('*.svg'))

    svgs = [process_svg_for_spritesheet(file) for file in svg_files]
    svg_names = [file.stem for file in svg_files]

    # Generate the spritesheet
    spritesheet_content = SVG_TEMPLATE.format(paths=''.join(f'<g id="{name}">{svg}</g>' for name, svg in zip(svg_names, svgs)))
    (pathlib.Path('./') / 'output.svg').write_text(spritesheet_content)

    # Save the list of SVG names
    (pathlib.Path('./') / 'output.json').write_text(json.dumps(svg_names, indent=4))
