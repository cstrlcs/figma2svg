import requests, os, shutil

def fetch(url, token):
    """Fetch a URL with an authorization token."""
    headers = {"X-Figma-Token": token}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        exception = response.json().get('err')
        exit(f'Failed to fetch: {exception}')

    return response.json()

def get_figma_file(key, token):
    """Fetch a Figma file's data."""
    url = f'https://api.figma.com/v1/files/{key}'
    return fetch(url, token)

def get_figma_image_svg(id, key, token):
    """Fetch an SVG image from Figma."""
    url = f'https://api.figma.com/v1/images/{key}?ids={id}&format=svg&use_absolute_bounds=true'
    
    response = fetch(url, token)
    image_url = response.get('images', {}).get(id)

    if image_url:
        return requests.get(image_url).text
    
    return None

def flatten_figma_nodes(nodes):
    """Recursively flatten a list of Figma nodes."""
    flattened = []
    for node in nodes:
        flattened.append(node)
        if 'children' in node:
            flattened.extend(flatten_figma_nodes(node['children']))
    return flattened

def is_valid_node(node):
    """Check if a Figma node is a valid component or instance with specific dimensions."""
    try:
        dimensions = node.get('absoluteBoundingBox', {})
        width, height = dimensions.get('width'), dimensions.get('height')
        
        is_correct_type = node.get('type') in ['COMPONENT', 'INSTANCE']
        is_square_and_correct_size = width == height == 24.0
        return is_correct_type and is_square_and_correct_size
    except TypeError:
        return False

def filter_valid_nodes(nodes):
    """Filter nodes by validity."""
    return [node for node in nodes if is_valid_node(node)]
    
def setup_icon_directory(path='./output', clear=False):
    """Ensure the icon directory is and ready."""
    if os.path.exists(path) and clear:
        shutil.rmtree(path, ignore_errors=True)
    os.makedirs(path, exist_ok=True)
