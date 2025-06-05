import json
import argparse
from pathlib import Path
from typing import Dict, List
from datetime import datetime


def load_heat_data(file_path: str) -> Dict[str, Dict[str, int]]:
    """Load heatmap data from JSON file.

    Args:
        file_path: Path to the JSON file

    Returns:
        Dictionary containing the heatmap data

    Raises:
        FileNotFoundError: If the data file doesn't exist
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")
    
    with path.open("r") as f:
        return json.load(f)


def get_month_columns(data: Dict[str, Dict[str, int]]) -> List[str]:
    """Extract and sort month columns from the data.

    Args:
        data: The heatmap data dictionary

    Returns:
        List of month columns in chronological order
    """
    # Get all unique months from the data
    months = set()
    for industry_data in data.values():
        months.update(industry_data.keys())
    
    # Sort months chronologically
    return sorted(months)


def generate_heatmap(data: Dict[str, Dict[str, int]], months: List[str]) -> str:
    """Generate HTML heatmap from the data.

    Args:
        data: The heatmap data dictionary
        months: List of month columns in chronological order

    Returns:
        HTML string containing the heatmap
    """
    # Sort industries by their most recent month's value
    most_recent_month = months[-1]
    sorted_industries = sorted(
        data.items(),
        key=lambda x: x[1].get(most_recent_month, 0),
        reverse=True
    )

    # Start with the HTML structure and CSS styles
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ISM Services Report Heatmap</title>
    <style>
        body {
            font-family: system-ui, -apple-system, sans-serif;
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        .heatmap-table {
            border-collapse: collapse;
            border: 1px solid var(--pico-muted-color);
        }
        .heatmap-table th {
            background-color: var(--pico-muted-color);
            color: var(--pico-primary-inverse);
            padding-left: 1em;
            padding-right: 1em;
        }
        .heatmap-table td {
            transition: border-color 0.2s ease;
            padding-left: 1em;
            padding-right: 1em;
        }
        .heatmap-table tr:hover td {
            border: 1px solid var(--pico-primary);
        }
        .cell {
            color: black;
            text-align: center;
        }
        .growing-cell {
            background-color: rgb(var(--growing-r), 255, 0);
        }
        .contracting-cell {
            background-color: rgb(255, var(--contracting-g), 0);
        }
        .heatmap-table tr:hover .growing-cell {
            filter: brightness(1.1);
        }
        .heatmap-table tr:hover .contracting-cell {
            filter: brightness(1.1);
        }
        .industry-name {
            font-weight: bold;
            text-align: right;
            padding-right: 1rem;
        }
        .legend {
            display: flex;
            gap: 2rem;
            margin: 1rem 0;
            padding: 1rem;
            background: var(--pico-muted-color);
            border-radius: 4px;
        }
        .legend-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .legend-color {
            width: 20px;
            height: 20px;
            border: 1px solid #000;
        }
        .last-updated {
            color: #666;
            font-size: 0.9rem;
            margin-top: 1rem;
        }
    </style>
</head>
<body>
    <h1>ISM Services Report Heatmap</h1>
    <div class="legend">
        <div class="legend-item">
            <div class="legend-color" style="background: rgb(100, 255, 0);"></div>
            <span>Strong Growth</span>
        </div>
        <div class="legend-item">
            <div class="legend-color" style="background: rgb(255, 255, 0);"></div>
            <span>Stagnant Growth</span>
        </div>
        <div class="legend-item">
            <div class="legend-color" style="background: rgb(255, 100, 0);"></div>
            <span>Strong Contraction</span>
        </div>
    </div>
"""

    # Start the table
    html += '<table class="heatmap-table">\n'
    
    # Add header row with months
    html += '<tr><th class="industry-name">Industry</th>'
    for month in months:
        # Format month for display (e.g., "2024-03" -> "Mar 2024")
        date = datetime.strptime(month, '%Y-%m')
        display_month = date.strftime('%b<br>%Y')
        html += f'<th>{display_month}</th>'
    html += '</tr>\n'

    # Add data rows
    for industry, month_data in sorted_industries:
        html += '<tr>'
        html += f'<td class="industry-name">{industry}</td>'
        
        for month in months:
            value = month_data.get(month, 0)
            if value >= 0:
                # Growing industry - calculate red component (255 to 0)
                growing_r = int(255 * (1 - (value / 20)))
                html += f'<td class="cell growing-cell" style="--growing-r: {growing_r}">{value}</td>'
            else:
                # Contracting industry - calculate green component (255 to 0)
                contracting_g = int(255 * (1 - (abs(value) / 20)))
                html += f'<td class="cell contracting-cell" style="--contracting-g: {contracting_g}">{value}</td>'
        
        html += '</tr>\n'

    # Close the table
    html += '</table>'
    
    # Add last updated timestamp
    html += f"""
    <div class="last-updated">
        Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    </div>
</body>
</html>"""
    
    return html


def main():
    parser = argparse.ArgumentParser(
        description="Generate heatmap from ISM Services Report data"
    )
    parser.add_argument(
        "--input",
        "-i",
        default="data/ism_heat_data.json",
        help="Input JSON file path (default: data/ism_heat_data.json)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="data/ism_heatmap.html",
        help="Output HTML file path (default: data/ism_heatmap.html)",
    )
    args = parser.parse_args()

    try:
        # Load the data
        data = load_heat_data(args.input)
        
        # Get month columns
        months = get_month_columns(data)
        
        # Generate the heatmap
        heatmap = generate_heatmap(data, months)
        
        # Ensure output directory exists
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write to file
        with output_path.open("w") as f:
            f.write(heatmap)
        
        print(f"Heatmap saved to {args.output}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main()) 
