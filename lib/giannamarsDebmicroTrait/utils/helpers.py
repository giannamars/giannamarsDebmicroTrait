import os

def html_add_batch_summary(params, api_results, html_output_dir):

    html_file = 'test' + '.html'
    output_html_file_path = os.path.join(html_output_dir, html_file)

    img_dpi = 300
    img_units = "in"
    img_pix_width = 1200
    img_in_width = round(float(img_pix_width) / float(img_dpi), 1)
    img_html_width = img_pix_width // 2

    # Make HTML
    intree_name = 'intreename'

    html_report_lines = []
    html_report_lines.append('<html>')
    html_report_lines.append('<head>')
    html_report_lines.append('<title>KBase Tree: {0}</title>'.format(intree_name))
    html_report_lines.append('<style>')
    html_report_lines.append('.tab {')
    html_report_lines.append('  display: none;')
    html_report_lines.append('}')
    html_report_lines.append('.active {')
    html_report_lines.append('  display: block;')
    html_report_lines.append('}')
    html_report_lines.append('.tab-button {')  # Added class for tab buttons
    html_report_lines.append('  background-color: white;')  # Set background color to white
    html_report_lines.append('  padding: 10px 20px;')  # Adjust padding to increase button size
    html_report_lines.append('  font-size: 16px;')  # Adjust font size
    html_report_lines.append('  border: 1px solid #ccc;')  # Add border for button
    html_report_lines.append('  border-radius: 5px;')  # Add border radius for button
    html_report_lines.append('  cursor: pointer;')
    html_report_lines.append('}')
    html_report_lines.append('</style>')
    html_report_lines.append('</head>')
    html_report_lines.append('<body>')

    # Tab navigation
    html_report_lines.append('<div>')
    html_report_lines.append('<button class="tab-button" onclick="showTab(0)">Substrate Thermodynamic Traits</button>')  # Added class for tab buttons
    html_report_lines.append('<button class="tab-button" onclick="showTab(1)">Substrate Kinetic Traits</button>')  # Added class for tab buttons
    html_report_lines.append('<button class="tab-button" onclick="showTab(2)">Phenotypic Traits</button>')  # Added class for tab buttons
    html_report_lines.append('<button class="tab-button" onclick="showTab(3)">Table</button>') 
    html_report_lines.append('</div>')

    # Tab content
    html_report_lines.append('<div id="tabContent">')
    html_report_lines.append('<div class="tab active">')
    html_report_lines.append('<div><h2>Image 1</h2></div>')  # Header for Image 1
    html_report_lines.append('<img width="{0}" src="{1}">'.format(img_html_width, api_results["png1"]))
    html_report_lines.append('</div>')
    html_report_lines.append('<div class="tab">')
    html_report_lines.append('<div><h2>Image 2</h2></div>')  # Header for Image 1
    html_report_lines.append('<img width="{0}" src="{1}">'.format(img_html_width, api_results["png1"]))
    html_report_lines.append('</div>')
    html_report_lines.append('<div class="tab">')
    html_report_lines.append('<div><h2>Background</h2></div>') 
    html_report_lines.append('<div style="width: 100%; height: 100vh; background-color: black;"></div>')
    html_report_lines.append('</div>')
    html_report_lines.append('<div class="tab">')
    html_report_lines.append('<div><h2>Table</h2></div>')  # Header for the table tab

    # Table content
    html_report_lines.append('<table border="1">')  # Basic table with borders
    # Table header row
    html_report_lines.append('<tr>')
    for header in api_results["header"]:
        html_report_lines.append('<th>{}</th>'.format(header))
    html_report_lines.append('</tr>')
    # Data rows
    for row in api_results["data"]:
        html_report_lines.append('<tr>')
        for cell in row:
            html_report_lines.append('<td>{}</td>'.format(cell))
        html_report_lines.append('</tr>')
    html_report_lines.append('</table>')
    html_report_lines.append('</div>')
    html_report_lines.append('</div>')
 

    # JavaScript for tab switching
    html_report_lines.append('<script>')
    html_report_lines.append('function showTab(index) {')
    html_report_lines.append('  var tabs = document.getElementsByClassName("tab");')
    html_report_lines.append('  for (var i = 0; i < tabs.length; i++) {')
    html_report_lines.append('    tabs[i].classList.remove("active");')
    html_report_lines.append('  }')
    html_report_lines.append('  tabs[index].classList.add("active");')
    html_report_lines.append('}')
    html_report_lines.append('</script>')

    html_report_lines.append('</body>')
    html_report_lines.append('</html>')

    html_report_str = "\n".join(html_report_lines)


     # Write HTML to file
    with open(output_html_file_path, 'w') as html_handle:
        html_handle.write(html_report_str)


    return {'path': output_html_file_path,
            'name': os.path.basename(output_html_file_path),
            'description': 'HTML report for batch mode simulations'}


