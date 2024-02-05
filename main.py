import os
from utils import setup_icon_directory, get_figma_file, flatten_figma_nodes, filter_valid_nodes
from exports import export_svgs, export_assets
from dotenv import load_dotenv

def load_environment_variables():
    """Load environment variables and return Figma credentials."""
    load_dotenv()

    document_key = os.getenv('DOCUMENT_KEY')
    figma_token = os.getenv('FIGMA_TOKEN')

    if not document_key or not figma_token:
        raise Exception('Missing Figma credentials')
    
    return document_key, figma_token

def process_figma_file(document_key, figma_token):
    """Fetch, filter, and flatten Figma file nodes, then export SVGs and assets."""
    res = get_figma_file(document_key, figma_token)
    nodes = filter_valid_nodes(flatten_figma_nodes(res['document']['children']))
    return nodes

def main():
    """Main function to orchestrate the Figma file processing."""
    # Load Figma credentials
    document_key, figma_token = load_environment_variables()

    # Clear any existing path for exporting
    setup_icon_directory()

    # Process Figma file and export SVGs and assets
    nodes = process_figma_file(document_key, figma_token)
    export_svgs(nodes, document_key, figma_token)
    export_assets()

if __name__ == "__main__":
    main()
